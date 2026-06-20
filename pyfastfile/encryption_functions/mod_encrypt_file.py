
from .module_wrapper import encrypt_file as enc
from ..debug_functions import check, fnf

def enc_encrypt_file(
    path:str=None,
    targetpath:str=None,
    key:bytes=None,
    mode:str="gcm"
):
    check(path, targetpath, key)
    fnf(path)
    
    enc(src_path=path, dst_path=targetpath, key=key, mode=mode)
    
    
    

