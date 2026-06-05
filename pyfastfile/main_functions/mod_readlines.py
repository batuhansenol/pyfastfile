

from ..debug_functions import check

def readlines(
        path:str=None,
        encoding:str="utf-8",
        newline:bool=True
):
    
    check(path)

    with open(path, "r", encoding=encoding) as f:
        
        lines = f.readlines()

        if not newline:
            lines = [line.removesuffix("\n") for line in lines]

    return lines
    
