


from ..debug_functions import check
import csv

def csv_getcolumn(
        path:str=None,
        column:str=None,
        encoding:str="utf-8",
):
    check(path, column)
    
    column_data = []

    with open(path, "r", encoding=encoding) as f:
        reader = csv.DictReader(f)

        for row in reader:
            column_data.append(row[column])

        return column_data