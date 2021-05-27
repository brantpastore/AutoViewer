import pywinauto, sys
from pywinauto.keyboard import send_keys

def LockViewer():
	app = pywinauto.application.Application()
	app.connect(path=r"C:/Program Files (x86)/Remote Utilities - Viewer/rutview.exe")

	app.windows()
	dlg = app['Remote Utilities - Viewer'] # Select the window by title
	dlg.type_keys('%l') # The shortcut Alt lists sub-shortcuts (l locks the viewer)


if __name__ == "__main__":
	LockViewer()
