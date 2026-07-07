"""Tests for encryption helpers."""

from pyfastfile.encryption_functions.mod_decrypt_file import enc_decrypt_file
from pyfastfile.encryption_functions.mod_encrypt_file import enc_encrypt_file

from .conftest import print_test_result


def test_encryption_roundtrip(tmp_path):
    print_test_result("encryption_roundtrip", "encrypts and decrypts a file", True)
    source_path = tmp_path / "plain.txt"
    encrypted_path = tmp_path / "plain.enc"
    decrypted_path = tmp_path / "plain.out.txt"
    source_path.write_bytes(b"secret-data")

    key = b"1234567890123456"
    enc_encrypt_file(str(source_path), str(encrypted_path), key)
    enc_decrypt_file(str(encrypted_path), str(decrypted_path), key)

    assert decrypted_path.read_bytes() == b"secret-data"
