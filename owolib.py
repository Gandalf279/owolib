#!/home/cj/Documents/owolib/.venv/bin/python

# ---------------------------------------------------------------------------- #
#                OWOlib - Omnipresent Workflow Optimizer Library               #
# ---------------------------------------------------------------------------- #

import sys
import os
from dotenv import load_dotenv
import datetime as dt

load_dotenv()
DEFAULT_VERBOSITY = int(os.getenv("DEFAULT_VERBOSITY", "0"))
LOGFILE = os.getenv("DEFAULT_LOGFILE", "owolib.log")
#print(f"You are using OWOlib v{os.getenv("VERSION")}")

class Colors:
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    MAGENTA = "\033[95m"
    CYAN = "\033[96m"
    WHITE = "\033[97m"
    BLACK = "\033[30m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"
    REVERSED = "\033[7m"
    RESET = "\033[0m"


def ansiColors(fg: tuple[int, int, int], bg: tuple[int, int, int]) -> str:
    """"Takes two RGB values and returns an ANSI string."""
    fgr, fgg, fgb = fg
    bgr, bgg, bgb = bg

    return f"\033[38;2;{fgr};{fgg};{fgb}m\033[48;2;{bgr};{bgg};{bgb}m"


def printInfo(msg: str, vLevel=DEFAULT_VERBOSITY) -> str:
    """Print the given text if the verbosity level given is greater than or equal to 0."""
    if vLevel >= 0:
        print(f"{Colors.BLUE}INFO: {msg}{Colors.RESET}")
        return f"INFO: {msg}"
    return ""

def printFatal(msg: str, vLevel=DEFAULT_VERBOSITY, code=1) -> None:
    """Print the given text if the verbosity level given is equal to 0, then exit with the given error code."""
    if vLevel == 0:
        text = f"{Colors.RED}{Colors.UNDERLINE}{Colors.BOLD}    FATAL: {msg}    {Colors.RESET}"
        print(text)
        sys.exit(code)

def printError(msg: str, vLevel=DEFAULT_VERBOSITY) -> str:
    """Print the given text if the verbosity level given is greater than or equal to 1."""
    if vLevel >= 1:
        print(f"{Colors.RED}ERROR: {msg}{Colors.RESET}")
        return f"ERROR: {msg}"
    return ""

def printWarning(msg: str, vLevel=DEFAULT_VERBOSITY) -> str:
    """Print the given text if the verbosity level given is greater than or equal to 2."""
    if vLevel >= 2:
        print(f"{Colors.YELLOW}WARNING: {msg}{Colors.RESET}")
        return f"WARNING: {msg}"
    return ""


def printDebug(msg: str, vLevel=DEFAULT_VERBOSITY) -> str:
    """Print the given text if the verbosity level given is greater than or equal to 3."""
    if vLevel >= 3:
        print(f"{Colors.MAGENTA}DEBUG: {msg}{Colors.RESET}")
        return f"DEBUG: {msg}"
    return ""


def debugPause(debug: int) -> None:
    """Pause and wait for the user to press Enter to continue"""
    if debug:
        input(f"{Colors.MAGENTA}Press Enter to continue...{Colors.RESET}")

def getCurrentPath() -> str:
    return os.getcwd()

def log(text: str) -> str:
    """Log the text given into the file specified in the variable LOGFILE."""
    if LOGFILE == os.getenv("DEFAULT_LOGFILE", "owolib.log"):
        printWarning(f"Using default Logfile {os.getenv("DEFAULT_LOGFILE", "owolib.py")}\n Change the default in .env or use the variable LOGFILE to set a name for the file and disable this warning.")
    with open(LOGFILE, mode="a") as file:
        text = f"{dt.datetime.now().replace(microsecond=0)}: {text}\n"
        file.write(text)
        return text


