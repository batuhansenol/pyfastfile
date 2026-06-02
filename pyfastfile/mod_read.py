

def read(
        path:str=None,
        encoding:str="utf-8"
):
    with open(path, "r", encoding=encoding) as f:
        return f.read()