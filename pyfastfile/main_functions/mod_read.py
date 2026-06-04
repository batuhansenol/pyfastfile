

from .debug_functions import check

def read(
        path:str=None,
        encoding:str="utf-8"
):
    
    check(path)

    with open(path, "r", encoding=encoding) as f:
        return f.read()