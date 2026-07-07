


from .mod_csv_read import csv_read
from .mod_csv_append import csv_append
from ..debug_functions import check

def csv_updaterow(
        path: str = None, 
        row: int = None, 
        new_data: list = None,
        encoding:str="utf-8"):
    
    check(path, row, new_data)

    rows = list(csv_read(path))

    if row < 0 or row >= len(rows):
        raise IndexError("Row index out of range")

    rows[row] = new_data


    open(path, "w").close()


    for r in rows:
        csv_append(path=path, data=r, encoding=encoding)