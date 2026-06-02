

def overwrite(
        path:str=None,
        data:str=None,
        encoding:str="utf-8"
):
    with open(path, "w", encoding=encoding) as f:
        f.write(data)