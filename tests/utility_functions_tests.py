"""Tests for utility helpers."""

import sys

import pyfastfile.utility_functions.mod_copy_to_clipboard as mod_copy_to_clipboard
from pyfastfile.utility_functions.mod_copy_to_clipboard import copy_to_clipboard
from pyfastfile.utility_functions.mod_decrypt_bytes import decrypt_bytes
from pyfastfile.utility_functions.mod_destroynewline import destroynewline
from pyfastfile.utility_functions.mod_encrypt_bytes import encrypt_bytes
from pyfastfile.utility_functions.mod_lmap import limp

from .conftest import print_test_result


def test_utility_helpers(monkeypatch):
    print_test_result("utility_helpers", "covers bytes and clipboard helpers", True)
    key = b"1234567890123456"
    payload = b"payload"

    encrypted = encrypt_bytes(payload, key)
    assert decrypt_bytes(encrypted, key) == payload
    assert destroynewline("hello\n") == "hello"
    assert limp(lambda value: value * 2, [1, 2, 3]) == [2, 4, 6]

    calls = []

    def fake_run(cmd, input=None, check=None):
        calls.append((cmd, input))
        return None

    monkeypatch.setattr(sys, "platform", "linux")
    monkeypatch.setattr(mod_copy_to_clipboard.subprocess, "run", fake_run)
    copy_to_clipboard("hello")
    assert calls
    assert calls[0][0][0] == "wl-copy"
