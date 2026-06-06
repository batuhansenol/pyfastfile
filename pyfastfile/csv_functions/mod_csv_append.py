

from ..debug_functions import check
import csv

def csv_append(
        path:str=None,
        data:list=None,
        encoding:str="utf-8"
):
    check(path, data)

    with open(path, "a", newline="", encoding=encoding) as f:
        writer = csv.writer(f)
        
        if isinstance(data[0], (list, tuple)):
            writer.writerows(data)
        else:
            writer.writerow(data)


