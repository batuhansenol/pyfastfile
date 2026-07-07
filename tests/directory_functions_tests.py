"""Tests for directory helpers."""

from pyfastfile.directory_functions.mod_dir_create_directory import dir_create
from pyfastfile.directory_functions.mod_dir_delete import dir_delete
from pyfastfile.directory_functions.mod_dir_is_directory import dir_is_directory
from pyfastfile.directory_functions.mod_dir_is_empty import dir_is_empty
from pyfastfile.directory_functions.mod_dir_list_directory import dir_list
from pyfastfile.directory_functions.mod_dir_size_directory import dir_size
from pyfastfile.directory_functions.mod_dir_size_directory_mb import dir_size_mb

from .conftest import print_test_result


def test_dir_create_creates_directory(tmp_path):
    print_test_result("dir_create", "creates a directory", True)
    target_dir = tmp_path / "created"

    dir_create(str(target_dir))

    assert dir_is_directory(str(target_dir))


def test_dir_is_directory_detects_directory(tmp_path):
    print_test_result("dir_is_directory", "detects a directory", True)
    target_dir = tmp_path / "folder"
    target_dir.mkdir()

    assert dir_is_directory(str(target_dir)) is True


def test_dir_is_empty_reports_empty_directory(tmp_path):
    print_test_result("dir_is_empty", "reports whether a directory is empty", True)
    target_dir = tmp_path / "empty"
    target_dir.mkdir()

    assert dir_is_empty(str(target_dir)) is True


def test_dir_list_returns_contents(tmp_path):
    print_test_result("dir_list", "returns the directory contents", True)
    target_dir = tmp_path / "folder"
    nested_dir = target_dir / "nested"
    nested_dir.mkdir(parents=True)
    (nested_dir / "file.txt").write_text("data", encoding="utf-8")

    assert "nested" in dir_list(str(target_dir))


def test_dir_size_reports_bytes(tmp_path):
    print_test_result("dir_size", "reports the size in bytes", True)
    target_dir = tmp_path / "folder"
    nested_dir = target_dir / "nested"
    nested_dir.mkdir(parents=True)
    (nested_dir / "file.txt").write_text("data", encoding="utf-8")

    assert dir_size(str(target_dir)) > 0


def test_dir_size_mb_reports_megabytes(tmp_path):
    print_test_result("dir_size_mb", "reports the size in megabytes", True)
    target_dir = tmp_path / "folder"
    nested_dir = target_dir / "nested"
    nested_dir.mkdir(parents=True)
    (nested_dir / "file.txt").write_text("data", encoding="utf-8")

    assert dir_size_mb(str(target_dir)) > 0


def test_dir_delete_removes_directory(tmp_path):
    print_test_result("dir_delete", "removes a directory", True)
    target_dir = tmp_path / "empty"
    target_dir.mkdir()

    dir_delete(str(target_dir))

    assert not target_dir.exists()
