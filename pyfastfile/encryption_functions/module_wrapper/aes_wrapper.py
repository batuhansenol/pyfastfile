import hashlib
import hmac
import os
from typing import Optional

from ..modules import (
    AESModeOfOperationCBC,
    AESModeOfOperationCFB,
    AESModeOfOperationCTR,
    AESModeOfOperationGCM,
    AESModeOfOperationOFB,
    Counter,
)

SUPPORTED_KEY_SIZES = (16, 24, 32)
GCM_IV_SIZE = 12
CBC_IV_SIZE = 16
CTR_COUNTER_SIZE = 16

_MAGIC = b"AESWRAP1"


def _validate_key(key: bytes) -> None:
    if not isinstance(key, (bytes, bytearray)):
        raise TypeError("Key must be bytes or bytearray")
    if len(key) not in SUPPORTED_KEY_SIZES:
        raise ValueError(
            f"Invalid key size: {len(key)} bytes. "
            f"Supported sizes: {SUPPORTED_KEY_SIZES}"
        )


def _pkcs7_pad(data: bytes, block_size: int = 16) -> bytes:
    pad_len = block_size - (len(data) % block_size)
    return data + bytes([pad_len] * pad_len)


def _pkcs7_unpad(data: bytes) -> bytes:
    if not data:
        raise ValueError("Empty data; cannot remove padding")
    pad_len = data[-1]
    if pad_len < 1 or pad_len > 16:
        raise ValueError(f"Invalid PKCS#7 padding value: {pad_len}")
    if data[-pad_len:] != bytes([pad_len] * pad_len):
        raise ValueError(
            "Invalid PKCS#7 padding; data or key might be incorrect"
        )
    return data[:-pad_len]


def _derive_key(password: str, salt: bytes, key_size: int = 32) -> bytes:
    return hashlib.pbkdf2_hmac(
        "sha256",
        password.encode(),
        salt,
        iterations=200_000,
        dklen=key_size,
    )


def _cbc_encrypt_blocks(key: bytes, iv: bytes, plaintext: bytes) -> bytes:
    cipher = AESModeOfOperationCBC(key, iv=iv)
    blocks = [plaintext[i:i + 16] for i in range(0, len(plaintext), 16)]
    return b"".join(cipher.encrypt(b) for b in blocks)


def _cbc_decrypt_blocks(key: bytes, iv: bytes, ciphertext: bytes) -> bytes:
    cipher = AESModeOfOperationCBC(key, iv=iv)
    blocks = [ciphertext[i:i + 16] for i in range(0, len(ciphertext), 16)]
    return b"".join(cipher.decrypt(b) for b in blocks)


class GCMEncryptor:
    def __init__(self, key: bytes, tag_length: int = 16):
        _validate_key(key)
        if not 4 <= tag_length <= 16:
            raise ValueError("tag_length must be between 4 and 16")
        self._key = key
        self._tag_length = tag_length

    def encrypt_bytes(
        self, plaintext: bytes, associated_data: bytes = b""
    ) -> bytes:
        iv = os.urandom(GCM_IV_SIZE)
        cipher = AESModeOfOperationGCM(
            self._key,
            iv=iv,
            associated_data=associated_data,
            tag_length=self._tag_length,
        )
        ciphertext = cipher.encrypt(plaintext)
        tag = cipher.tag

        if isinstance(ciphertext, str):
            ciphertext = ciphertext.encode("latin-1")
        if isinstance(tag, str):
            tag = tag.encode("latin-1")

        return _MAGIC + iv + bytes([self._tag_length]) + tag + ciphertext

    def decrypt_bytes(
        self, blob: bytes, associated_data: bytes = b""
    ) -> bytes:
        if not blob.startswith(_MAGIC):
            raise ValueError("Invalid file format or missing magic byte")

        offset = len(_MAGIC)
        iv = blob[offset:offset + GCM_IV_SIZE]
        offset += GCM_IV_SIZE
        tag_len = blob[offset]
        offset += 1
        tag = blob[offset:offset + tag_len]
        offset += tag_len
        ciphertext = blob[offset:]

        cipher = AESModeOfOperationGCM(
            self._key,
            iv=iv,
            associated_data=associated_data,
            tag_length=tag_len,
        )
        plaintext = cipher.decrypt(ciphertext, tag=tag)

        if isinstance(plaintext, str):
            plaintext = plaintext.encode("latin-1")
        return plaintext

    def encrypt_file(
        self, src_path: str, dst_path: str, associated_data: bytes = b""
    ) -> None:
        with open(src_path, "rb") as f:
            plaintext = f.read()
        blob = self.encrypt_bytes(plaintext, associated_data)
        with open(dst_path, "wb") as f:
            f.write(blob)

    def decrypt_file(
        self, src_path: str, dst_path: str, associated_data: bytes = b""
    ) -> None:
        with open(src_path, "rb") as f:
            blob = f.read()
        plaintext = self.decrypt_bytes(blob, associated_data)
        with open(dst_path, "wb") as f:
            f.write(plaintext)


class CBCEncryptor:
    _HMAC_SIZE = 32

    def __init__(self, key: bytes):
        _validate_key(key)
        self._enc_key = key
        self._mac_key = bytes(b ^ 0x5C for b in key) + b"\x00" * (32 - len(key))

    def _compute_mac(self, iv: bytes, ciphertext: bytes) -> bytes:
        return hmac.new(
            self._mac_key, iv + ciphertext, hashlib.sha256
        ).digest()

    def encrypt_bytes(self, plaintext: bytes) -> bytes:
        iv = os.urandom(CBC_IV_SIZE)
        padded = _pkcs7_pad(plaintext)
        ciphertext = _cbc_encrypt_blocks(self._enc_key, iv, padded)
        mac = self._compute_mac(iv, ciphertext)
        return _MAGIC + iv + mac + ciphertext

    def decrypt_bytes(self, blob: bytes) -> bytes:
        if not blob.startswith(_MAGIC):
            raise ValueError("Invalid file format or missing magic byte")

        offset = len(_MAGIC)
        iv = blob[offset:offset + CBC_IV_SIZE]
        offset += CBC_IV_SIZE
        mac_stored = blob[offset:offset + self._HMAC_SIZE]
        offset += self._HMAC_SIZE
        ciphertext = blob[offset:]

        mac_expected = self._compute_mac(iv, ciphertext)
        if not hmac.compare_digest(mac_stored, mac_expected):
            raise ValueError(
                "MAC verification failed; data or key might be incorrect"
            )

        padded = _cbc_decrypt_blocks(self._enc_key, iv, ciphertext)
        return _pkcs7_unpad(padded)

    def encrypt_file(self, src_path: str, dst_path: str) -> None:
        with open(src_path, "rb") as f:
            data = f.read()
        with open(dst_path, "wb") as f:
            f.write(self.encrypt_bytes(data))

    def decrypt_file(self, src_path: str, dst_path: str) -> None:
        with open(src_path, "rb") as f:
            blob = f.read()
        with open(dst_path, "wb") as f:
            f.write(self.decrypt_bytes(blob))


class CTREncryptor:
    _HMAC_SIZE = 32

    def __init__(self, key: bytes):
        _validate_key(key)
        self._key = key
        self._mac_key = bytes(b ^ 0x36 for b in key) + b"\x00" * (32 - len(key))

    def _compute_mac(self, nonce: bytes, ciphertext: bytes) -> bytes:
        return hmac.new(
            self._mac_key, nonce + ciphertext, hashlib.sha256
        ).digest()

    def _make_counter(self, nonce: bytes) -> Counter:
        return Counter(initial_value=int.from_bytes(nonce, "big"))

    def encrypt_bytes(self, plaintext: bytes) -> bytes:
        nonce = os.urandom(CTR_COUNTER_SIZE)
        cipher = AESModeOfOperationCTR(
            self._key, counter=self._make_counter(nonce)
        )
        ciphertext = cipher.encrypt(plaintext)
        if isinstance(ciphertext, str):
            ciphertext = ciphertext.encode("latin-1")
        mac = self._compute_mac(nonce, ciphertext)
        return _MAGIC + nonce + mac + ciphertext

    def decrypt_bytes(self, blob: bytes) -> bytes:
        if not blob.startswith(_MAGIC):
            raise ValueError("Invalid file format or missing magic byte")

        offset = len(_MAGIC)
        nonce = blob[offset:offset + CTR_COUNTER_SIZE]
        offset += CTR_COUNTER_SIZE
        mac_stored = blob[offset:offset + self._HMAC_SIZE]
        offset += self._HMAC_SIZE
        ciphertext = blob[offset:]

        if not hmac.compare_digest(
            self._compute_mac(nonce, ciphertext), mac_stored
        ):
            raise ValueError(
                "MAC verification failed; data or key might be incorrect"
            )

        cipher = AESModeOfOperationCTR(
            self._key, counter=self._make_counter(nonce)
        )
        plaintext = cipher.decrypt(ciphertext)
        if isinstance(plaintext, str):
            plaintext = plaintext.encode("latin-1")
        return plaintext

    def encrypt_file(self, src_path: str, dst_path: str) -> None:
        with open(src_path, "rb") as f:
            data = f.read()
        with open(dst_path, "wb") as f:
            f.write(self.encrypt_bytes(data))

    def decrypt_file(self, src_path: str, dst_path: str) -> None:
        with open(src_path, "rb") as f:
            blob = f.read()
        with open(dst_path, "wb") as f:
            f.write(self.decrypt_bytes(blob))


def derive_key_from_password(
    password: str, salt: Optional[bytes] = None, key_size: int = 32
) -> tuple[bytes, bytes]:
    if key_size not in SUPPORTED_KEY_SIZES:
        raise ValueError(f"Invalid key_size: {key_size}")
    if salt is None:
        salt = os.urandom(16)
    key = _derive_key(password, salt, key_size)
    return key, salt


def encrypt_file(
    src_path: str,
    dst_path: str,
    key: bytes,
    mode: str = "gcm",
    associated_data: bytes = b"",
) -> None:
    mode = mode.lower()
    if mode == "gcm":
        GCMEncryptor(key).encrypt_file(src_path, dst_path, associated_data)
    elif mode == "cbc":
        CBCEncryptor(key).encrypt_file(src_path, dst_path)
    elif mode == "ctr":
        CTREncryptor(key).encrypt_file(src_path, dst_path)
    else:
        raise ValueError(
            f"Unknown mode: '{mode}'. Supported modes: gcm, cbc, ctr"
        )


def decrypt_file(
    src_path: str,
    dst_path: str,
    key: bytes,
    mode: str = "gcm",
    associated_data: bytes = b"",
) -> None:
    mode = mode.lower()
    if mode == "gcm":
        GCMEncryptor(key).decrypt_file(src_path, dst_path, associated_data)
    elif mode == "cbc":
        CBCEncryptor(key).decrypt_file(src_path, dst_path)
    elif mode == "ctr":
        CTREncryptor(key).decrypt_file(src_path, dst_path)
    else:
        raise ValueError(
            f"Unknown mode: '{mode}'. Supported modes: gcm, cbc, ctr"
        )