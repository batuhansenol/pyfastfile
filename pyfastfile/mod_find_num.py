

from .debug_functions import check


def find_num(
        path:str=None,
        encoding:str="utf-8",
        data:str=None
):
    
    check(path, data)

    lines = []
    with open(path, "r", encoding=encoding) as f:

        for i, line in enumerate(f):
            if data in line:
                lines.append(i)
    
    return lines