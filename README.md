# pyfastfile

A lightweight Python library for __easy-to-use__ operations.

## Installation

```bash
pip install pyfastfile
```

## Usage

```python
import pyfastfile as pf

# === Main Functions

pf.overwrite("test.txt", "Hello")
pf.append("test.txt", "World")
pf.read("test.txt")
pf.readlines("test.txt", newline=True)
pf.getline("test.txt", line=0, newline=True)
pf.exists("test.txt")
pf.find("test.txt", "testdata")
pf.find_num("test.txt", "testdata") # Return Index

# === Utility Functions ===

pf.destroynewline("test")

```
## Optional 
```py
    encoding="utf-8"
```

[Project Repo Github](https://github.com/batuhansenol/pyfastfile) • [Project Repo PyPI](https://pypi.org/project/pyfastfile/) 

[Author Github Profile](https://github.com/batuhansenol) • [Author PyPI Profile](https://pypi.org/user/Batuhan_Senol/)

*--Batuhan Şenol*