"""Tests for JSON helpers."""

from pyfastfile.json_functions.mod_json_append import json_append
from pyfastfile.json_functions.mod_json_delete_key import json_delete_key
from pyfastfile.json_functions.mod_json_get_keys import json_get_keys
from pyfastfile.json_functions.mod_json_get_values import json_get_values
from pyfastfile.json_functions.mod_json_is_valid import json_is_valid
from pyfastfile.json_functions.mod_json_overwrite import json_overwrite
from pyfastfile.json_functions.mod_json_read import json_read

from .conftest import print_test_result


def test_json_helpers(tmp_path):
    print_test_result("json_helpers", "handles the JSON lifecycle", True)
    json_path = tmp_path / "data.json"

    json_overwrite(str(json_path), {"a": 1})
    assert json_read(str(json_path))["a"] == 1
    assert json_is_valid(str(json_path)) is True

    json_append(str(json_path), {"b": 2})
    assert json_read(str(json_path))["b"] == 2
    assert list(json_get_keys(str(json_path))) == ["a", "b"]
    assert list(json_get_values(str(json_path), withlist=True)) == [1, 2]

    json_delete_key(str(json_path), "a")
    assert "a" not in json_read(str(json_path))
