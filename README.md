# pyfastfile

A lightweight Python library for __easy-to-use__ operations.

## Installation

```bash
pip install pyfastfile
```

# Usage

## Main Functions

|Function Name|Description|Arguments|Returns|
|-------------|-----------|---------|-------|
|`overwrite()`|Overwrites a file with given content.|`path`:`str`, `data`:`str`,`encoding`:`str`|`None`|
|`append()`|Appends data to the end of a file.|`path`:`str`, `data`:`str`|`None`|
|`read()`|Reads entire file content as string.|`path`:`str`|`str`|
|`readlines()`|Returns file lines as a list.|`path`:`str`, `newline`:`bool`|`list`|
|`getline()`|Returns a specific line from file.|`path`:`str`, `line`:`int`,`newline`:`bool`|`str`|
|`exists()`|Checks if file exists.|`path`:`str`|`bool`|
|`find()`|Returns lines containing target text.|`path`:`str`,`data`:`str`|`list[str]`|
|`find_num()`|Returns line numbers matching target text.|`path`:`str`,`data`:str|`list[int]`|

## Utility Functions

|Function Name|Description|Arguments|Returns|
|-------------|-----------|---------|-------|
|`destroynewline()`|Removes newline characters from text.|`data`:`str`|`str`|


[Project Repo Github](https://github.com/batuhansenol/pyfastfile) • [Project Repo PyPI](https://pypi.org/project/pyfastfile/) 

[Author Github Profile](https://github.com/batuhansenol) • [Author PyPI Profile](https://pypi.org/user/Batuhan_Senol/)

*--Batuhan Şenol*