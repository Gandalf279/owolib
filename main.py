#!/home/cj/Documents/owolib/.venv/bin/python
import owolib

owolib.LOGFILE = "test.log"

owolib.printError(owolib.LOGFILE)

print(f"{owolib.ansiColors((255, 0, 0), (0, 255, 255))}Hi!{owolib.Colors.RESET}")