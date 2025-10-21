from unittest.mock import patch
import datetime as dt
import owolib as owo
import pytest
import os

def testPrintInfo():
    assert owo.printInfo("Hello Info", 0) == ""
    assert owo.printInfo("Hello Info", 1) == ""
    assert owo.printInfo("Hello Info", 2) == ""
    assert owo.printInfo("Hello Info", 3) == ""
    assert owo.printInfo("Hello Info", 4) == "INFO: Hello Info"
    assert owo.printInfo("Hello Info", 5) == "INFO: Hello Info"
    assert owo.printInfo("Hello Info", 621) == "INFO: Hello Info"

def testPrintDebug():
    assert owo.printDebug("Hello Debug", 0) == ""
    assert owo.printDebug("Hello Debug", 1) == ""
    assert owo.printDebug("Hello Debug", 2) == ""
    assert owo.printDebug("Hello Debug", 3) == "DEBUG: Hello Debug"
    assert owo.printDebug("Hello Debug", 4) == "DEBUG: Hello Debug"
    assert owo.printDebug("Hello Debug", 5) == "DEBUG: Hello Debug"
    assert owo.printDebug("Hello Debug", 621) == "DEBUG: Hello Debug"

def testPrintWarning():
    assert owo.printWarning("Hello Warning", 0) == ""
    assert owo.printWarning("Hello Warning", 1) == ""
    assert owo.printWarning("Hello Warning", 2) == "WARNING: Hello Warning"
    assert owo.printWarning("Hello Warning", 3) == "WARNING: Hello Warning"
    assert owo.printWarning("Hello Warning", 4) == "WARNING: Hello Warning"
    assert owo.printWarning("Hello Warning", 5) == "WARNING: Hello Warning"
    assert owo.printWarning("Hello Warning", 621) == "WARNING: Hello Warning"

def testPrintError():
    assert owo.printError("Hello Error", 0) == ""
    assert owo.printError("Hello Error", 1) == "ERROR: Hello Error"
    assert owo.printError("Hello Error", 2) == "ERROR: Hello Error"
    assert owo.printError("Hello Error", 3) == "ERROR: Hello Error"
    assert owo.printError("Hello Error", 4) == "ERROR: Hello Error"
    assert owo.printError("Hello Error", 5) == "ERROR: Hello Error"
    assert owo.printError("Hello Error", 621) == "ERROR: Hello Error"

def testGetCwd():
    assert owo.getCurrentPath() == os.getcwd()

def testAnsiColors():
    assert owo.ansiColors(fg=(0, 0, 0), bg=(255, 255, 255)) == "\033[38;2;0;0;0m\033[48;2;255;255;255m"
    with pytest.raises(ValueError):
        assert owo.ansiColors(fg=(0, 0), bg=(255, 255, 255)) == "\033[38;2;0;0;0m\033[48;2;255;255;255m" # pyright: ignore[reportArgumentType]

def testLog():
    assert owo.log("testing") == f"{dt.datetime.now().replace(microsecond=0)}: testing\n"

def test_debugPause_called():
    with patch("builtins.input", return_value=""):
        assert owo.debugPause(True) is None

def test_debugPause_not_called():
    with patch("builtins.input") as mock_input:
        owo.debugPause(False)
        mock_input.assert_not_called()

def testDefaultLogfileWarning(capsys):
    owo.LOGFILE = os.getenv("LOGFILE", "owolib.log")
    owo.log("testing")
    capturedOutput = capsys.readouterr()
    assert capturedOutput.out == f"{owo.Colors.YELLOW}WARNING: Using default Logfile {os.getenv("DEFAULT_LOGFILE", "owolib.py")}\n Change the default in .env or use the variable LOGFILE to set a name for the file and disable this warning.{owo.Colors.RESET}\n"

def testNoDefaultLogfileWarning(capsys):
    owo.LOGFILE = "testabc123.test.log"
    owo.log("testing")
    capturedOutput = capsys.readouterr()
    assert capturedOutput.out == ""
