"""Tests for main file helpers."""

from pyfastfile.main_functions.mod_append import append
from pyfastfile.main_functions.mod_clear import clear
from pyfastfile.main_functions.mod_count_lines import count_lines
from pyfastfile.main_functions.mod_delete import delete
from pyfastfile.main_functions.mod_exists import exists
from pyfastfile.main_functions.mod_find import find
from pyfastfile.main_functions.mod_find_num import find_num
from pyfastfile.main_functions.mod_getline import getline
from pyfastfile.main_functions.mod_move import move
from pyfastfile.main_functions.mod_overwrite import overwrite
from pyfastfile.main_functions.mod_read import read
from pyfastfile.main_functions.mod_read_bytes import read_bytes
from pyfastfile.main_functions.mod_readlines import readlines
from pyfastfile.main_functions.mod_rename import rename
from pyfastfile.main_functions.mod_size import size
from pyfastfile.main_functions.mod_size_mb import size_mb
from pyfastfile.main_functions.mod_touch import touch

from .conftest import print_test_result


def test_text_file_helpers(tmp_path):
    print_test_result("text_file_helpers", "manipulates text file content", True)
    file_path = tmp_path / "notes.txt"
    file_path.write_text("", encoding="utf-8")

    append(str(file_path), "alpha")
    append(str(file_path), "beta", newline=False)
    assert read(str(file_path)) == "alpha\nbeta"
    assert count_lines(str(file_path)) == 2
    assert find(str(file_path), "beta") == ["beta"]
    assert find_num(str(file_path), "beta") == [1]
    assert getline(str(file_path), 1) == "beta"
    assert readlines(str(file_path), newline=False) == ["alpha", "beta"]
    assert read_bytes(str(file_path)) == b"alpha\nbeta"

    clear(str(file_path))
    assert read(str(file_path)) == ""


def test_file_management_helpers(tmp_path):
    print_test_result("file_management_helpers", "manages the file lifecycle", True)
    file_path = tmp_path / "source.txt"
    file_path.write_text("data", encoding="utf-8")

    touch(str(tmp_path / "created.txt"))
    assert exists(str(tmp_path / "created.txt")) is True

    overwrite(str(file_path), "new-data")
    assert read(str(file_path)) == "new-data"

    renamed_path = tmp_path / "renamed.txt"
    rename(str(file_path), str(renamed_path))
    assert exists(str(renamed_path)) is True

    moved_path = tmp_path / "moved" / "renamed.txt"
    moved_path.parent.mkdir()
    move(str(renamed_path), str(moved_path))
    assert exists(str(moved_path)) is True

    assert size(str(moved_path)) > 0
    assert size_mb(str(moved_path)) >= 0

    delete(str(moved_path))
    assert exists(str(moved_path)) is False
