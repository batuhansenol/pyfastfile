
from .mod_dir_list_directory import dir_list
from ..debug_functions import check, fnf

def dir_is_empty(
    path:str=None
):
    check(path)
    fnf(path)
    
    if (len(dir_list(path))) == 0:
        return True
    else:
        False



