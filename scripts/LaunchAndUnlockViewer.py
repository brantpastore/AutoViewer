import pywinauto
from pywinauto.application import Application
import sys
from pywinauto.keyboard import send_keys

from sys import path
path.append('./scripts/')
import GenOTP

def GetWindow():
    # TODO: 
    # Set the size of the window when opening it.
    # Remote execution (See: https://pywinauto.readthedocs.io/en/latest/remote_execution.html)
	app = Application(backend="uia").start('C:/Program Files (x86)/Remote Utilities - Viewer/rutview.exe').connect(path=r"C:/Program Files (x86)/Remote Utilities - Viewer/rutview.exe")
	app.windows()

	dlg = app['Remote Utilities - Viewer'] # Grab the window name
	dlg.Edit.type_keys('^a^c{BACKSPACE}') # Clear the text box
	dlg.type_keys("test") # We can store the key in a vault, this is temporary.
	dlg.Edit.type_keys('{ENTER}') # Unlock the viewer


if __name__ == "__main__":
	GetWindow()
