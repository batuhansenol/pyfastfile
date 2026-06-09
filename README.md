
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