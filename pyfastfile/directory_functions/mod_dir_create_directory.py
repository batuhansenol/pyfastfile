

from ..debug_functions import check
from ..main_functions import exists
from os import makedirs

def dir_create(
    path:str=None
):
    check(path)
    
    if exists(path=path):
        pass
    else:
        makedirs(path, exist_ok=True)

        
    
    
    

