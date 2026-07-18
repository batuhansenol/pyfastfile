


from ..debug_functions import check, fnf
import shutil as sh


def move(
        filepath:str=None,
        targetpath:str=None
):
    check(filepath, targetpath)
    fnf(filepath)

    sh.move(filepath, targetpath)