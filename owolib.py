#!/home/cj/Documents/owolib/.venv/bin/python
# ---------------------------------------------------------------------------- #
#                OWOlib - Omnipresent Workflow Optimizer Library               #
# ---------------------------------------------------------------------------- #

import sys
import os
from dotenv import load_dotenv

LOGFILE = "default.log"

load_dotenv()
DEFAULT_VERBOSITY = int(os.getenv("DEFAULT_VERBOSITY", "0"))
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
    fgr, fgg, fgb = fg
    bgr, bgg, bgb = bg


    return f"\033[38;2;{fgr};{fgg};{fgb}m\033[48;2;{bgr};{bgg};{bgb}m"


def printFatal(msg: str, vLevel=DEFAULT_VERBOSITY, code=1) -> None:
    """Print the given text if the verbosity level given is equal to 0, then exit with the given error code."""
    if vLevel == 0:
        msg = f"{Colors.RED}{Colors.UNDERLINE}{Colors.BOLD}    FATAL: {msg}    {Colors.RESET}"
        print(msg)
        sys.exit(code)

def printError(msg: str, vLevel=DEFAULT_VERBOSITY) -> str:
    """Print the given text if the verbosity level given is greater than or equal to 1."""
    if vLevel >= 1:
        msg = f"{Colors.RED}ERROR: {msg}{Colors.RESET}"
        print(msg)
        return msg
    return ""

def printDebug(msg: str, vLevel=DEFAULT_VERBOSITY) -> str:
    """Print the given text if the verbosity level given is greater than or equal to 2."""
    if vLevel >= 2:
        msg = f"{Colors.YELLOW}DEBUG: {msg}{Colors.RESET}"
        print(msg)
        return msg
    return ""

def printInfo(msg: str, vLevel=DEFAULT_VERBOSITY) -> str:
    """Print the given text if the verbosity level given is greater than or equal to 3."""
    if vLevel >= 3:
        msg = f"{Colors.BLUE}INFO: {msg}{Colors.RESET}"
        print(msg)
        return msg
    return ""

def debugPause(debug: int) -> None:
    """Pause and wait for the user to press Enter to continue"""
    if debug:
        input(f"{Colors.MAGENTA}Press Enter to continue...{Colors.RESET}")

def getCurrentPath() -> str:
    return os.getcwd()

