


def find(
        path:str=None,
        encoding:str="utf-8",
        data:str=None
):
    lines = []

    with open(path, "r", encoding=encoding) as f:
        for line in f:
            if data in line:
                lines.append(f)
    
    return lines