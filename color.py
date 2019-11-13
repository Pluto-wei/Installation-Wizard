import platform
import sys
import ctypes
__stdInputHandle = -10
__stdOutputHandle = -11
__stdErrorHandle = -12
__foreGroundBLUE = 0x09
__foreGroundGREEN = 0x0a
__foreGroundRED = 0x0c
__foreGroundYELLOW = 0x0e
stdOutHandle=ctypes.windll.kernel32.GetStdHandle(__stdOutputHandle)
def setCmdColor(color,handle=stdOutHandle):
    return ctypes.windll.kernel32.SetConsoleTextAttribute(handle, color)
def resetCmdColor():
    setCmdColor(__foreGroundRED | __foreGroundGREEN | __foreGroundBLUE)
def printBlue(msg):
    setCmdColor(__foreGroundBLUE)
    sys.stdout.write(msg + '\n')
    resetCmdColor()
def printGreen(msg):
    setCmdColor(__foreGroundGREEN)
    sys.stdout.write(msg + '\n')
    resetCmdColor()
def printRed(msg):
    setCmdColor(__foreGroundRED)
    sys.stdout.write(msg + '\n')
    resetCmdColor()
def printYellow(msg):
    setCmdColor(__foreGroundYELLOW)
    sys.stdout.write(msg + '\n')
    resetCmdColor()
