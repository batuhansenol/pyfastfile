
from ..debug_functions import fnf, check

def read_bytes(
    path:str
):
    check(path)
    fnf(path)
    
    with open(path, "rb") as f:
        return f.read()

