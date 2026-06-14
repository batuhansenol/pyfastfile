

from .deb_parameter_check import parameter_check as check
from ..main_functions import exists

def fnf(
        path:str=None,
):
    check(path)

    if not(exists(path=path)):
        raise FileNotFoundError(f"File not found: {path}")
    

