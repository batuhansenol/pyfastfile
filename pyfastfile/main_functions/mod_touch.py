

from ..debug_functions import check
from .mod_exists import exists

def touch(
        path:str=None,
        existserror:bool=True
):
    check(path)

    if existserror:
        with open(path, "x"):
            pass
    else:
        if exists(path):
            pass
        else:
            with open(path, "w"):
                pass
