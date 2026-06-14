


from ..debug_functions import check
from .mod_overwrite import overwrite
from ..debug_functions import fnf

def clear(
        path:str=None,
        encoding:str="utf-8"
):
    check(path)

    fnf(path=path)
    
    overwrite(path=path, encoding=encoding, data="")



