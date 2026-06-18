

from .mod_dir_size_directory import dir_size


def dir_size_mb(
    path:str=None
):
    return dir_size(path=path) / (1024 * 1024)