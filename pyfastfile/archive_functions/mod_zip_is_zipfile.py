
import zipfile as zip
from ..debug_functions import check, fnf

def zip_is_zipfile(
    path:str=None
):
    check(path)
    fnf(path)
    
    return zip.is_zipfile(path)

