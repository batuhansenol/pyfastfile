
import os
from ..debug_functions import check
from ..debug_functions import fnf

def size(
        path:str=None
):
    check(path)

    fnf(path)

    return os.path.getsize(path)

