

import csv

from .mod_csv_getrow import csv_getrow
from ..debug_functions import check

def csv_getdata(
        path:str=None,
        row:int=None,
        column:str=None,
        encoding:str="utf-8"
):
    check(path, row, column)

    with open(path, "r", encoding=encoding) as f:
        rows = list(csv.reader(f))

    header = rows[0]
    if row < 0:
        raise IndexError("Row index out of range")
    if row >= len(rows) - 1:
        raise IndexError("Row index out of range")
    row_data = rows[row + 1]
    return row_data[header.index(column)]

