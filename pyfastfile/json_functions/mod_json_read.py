
from ..debug_functions import check
import json 


def json_read(
        path:str=None,
):
    check(path)

    with open(path, "r") as jf:
        return json.load(jf)

