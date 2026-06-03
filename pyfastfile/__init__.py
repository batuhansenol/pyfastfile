from .mod_overwrite import overwrite
from .mod_append import append
from .mod_read import read
from .mod_readlines import readlines
from .mod_getline import getline
from .mod_exists import exists
from .mod_find import find
from .mod_find_num import find_num


from .utility_functions import destroynewline

from importlib.metadata import version

try:
    __version__ = version("pyfastfile")
except Exception:
    __version__ = "0.0.0"

def signature(show=False):
    data = (
        f"pyfastfile v{__version__}\n"
        "Experimental Toolkit\n"
        "Author: Batuhan Şenol"
    )

    if show:
        print(data)

    return data

__all__ = [
    "signature",
    "overwrite",
    "append",
    "read",
    "readlines",
    "getline",
    "exists",
    "find",
    "find_num",
    


    "destroynewline"
]