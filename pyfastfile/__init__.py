
# Main Functions

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
from .main_functions import touch
from .main_functions import move

# Csv Functions

from .csv_functions import csv_getheader
from .csv_functions import csv_append
from .csv_functions import csv_read
from .csv_functions import csv_getcolumn
from .csv_functions import csv_getrow
from .csv_functions import csv_getdata
from .csv_functions import csv_overwrite
from .csv_functions import csv_count
from .csv_functions import csv_updaterow

# Utility Functions

from .utility_functions import destroynewline as destroy_newline
from .utility_functions import limp as lmap 
from .utility_functions import copy_to_clipboard

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
    "rename",
    "touch",
    "move"
] 

# Utility Functions 
 
__all__ += [ 
    "destroy_newline", 
    "lmap",
    "copy_to_clipboard" 
]

# Csv Functions

__all__ += [
    "csv_read",
    "csv_getheader",
    "csv_append",
    "csv_getrow",
    "csv_getcolumn",
    "csv_getdata",
    "csv_overwrite",
    "csv_count",
    "csv_updaterow"
]