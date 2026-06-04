from .main_functions import __all__ as _main
from .utility_functions import __all__ as _utility

from importlib.metadata import version

try:
    __version__ = version("pyfastfile")
except Exception:
    __version__ = "0.0.0"

def signature(show=False):
    data = (
        f"pyfastfile v{__version__}\n"
        "Experimental Toolkit\n"
        "Author: Batuhan Şenol"
    )

    if show:
        print(data)

    return data

__all__ = _main + _utility + ["signature"]