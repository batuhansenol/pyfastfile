
from ..debug_functions import check, fnf
import os
import zipfile


def zip_append(
    zip_file:str=None,
    file:str=None
):
    check(zip_file, file); fnf(zip_file)

    with zipfile.ZipFile(zip_file, "a") as zip:
        zip.write(file, arcname=os.path.basename(file))
