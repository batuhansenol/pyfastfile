# pyfastfile

A lightweight Python library for simple and fast file operations.

## Installation

```bash
pip install pyfastfile
```

## Usage

```python
from pyfastfile import overwrite, append, read, readlines

overwrite("test.txt", "Hello")
append("test.txt", "World")
read("test.txt")
readlines("test.txt", newline=True)
```

--Batuhan Şenol