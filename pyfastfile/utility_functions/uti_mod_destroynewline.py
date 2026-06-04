

from debug_functions import check

def destroynewline(
        data:str=None
):
    
    check(data)

    return data.removesuffix("\n")
