
from .mod_zip_is_zipfile import zip_is_zipfile
from ..debug_functions import check, fnf
import zipfile as zip


def zip_list(
    path:str=None
):
    check(path)
    fnf(path)
    
    if not zip_is_zipfile(path):
        raise ValueError(f"{path} is not a valid zip file.")
    
    with zip.ZipFile(path, "r") as zf:
        return zf.namelist()
    

    
    
    
    


