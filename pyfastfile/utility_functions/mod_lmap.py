


from ..debug_functions import check
from typing import Callable

def limp(
    func: Callable = None,
    lst: list = None
) -> list:
    check(func, lst)
    return list(map(func, lst))
