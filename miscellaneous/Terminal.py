import os
import time
from attr import attrs

from termcolor import colored, cprint

def clear() -> None:
    """
    * Clear all the contents of the terminal.
    
    * Add support for Windows and Linux compatibility.
    """
    os.system("cls") if os.name == "nt" else os.system("clear")


def delay(time: int = 1) -> None:
    """Make the console sleep for a specified amount of time.

    Args:
        time (int, optional): Time until the console starts responding again. Defaults to 1.
    """
    time.sleep(time)


def info_message(message: str, is_bold: bool = False) -> None:
    cprint(message, attrs=["bold" if is_bold else ""], color="blue")
    

def error_message(message: str, is_bold: bool = False) -> None:
    cprint(message, attrs=["bold" if is_bold else ""], color="red")
    

def warn_message(message: str, is_bold: bool = False) -> None:
    cprint(message, attrs=["bold" if is_bold else ""], color="yellow")
    
