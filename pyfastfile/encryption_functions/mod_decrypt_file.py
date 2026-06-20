

from .module_wrapper import decrypt_file as denc
from ..debug_functions import fnf, check

def enc_decrypt_file(
    path:str=None,
    targetpath:str=None,
    key:bytes=None,
    mode:str="gcm"
):
    check(path, targetpath, key)
    fnf(path)
    
    denc(src_path=path, dst_path=targetpath, key=key, mode=mode)