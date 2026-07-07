"""Tests for CSV helpers."""

from pyfastfile.csv_functions.mod_csv_append import csv_append
from pyfastfile.csv_functions.mod_csv_count import csv_count
from pyfastfile.csv_functions.mod_csv_getcolumn import csv_getcolumn
from pyfastfile.csv_functions.mod_csv_getdata import csv_getdata
from pyfastfile.csv_functions.mod_csv_getheader import csv_getheader
from pyfastfile.csv_functions.mod_csv_getrow import csv_getrow
from pyfastfile.csv_functions.mod_csv_overwrite import csv_overwrite
from pyfastfile.csv_functions.mod_csv_updaterow import csv_updaterow

from .conftest import print_test_result


def test_csv_overwrite_writes_rows(tmp_path):
    print_test_result("csv_overwrite", "writes rows to the CSV file", True)
    csv_path = tmp_path / "people.csv"

    csv_overwrite(str(csv_path), [["name", "age"], ["Ada", "30"]])

    assert csv_getheader(str(csv_path)) == ["name", "age"]


def test_csv_getrow_returns_requested_row(tmp_path):
    print_test_result("csv_getrow", "returns the requested row", True)
    csv_path = tmp_path / "people.csv"
    csv_overwrite(str(csv_path), [["name", "age"], ["Ada", "30"]])

    assert csv_getrow(str(csv_path), 1) == ["Ada", "30"]


def test_csv_getcolumn_returns_column_values(tmp_path):
    print_test_result("csv_getcolumn", "returns the column values", True)
    csv_path = tmp_path / "people.csv"
    csv_overwrite(str(csv_path), [["name", "age"], ["Ada", "30"]])

    assert csv_getcolumn(str(csv_path), "age") == ["30"]


def test_csv_getdata_returns_specific_value(tmp_path):
    print_test_result("csv_getdata", "returns a specific CSV value", True)
    csv_path = tmp_path / "people.csv"
    csv_overwrite(str(csv_path), [["name", "age"], ["Ada", "30"]])

    assert csv_getdata(str(csv_path), 0, "age") == "30"


def test_csv_count_counts_rows(tmp_path):
    print_test_result("csv_count", "counts the rows in the CSV file", True)
    csv_path = tmp_path / "people.csv"
    csv_overwrite(str(csv_path), [["name", "age"], ["Ada", "30"]])

    assert csv_count(str(csv_path)) == 1
    assert csv_count(str(csv_path), withheader=True) == 2


def test_csv_append_adds_row(tmp_path):
    print_test_result("csv_append", "appends a new row", True)
    csv_path = tmp_path / "people.csv"
    csv_overwrite(str(csv_path), [["name", "age"], ["Ada", "30"]])

    csv_append(str(csv_path), ["Bob", "25"])

    assert csv_getrow(str(csv_path), 2) == ["Bob", "25"]


def test_csv_updaterow_updates_row(tmp_path):
    print_test_result("csv_updaterow", "updates a specific row", True)
    csv_path = tmp_path / "people.csv"
    csv_overwrite(str(csv_path), [["name", "age"], ["Ada", "30"]])

    csv_updaterow(str(csv_path), 1, ["Grace", "31"])

    assert csv_getrow(str(csv_path), 1) == ["Grace", "31"]
