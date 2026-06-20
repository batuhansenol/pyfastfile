
from ..debug_functions import check
from ..encryption_functions.module_wrapper.aes_wrapper import GCMEncryptor

def decrypt_bytes(
    data:bytes=None,
    key:bytes=None
):
    check(data, key)
    
    cipher = GCMEncryptor(key=key)
    
    return cipher.decrypt_bytes(data)
    

