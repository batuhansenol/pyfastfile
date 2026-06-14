

from .mod_readlines import readlines
from ..debug_functions import check
from ..debug_functions import fnf

def count_lines(
        path:str=None
):
    check(path)

    fnf(path=path)

    return len(readlines(path=path))


