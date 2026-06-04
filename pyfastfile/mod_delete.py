

from debug_functions import check
from pathlib import Path

def delete(
        path:str=None
):
    check(path)
    
    file = Path(path)
    

    if file.exists():
        file.unlink()
