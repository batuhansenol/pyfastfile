"""Tests for debug helpers."""

import pytest

from pyfastfile.debug_functions.deb_file_not_found import exists, fnf
from pyfastfile.debug_functions.deb_parameter_check import parameter_check

from .conftest import print_test_result


def test_exists_reports_existing_file(tmp_path):
    print_test_result("exists", "reports whether a file exists", True)
    file_path = tmp_path / "sample.txt"
    file_path.write_text("hello", encoding="utf-8")

    assert exists(str(file_path)) is True


def test_fnf_accepts_existing_file(tmp_path):
    print_test_result("fnf", "accepts an existing file", True)
    file_path = tmp_path / "sample.txt"
    file_path.write_text("hello", encoding="utf-8")

    assert fnf(str(file_path)) is None


def test_parameter_check_rejects_none_values():
    print_test_result("parameter_check", "rejects None values", True)
    with pytest.raises(ValueError):
        parameter_check(None)


def test_fnf_raises_for_missing_file(tmp_path):
    print_test_result("fnf", "raises an error for a missing file", True)
    with pytest.raises(FileNotFoundError):
        fnf(str(tmp_path / "missing.txt"))
