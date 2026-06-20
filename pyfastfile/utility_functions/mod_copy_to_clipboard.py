
from ..debug_functions import check
import subprocess
import sys

def copy_to_clipboard(text: str = None) -> None:
    
    check(text)


    if sys.platform == "win32":
        subprocess.run("clip", input=text.encode("utf-16"), check=True)
    elif sys.platform == "darwin":
        subprocess.run("pbcopy", input=text.encode("utf-8"), check=True)
    else:
        encoded = text.encode("utf-8")
        commands = [
            ["wl-copy"],                          
            ["xclip", "-selection", "clipboard"], 
            ["xsel", "--clipboard", "--input"],   
        ]
        for cmd in commands:
            try:
                subprocess.run(cmd, input=encoded, check=True)
                return
            except FileNotFoundError:
                continue
        raise RuntimeError("No clipboard tool found (install xclip, xsel, or wl-clipboard)")

