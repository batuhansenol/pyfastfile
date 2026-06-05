from .main_functions import overwrite
from .main_functions import append
from .main_functions import read
from .main_functions import readlines
from .main_functions import getline
from .main_functions import exists
from .main_functions import find
from .main_functions import find_num
from .main_functions import delete
from .main_functions import rename


from .utility_functions import destroynewline
from .utility_functions import limp

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

__all__ = [] 

# Main Functions 
 
__all__ += [
    "signature",
    "overwrite",
    "append",
    "read",
    "readlines",
    "getline",
    "exists",
    "find", 
    "find_num", 
    "delete", 
    "rename", ] 

# Utility Functions 
 
__all__ += [ 
    "destroynewline", 
    "limp" ]