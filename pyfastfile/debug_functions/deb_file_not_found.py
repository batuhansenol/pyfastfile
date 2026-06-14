
from .deb_parameter_check import parameter_check as check
from pathlib import Path

def exists(path: str = None):
    check(path)
    file = Path(path)
    return file.exists()

def fnf(path: str = None):
    check(path)
    if not exists(path=path):
        raise FileNotFoundError(f"File not found: {path}")