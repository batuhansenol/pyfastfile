

from ..debug_functions import fnf, check
from os import listdir


def dir_list(
    path:str=None
):
    check(path)
    fnf(path)
    
    return listdir(path)



