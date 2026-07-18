
from ..debug_functions import check, fnf

def getline(
        path:str=None,
        line:int=0,
        encoding:str="utf-8",
        newline:bool=True
):
    
    check(path)
    fnf(path)

    with open(path, "r", encoding=encoding) as f:
        lines = f.readlines()

    if  not newline:
        lines = [line.removesuffix("\n") for line in lines]


    return lines[line]