
from ..debug_functions import check, fnf
import tarfile

def tar_append(
    path:str=None,
    target:str=None
):
    check(path, target)
    fnf(path); fnf(target)
    
    with tarfile.open(path, "a") as tar:
        tar.add(target)

