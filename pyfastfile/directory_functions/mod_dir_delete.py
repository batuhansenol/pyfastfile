
from os import rmdir
from .mod_dir_is_empty import dir_is_empty
from ..debug_functions import check
from shutil import rmtree


def dir_delete(
    path:str=None
):
    check(path)
    
    if dir_is_empty(path=path) == 0:
        rmdir(path)
    else:
        rmtree(path)

