

from .mod_csv_getrow import csv_getrow
from ..debug_functions import check

def csv_getdata(
        path:str=None,
        row:int=None,
        column:str=None,
        encoding:str="utf-8"
):
    check(path, row, column)

    row_data = csv_getrow(path=path, row=row, encoding=encoding)

    return row_data[column]

