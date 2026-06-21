
from ..debug_functions import check, fnf
import tarfile 


def tar_list(
    path:str=None
):
    check(path)
    fnf(path)
    
    with tarfile.open(path, "r") as tar:
        return tar.getnames() 

