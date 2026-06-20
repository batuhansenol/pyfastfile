
from ...debug_functions import check

from ..modules import (
    AESModeOfOperationCTR,
    AESModeOfOperationCBC,
    AESModeOfOperationCFB,
    AESModeOfOperationECB,
    AESModeOfOperationOFB,
    Counter
)

BLOCK_SIZE = 16


def pad(data):
    pad_len = BLOCK_SIZE - (len(data) % BLOCK_SIZE)
    return data + bytes([pad_len] * pad_len)


def unpad(data):
    pad_len = data[-1]
    return data[:-pad_len]


def get_cipher(key, mode, iv):
    mode = mode.lower()

    if mode == "ecb":
        return AESModeOfOperationECB(key)

    if mode == "cbc":
        return AESModeOfOperationCBC(key, iv=iv)

    if mode == "cfb":
        return AESModeOfOperationCFB(
            key,
            iv=iv,
            segment_size=1
        )

    if mode == "ofb":
        return AESModeOfOperationOFB(key, iv=iv)

    if mode == "ctr":
        ctr = Counter(
            initial_value=int.from_bytes(iv, "big")
        )
        return AESModeOfOperationCTR(
            key,
            counter=ctr
        )

    raise ValueError("Unsupported mode")


def encrypt_file(
    input_path,
    output_path,
    key,
    mode="cbc",
    iv=None
):
    if len(key) not in (16, 24, 32):
        raise ValueError("Invalid key length")

    check(iv)

    cipher = get_cipher(key, mode, iv)

    with open(input_path, "rb") as f:
        data = f.read()

    if mode.lower() in ("ecb", "cbc"):
        data = pad(data)

        encrypted_data = b""
        for i in range(0, len(data), BLOCK_SIZE):
            encrypted_data += cipher.encrypt(
                data[i:i + BLOCK_SIZE]
            )
    else:
        encrypted_data = cipher.encrypt(data)

    with open(output_path, "wb") as f:
        if mode.lower() != "ecb":
            f.write(iv)

        f.write(encrypted_data)


def decrypt_file(
    input_path,
    output_path,
    key,
    mode="cbc"
):
    if len(key) not in (16, 24, 32):
        raise ValueError("Invalid key length")

    mode = mode.lower()

    with open(input_path, "rb") as f:
        if mode != "ecb":
            iv = f.read(BLOCK_SIZE)
        else:
            iv = None

        encrypted_data = f.read()

    cipher = get_cipher(key, mode, iv)

    if mode in ("ecb", "cbc"):
        decrypted_data = b""

        for i in range(
            0,
            len(encrypted_data),
            BLOCK_SIZE
        ):
            decrypted_data += cipher.decrypt(
                encrypted_data[i:i + BLOCK_SIZE]
            )

        decrypted_data = unpad(decrypted_data)

    else:
        decrypted_data = cipher.decrypt(
            encrypted_data
        )

    with open(output_path, "wb") as f:
        f.write(decrypted_data)