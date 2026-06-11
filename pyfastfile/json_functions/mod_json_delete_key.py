
from ..debug_functions import check
from .mod_json_read import json_read
from .mod_json_overwrite import json_overwrite


def json_delete_key(
        path:str=None,
        key:str=None,
        encoding:str="utf-8"
):
    check(path, key)

    data = json_read(path=path)

    if key in data:
        del data[key]

    json_overwrite(path=path, data=data, encoding=encoding)






