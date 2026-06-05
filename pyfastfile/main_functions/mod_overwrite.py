

from ..debug_functions import check

def overwrite(
        path:str=None,
        data:str=None,
        encoding:str="utf-8"
):
    
    check(path, data)

    with open(path, "w", encoding=encoding) as f:
        f.write(data)