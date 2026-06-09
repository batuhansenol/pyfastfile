


from ..debug_functions import check
import shutil as sh


def move(
        filepath:str=None,
        targetpath:str=None
):
    check(filepath, targetpath)

    sh.move(filepath, targetpath)