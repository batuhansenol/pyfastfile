

import csv
from ..debug_functions import check


def csv_read(
        path:str=None,
        encoding:str="utf-8",
):
    check(path)

    with open(path, "r", encoding=encoding) as f:
        for row in csv.reader(f):
            yield row
