

from ..debug_functions import check
from .mod_csv_read import csv_read

def csv_count(
        path:str=None,
        withheader:bool=False
):
    check(path)

    file = csv_read(path=path)

    if not withheader:
        next(file)

    n = 0

    for _ in file:
        n+=1

    return n

