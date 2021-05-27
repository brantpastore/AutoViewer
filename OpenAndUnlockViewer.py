import pywinauto
from pywinauto.application import Application
import sys
from pywinauto.keyboard import send_keys

from sys import path
path.append('./scripts/')
import GenOTP

def GetWindow():
	app = Application(backend="uia").start('C:/Program Files (x86)/Remote Utilities - Viewer/rutview.exe').connect(path=r"C:/Program Files (x86)/Remote Utilities - Viewer/rutview.exe")
	app.windows()
	
	dlg = app['Remote Utilities - Viewer']
	dlg.Edit.type_keys('^a^c{BACKSPACE}') # Clear the password field
	dlg.type_keys("PASSWORD_HERE") # Enter the password
	dlg.Edit.type_keys('{ENTER}') # Submit password


if __name__ == "__main__":
	GetWindow()


	#https://pywinauto.readthedocs.io/en/latest/getting_started.html
	#https://stackoverflow.com/questions/50656751/pywinauto-send-key-down-to-application
	#https://readthedocs.org/projects/airelil-pywinauto/downloads/pdf/latest/