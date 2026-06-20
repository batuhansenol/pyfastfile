
import zipfile as zip
from ..debug_functions import check, fnf
from ..directory_functions import dir_is_directory
import os

def zip_create(
    path:str=None,
    targetpath:str=None
):
    check(path, targetpath)
    fnf(path)
    
    if dir_is_directory(path):
  
        with zip.ZipFile(targetpath, "w", zip.ZIP_DEFLATED) as zf:  
            for root, _, files in os.walk(path):
                for file in files:
                    fullway = os.path.join(root, file)
                    arch_path = os.path.relpath(fullway, path)
                    zf.write(fullway, arch_path)
                    
    else:
         
        with zip.ZipFile(targetpath, "w", zip.ZIP_DEFLATED) as zf:
            zf.write(path, os.path.basename(path))


