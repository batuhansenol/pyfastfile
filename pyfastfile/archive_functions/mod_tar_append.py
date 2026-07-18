
from ..debug_functions import check, fnf
import tarfile

def tar_append(
    zip_file:str=None,
    file:str=None
):
    check(zip_file, file)
    fnf(zip_file); fnf(file)
    
    with tarfile.open(zip_file, "a") as tar:
        tar.add(file)

