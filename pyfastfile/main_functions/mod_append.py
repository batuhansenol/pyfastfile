
from .debug_functions import check

def append(
        path:str=None,
        data:str=None,
        newline:bool=True,
        encoding:str="utf-8" 
        ):
    
    check(path, data)

    with open(path, "a", encoding=encoding) as f:
        if newline:
            f.write(data+"\n")
        else:
            f.write(data)

