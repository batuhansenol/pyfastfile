
from ..debug_functions import fnf, check 
from ..main_functions import size
from .mod_dir_list_directory import dir_list
from .mod_dir_is_directory import dir_is_directory

def dir_size(path: str = None):
    check(path)
    fnf(path)
    if not dir_is_directory(path):
        raise FileExistsError("This is not directory.")
    
    size_byte = 0
    for i in dir_list(path):
        full_path = fr"{path}/{i}"
        if dir_is_directory(full_path):
            size_byte += dir_size(full_path)  
        else:
            size_byte += size(path=full_path)
    
    return size_byte



