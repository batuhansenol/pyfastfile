

from pathlib import Path

def exists(
        path:str=None,
):
    file = Path(path)

    if file.exists():
        return True
    else:
        return False
