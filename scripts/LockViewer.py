import pywinauto, sys
from pywinauto.keyboard import send_keys

def LockViewer():
	app = pywinauto.application.Application()
	app.connect(path=r"C:/Program Files (x86)/Remote Utilities - Viewer/rutview.exe")

	app.windows()
	dlg = app['Remote Utilities - Viewer'] # Select the window by title
    
    # The Alt key lists sub-shortcuts 
	dlg.type_keys('%l') # ALT + l locks the viewer


if __name__ == "__main__":
	LockViewer()
