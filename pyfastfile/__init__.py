
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
from .main_functions import clear
from .main_functions import count_lines
from .main_functions import size_mb
from .main_functions import size

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

# json Functions

from .json_functions import json_append
from .json_functions import json_overwrite
from .json_functions import json_delete_key
from .json_functions import json_read
from .json_functions import json_get_keys
from .json_functions import json_get_values
from .json_functions import json_is_valid

# Directory Functions

from .directory_functions import dir_create
from .directory_functions import dir_is_empty
from .directory_functions import dir_delete
from .directory_functions import dir_is_directory
from .directory_functions import dir_list
from .directory_functions import dir_size
from .directory_functions import dir_size_mb


# __init__.py imports

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
    "move",
    "size",
    "size_mb",
    "count_lines",
    "clear"
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


# Json Functions

__all__ += [
    "json_append",
    "json_overwrite",
    "json_delete_key",
    "json_read",
    "json_get_values",
    "json_get_keys",
    "json_is_valid"
]

# Directory Functions

__all__ += [
    "dir_create",
    "dir_list",
    "dir_size",
    "dir_size_mb",
    "dir_is_empty",
    "dir_delete",
    "dir_is_directory"
]