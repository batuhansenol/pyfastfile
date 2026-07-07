
from ..debug_functions import check
from .mod_json_read import json_read

def json_get_values(
        path:str=None,
        withlist:bool=False,
        encoding:str="utf-8"
):
    check(path)

    file = json_read(path=path)

    if withlist:
        return list(file.values())
    else:
        return file.values()

