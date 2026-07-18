
from ..debug_functions import check, fnf

def append(
        path:str=None,
        data:str=None,
        newline:bool=True,
        encoding:str="utf-8" 
        ):
    
    check(path, data)
    fnf(path)

    with open(path, "a", encoding=encoding) as f:
        if newline:
            f.write(data+"\n")
        else:
            f.write(data)

