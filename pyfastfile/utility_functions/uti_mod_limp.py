


from ..debug_functions import check

def limp(
        func:function=None,
        lst:list=None
):
    check(func, lst)

    return list(map(func, lst))


