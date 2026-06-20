
# pyfastfile


A lightweight Python library for __easy-to-use__ operations.

----

![logo](logo.png)

![python](https://img.shields.io/badge/Python-3.10+-blue.svg?logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-Apache%202.0-green)
![Status](https://img.shields.io/badge/Status-Active-success)
![Type](https://img.shields.io/badge/API-File%20Operations-informational)
![Github]( https://img.shields.io/badge/github-repo-blue?logo=github)
<img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" width="20"/>

## Installation

```bash
pip install pyfastfile
```

# Usage

The `encoding` parameter defaults to **`utf-8`** in all functions that support text encoding. \
All index-based functions use **zero-based indexing**.


# Titles

- [**Main Functions**](#main-functions)
- [**Csv Functions**](#csv-functions)
- [**Json Functions**](#json-functions)
- [**Directory Functions**](#directory-functions)
- [**Archive Functions**](#archive-functions)
- [**Utility Functions**](#utility-functions)



---

## Main Functions

|Function Name|Description|Arguments|Returns|
|-------------|-----------|---------|-------|
|`overwrite()`|Overwrites a file with given content.|`path`:`str`, `data`:`str`,`encoding`:`str`|`None`|
|`append()`|Appends data to the end of a file.|`path`:`str`, `data`:`str`,`encoding`:`str`|`None`|
|`read()`|Reads entire file content as string.|`path`:`str`,`encoding`:`str`|`str`|
|`readlines()`|Returns file lines as a list.|`path`:`str`, `newline`:`bool`,`encoding`:`str`|`list`|
|`getline()`|Returns a specific line from file.|`path`:`str`, `line`:`int`,`newline`:`bool`,`encoding`:`str`|`str`|
|`exists()`|Checks if file exists.|`path`:`str`|`bool`|
|`find()`|Returns lines containing target text.|`path`:`str`,`data`:`str`,`encoding`:`str`|`list[str]`|
|`find_num()`|Returns line numbers matching target text.|`path`:`str`,`data`:`str`,`encoding`:`str`|`list[int]`|
|`delete()`|Delete target file.|`path`:`str`|`None`|
|`rename()`|Rename target file.|`path`:`str`, `name`:`str`|`None`|
|`touch()`|Create file.|`path`:`str`,`existserror`:`bool`|`None`|
|`move()`|Move files|`filepath`:`str`,`targetpath`:`str`|`None`|
| `clear()` | Clears the content of a file by overwriting it with an empty string. | `path: str`, `encoding: str = "utf-8"` | `None` |
| `count_lines()` | Returns the number of lines in a file. | `path`: `str` | `int` |
| `size_mb()` | Returns file size in megabytes. | `path`:`str` | `float` |
| `size()` | Returns file size in bytes. | `path`:`str` | `int` |

## Csv Functions

|Function Name|Description|Arguments|Returns|
|-------------|-----------|---------|-------|
|`csv_read()`|Read target csv.|`path`:`str`,`encoding`:`str`|`Generator`|
|`csv_append()`|Appends data to the end of a csv file.| `path`:`str`,`data`:`list`,`encoding`:`str`| `None`|
|`csv_getheader()`|Return header of the target csv file.|`path`:`str`,`encoding`:`str`|`list`|
|`csv_getrow()`|Return target row of the csv file.| `path`:`str`,`row`:`int`,`encoding`:`str`|`list`|
|`csv_getcolumn()`|Return target column of the csv file.|`path`:`str`,`column`:`str`,`encoding`:`str`|`list`|
|`csv_getdata()`|Gets a value from CSV by row and column.|`path`:`str`,`row`:`int`,`column`:`str`,`encoding`:`str`,|`any`|
|`csv_updaterow()`|Update target row|`path`:`str`,`row`:`int`,`new_data`:`list`,`encoding`:`str`|`None`|
|`csv_overwrite()`|Overwrite on target file.|`path`:`str`,`data`:`list`,`encoding`:`str`|`None`|
|`csv_count()`|Return lenght of target file.|`path`:`str`,`withheader`:`bool`| `int`|



## Json Functions

| Function Name| Description| Arguments|Returns|
| ------ | ----- | ----- | ----- |
| `json_read()`       | Read target JSON file and parse its content.| `path`:`str`| `dict` |
| `json_overwrite()`  | Overwrite target JSON file with new data.| `path`:`str`, `data`:`dict`, `encoding`:`str` | `None`|
| `json_append()`     | Reads JSON file, merges new dictionary into existing data (key update behavior). | `path`:`str`, `data`:`dict`| `None`|
| `json_delete_key()` | Deletes a specific key from JSON data and rewrites the file.| `path`:`str`, `key`:`str`, `encoding`:`str`| `None`|
| `json_is_valid()`| Checks whether the target JSON file contains valid JSON data. | `path`:`str`|`bool`|
| `json_get_values()` | Returns all values from the target JSON object.| `path`:`str`, `withlist`:`bool`, `encoding`:`str` | `dict_values` | `list` |
|`json_get_keys()`| Returns all keys from the target JSON object.|`path`:`str`, `withlist`:`bool`, `encoding`:`str`|`dict_keys`|`list`|


## Directory Functions
| Function Name| Description| Arguments|Returns|
| ------ | ----- | ----- | ----- |
| `dir_create()`| Creates the target directory if it does not already exist.| `path`:`str`| `None`|
| `dir_list()`| Lists all entries in the target directory.| `path`:`str`| `list`|
| `dir_is_directory()`| Checks whether the target path is a directory.| `path`:`str`| `bool`|
| `dir_delete()`| Deletes the target directory. Removes recursively if non-empty.| `path`:`str`| `None`|
| `dir_is_empty()`| Checks whether the target directory is empty.| `path`:`str`| `bool`|
| `dir_size()`| Returns the total size of the target directory in bytes, recursively.| `path`:`str`| `int`|
| `dir_size_mb()`| Returns the total size of the target directory in megabytes, recursively.| `path`:`str`| `float`|


## Archive Functions
|Function Name|Description|Arguments|Returns|
|-------------|-----------|---------|-------|
|`zip_create()`|Creates a zip archive from file or directory.|`path`:`str`, `targetpath`:`str`|`None`|
|`zip_extract()`|Extracts a zip archive to target path.|`path`:`str`, `targetpath`:`str`|`None`|
|`zip_is_zipfile()`|Checks if file is a valid zip archive.|`path`:`str`|`bool`|
|`zip_list()`|Returns list of files inside zip archive.|`path`:`str`|`list`|

## Utility Functions

|Function Name|Description|Arguments|Returns|
|-------------|-----------|---------|-------|
|`destroy_newline()`|Removes newline characters from text.|`data`:`str`|`str`|
|`lmap()`|Only: list(map(...))|`func`:`function`,`lst`:`list`|`list`|
|`copy_to_clipboard()`|Copy text on clipboard|`text`:`str`|`None`|

---

[Project Repo Github](https://github.com/batuhansenol/pyfastfile) • [Project Repo PyPI](https://pypi.org/project/pyfastfile/) --
[Author Github Profile](https://github.com/batuhansenol) • [Author PyPI Profile](https://pypi.org/user/Batuhan_Senol/)

*--Batuhan Şenol*