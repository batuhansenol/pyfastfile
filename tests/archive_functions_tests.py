"""Tests for archive-related helpers."""

from pyfastfile.archive_functions.mod_tar_append import tar_append
from pyfastfile.archive_functions.mod_tar_create import tar_create
from pyfastfile.archive_functions.mod_tar_extract import tar_extract
from pyfastfile.archive_functions.mod_tar_list import tar_list
from pyfastfile.archive_functions.mod_tar_remove import tar_remove
from pyfastfile.archive_functions.mod_zip_append import zip_append
from pyfastfile.archive_functions.mod_zip_create import zip_create
from pyfastfile.archive_functions.mod_zip_extract import zip_extract
from pyfastfile.archive_functions.mod_zip_is_zipfile import zip_is_zipfile
from pyfastfile.archive_functions.mod_zip_list import zip_list

from .conftest import print_test_result


def test_tar_create_creates_archive(tmp_path):
    print_test_result("tar_create", "creates an archive", True)
    source_dir = tmp_path / "source"
    source_dir.mkdir()
    (source_dir / "hello.txt").write_text("hello", encoding="utf-8")
    archive_path = tmp_path / "sample.tar"

    tar_create(str(source_dir), str(archive_path))

    assert archive_path.exists()


def test_tar_list_lists_members(tmp_path):
    print_test_result("tar_list", "lists archive members", True)
    source_dir = tmp_path / "source"
    source_dir.mkdir()
    (source_dir / "hello.txt").write_text("hello", encoding="utf-8")
    archive_path = tmp_path / "sample.tar"
    tar_create(str(source_dir), str(archive_path))

    names = tar_list(str(archive_path))

    assert any("hello.txt" in name for name in names)


def test_tar_append_adds_file(tmp_path):
    print_test_result("tar_append", "adds a file to the archive", True)
    source_dir = tmp_path / "source"
    source_dir.mkdir()
    (source_dir / "hello.txt").write_text("hello", encoding="utf-8")
    archive_path = tmp_path / "sample.tar"
    tar_create(str(source_dir), str(archive_path))
    extra_file = tmp_path / "extra.txt"
    extra_file.write_text("extra", encoding="utf-8")

    tar_append(str(archive_path), str(extra_file))

    assert any("extra.txt" in name for name in tar_list(str(archive_path)))


def test_tar_remove_removes_member(tmp_path):
    print_test_result("tar_remove", "removes a member from the archive", True)
    source_dir = tmp_path / "source"
    source_dir.mkdir()
    (source_dir / "hello.txt").write_text("hello", encoding="utf-8")
    archive_path = tmp_path / "sample.tar"
    tar_create(str(source_dir), str(archive_path))
    extra_file = tmp_path / "extra.txt"
    extra_file.write_text("extra", encoding="utf-8")
    tar_append(str(archive_path), str(extra_file))

    tar_remove(str(archive_path), "extra.txt")

    assert not any("extra.txt" in name for name in tar_list(str(archive_path)))


def test_tar_extract_extracts_files(tmp_path):
    print_test_result("tar_extract", "extracts files from the archive", True)
    source_dir = tmp_path / "source"
    source_dir.mkdir()
    (source_dir / "hello.txt").write_text("hello", encoding="utf-8")
    archive_path = tmp_path / "sample.tar"
    tar_create(str(source_dir), str(archive_path))
    extract_dir = tmp_path / "extracted"
    extract_dir.mkdir()

    tar_extract(str(archive_path), str(extract_dir))

    assert any(path.name == "hello.txt" for path in extract_dir.rglob("hello.txt"))


def test_zip_create_creates_archive(tmp_path):
    print_test_result("zip_create", "creates a zip archive", True)
    source_file = tmp_path / "sample.txt"
    source_file.write_text("zip-data", encoding="utf-8")
    archive_path = tmp_path / "sample.zip"

    zip_create(str(source_file), str(archive_path))

    assert archive_path.exists()


def test_zip_is_zipfile_detects_archive(tmp_path):
    print_test_result("zip_is_zipfile", "detects a zip archive", True)
    source_file = tmp_path / "sample.txt"
    source_file.write_text("zip-data", encoding="utf-8")
    archive_path = tmp_path / "sample.zip"
    zip_create(str(source_file), str(archive_path))

    assert zip_is_zipfile(str(archive_path)) is True


def test_zip_list_lists_members(tmp_path):
    print_test_result("zip_list", "lists zip members", True)
    source_file = tmp_path / "sample.txt"
    source_file.write_text("zip-data", encoding="utf-8")
    archive_path = tmp_path / "sample.zip"
    zip_create(str(source_file), str(archive_path))

    assert zip_list(str(archive_path)) == ["sample.txt"]


def test_zip_append_adds_file(tmp_path):
    print_test_result("zip_append", "adds a file to the zip archive", True)
    source_file = tmp_path / "sample.txt"
    source_file.write_text("zip-data", encoding="utf-8")
    archive_path = tmp_path / "sample.zip"
    zip_create(str(source_file), str(archive_path))
    extra_file = tmp_path / "extra.txt"
    extra_file.write_text("extra", encoding="utf-8")

    zip_append(str(archive_path), str(extra_file))

    assert "extra.txt" in zip_list(str(archive_path))


def test_zip_extract_extracts_files(tmp_path):
    print_test_result("zip_extract", "extracts files from the zip archive", True)
    source_file = tmp_path / "sample.txt"
    source_file.write_text("zip-data", encoding="utf-8")
    archive_path = tmp_path / "sample.zip"
    zip_create(str(source_file), str(archive_path))
    extract_dir = tmp_path / "unzipped"
    extract_dir.mkdir()

    zip_extract(str(archive_path), str(extract_dir))

    assert (extract_dir / "sample.txt").exists()



