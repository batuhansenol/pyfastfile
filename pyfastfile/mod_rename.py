

from .debug_functions import check
from pathlib import Path

def rename(
        path:str=None,
        name:str=None
):
    check(name, path)

    file = Path(path)
    file.rename(name)