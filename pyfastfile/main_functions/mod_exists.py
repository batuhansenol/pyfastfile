

from pathlib import Path
from .debug_functions import check

def exists(
        path:str=None,
):
    check(path)

    file = Path(path)

    return file.exists()
