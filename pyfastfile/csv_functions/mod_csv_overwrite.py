

from .mod_csv_append import csv_append
from ..debug_functions import check
import csv

def csv_overwrite(
        path:str=None,
        data:list=None,
        encoding:str="utf-8"
):
    check(path, data)

    with open(path, "w", newline="", encoding=encoding) as f:
        writer = csv.writer(f)
        writer.writerows(data)