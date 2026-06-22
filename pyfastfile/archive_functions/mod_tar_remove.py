import tarfile
import os

from ..debug_functions import check, fnf


def tar_remove(path: str = None, target: str = None):
    check(path, target)
    fnf(path)

    temp_path = path + ".tmp"

    with tarfile.open(path, "r") as tarold:
        with tarfile.open(temp_path, "w") as tarnew:
            for member in tarold.getmembers():
                if member.name == target:
                    continue

                fileobj = tarold.extractfile(member)

                if fileobj is not None:
                    tarnew.addfile(member, fileobj)
                else:
                    tarnew.addfile(member)

    os.replace(temp_path, path)