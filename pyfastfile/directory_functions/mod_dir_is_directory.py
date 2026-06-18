
from os.path import isdir
from ..debug_functions import check


def dir_is_directory(
    path:str=None,
):
    check(path)
    
    return isdir(path)


