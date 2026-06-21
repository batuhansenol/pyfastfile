
import tarfile
from ..debug_functions import check, fnf
from ..directory_functions import dir_is_directory as did

def tar_create(
    path:str=None,
    targetpath:str=None
):
    check(path, targetpath)
    
    if not did(path):
        raise ValueError("Path value must be directory.")
    
    with tarfile.open(targetpath, "w") as ta:
        ta.add(path)


