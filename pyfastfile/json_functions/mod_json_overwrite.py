

from ..debug_functions import check
import json


def json_overwrite(
        path:str=None,
        data:dict=None,
        encoding:str="utf-8"
):
    check(data, path)

    with open(path, "w", encoding=encoding) as jf:
        json.dump(data, jf)

