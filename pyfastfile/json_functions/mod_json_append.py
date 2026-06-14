

from ..debug_functions import check
from .mod_json_read import json_read



def json_append(
        path:str=None,
        data:dict=None,
):
    check(path, data)

    jf_data = json_read(path=path)
    jf_data.update(data)
    






