

from ..debug_functions import check
import csv

def csv_getrow(
        path:str=None,
        row:int=None,
        encoding:str="utf-8"
):
    check(path, row)

    with open(path, "r", encoding=encoding) as f:
        file = list(csv.reader(f))

        return file[row]
    


