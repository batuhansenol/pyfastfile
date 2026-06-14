



import os
from ..debug_functions import check
from ..debug_functions import fnf

def size_mb(
        path:str=None
):
    check(path)

    fnf(path)

    return ((os.path.getsize(path) / 1024) / 1024)
