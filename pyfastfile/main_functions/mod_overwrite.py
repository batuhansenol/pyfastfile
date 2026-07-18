

from ..debug_functions import check, fnf

def overwrite(
        path:str=None,
        data:str=None,
        encoding:str="utf-8"
):  
    check(path, data)
    fnf(path)
      
    with open(path, "w", encoding=encoding) as f:
        f.write(data)