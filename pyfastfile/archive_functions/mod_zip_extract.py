

import zipfile as zip

from .mod_zip_is_zipfile import zip_is_zipfile
from ..debug_functions import fnf, check


def zip_extract(
    path:str=None,
    targetpath:str=None
):
    check(path, targetpath)
    fnf(path)
    
    if not zip_is_zipfile(path):
        raise ValueError(f"{path} is not a valid zip file.")
    
    with zip.ZipFile(path, "r") as zf:
        zf.extractall(targetpath)
        
        
    

