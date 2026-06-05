

from ..debug_functions import check
import csv

def csv_getheader(
        path:str=None,
        encoding:str="utf-8",
):
    check(path)

    with open(path, "r", encoding=encoding) as f:
        reader = csv.reader(f)
        header = next(reader)

        return header