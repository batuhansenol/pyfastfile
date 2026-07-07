
from ..debug_functions import check, fnf
import os
import zipfile


def zip_append(
    path:str=None,
    target:str=None
):
    check(path, target); fnf(path)

    with zipfile.ZipFile(path, "a") as zip:
        zip.write(target, arcname=os.path.basename(target))
