
from ..debug_functions import check, fnf
import tarfile


def tar_extract(
    path:str=None,
    targetpath:str=None
):
    check(path, targetpath)
    fnf(path=path)
    
    with tarfile.open(path, "r") as tar:
        tar.extractall(targetpath)
    
