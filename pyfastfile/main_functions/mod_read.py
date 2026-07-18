

from ..debug_functions import check, fnf

def read(
        path:str=None,
        encoding:str="utf-8"
):
    fnf(path)
    check(path)

    with open(path, "r", encoding=encoding) as f:
        return f.read()