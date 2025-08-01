import sys

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

global verbosityLevel
verbosityLevel = 0
global debugMode
debugMode = False

def printInfo(msg, vLevel=verbosityLevel) -> str:
    if vLevel >= 3:
        msg = f"{Colors.BLUE}INFO: {msg}{Colors.RESET}"
        print(msg)
        return msg
    return ""
        

def printDebug(msg, vLevel=verbosityLevel) -> str:
    if vLevel >= 2:
        msg = f"{Colors.YELLOW}DEBUG: {msg}{Colors.RESET}"
        print(msg)
        return msg
    return ""

def printError(msg, vLevel=verbosityLevel) -> str:
    if vLevel >= 1:
        msg = f"{Colors.RED}ERROR: {msg}{Colors.RESET}"
        print(msg)
        return msg
    return ""

def printFatal(msg, vLevel=verbosityLevel, code=1) -> None:
    if vLevel >= 4:
        msg = f"{Colors.RED}{Colors.UNDERLINE}{Colors.BOLD}    FATAL: {msg}    {Colors.RESET}"
        print(msg)
        sys.exit(code)

def debugPause(debug=debugMode) -> str:
    if debug:
        input(f"{Colors.MAGENTA}Press Enter to continue...{Colors.RESET}")
        return "-"*10 + "PAUSED" + "-"*10
    return ""