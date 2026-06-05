
![logo](logo.png)

A lightweight Python library for __easy-to-use__ operations. \
 \
![python](https://img.shields.io/badge/Python-3.10+-blue.svg?logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-Apache%202.0-green)
![Version](https://img.shields.io/badge/Version-0.1.7post4-orange)
![Status](https://img.shields.io/badge/Status-Active-success)
![Type](https://img.shields.io/badge/API-File%20Operations-informational)

## Installation

```bash
pip install pyfastfile
```

# Usage

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

## Utility Functions

|Function Name|Description|Arguments|Returns|
|-------------|-----------|---------|-------|
|`destroynewline()`|Removes newline characters from text.|`data`:`str`|`str`|
|`limp()`|Only: list(map(...))|`func`:`function`,`lst`:`list`|`list`|

[Project Repo Github](https://github.com/batuhansenol/pyfastfile) • [Project Repo PyPI](https://pypi.org/project/pyfastfile/) 

[Author Github Profile](https://github.com/batuhansenol) • [Author PyPI Profile](https://pypi.org/user/Batuhan_Senol/)

*--Batuhan Şenol*