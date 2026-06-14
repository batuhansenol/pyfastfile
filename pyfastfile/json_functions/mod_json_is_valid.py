


from ..debug_functions import check
from .mod_json_read import json_read
import json

def json_is_valid(
        path:str=None,
):  
    check(path)

    try:
        json_read(path=path)
        return True
    except json.JSONDecodeError:
        return False
    

