

from pathlib import Path
from .debug_functions import check

def exists(
        path:str=None,
):
    check(path)

    file = Path(path)

    if file.exists():
        return True
    else:
        return False
