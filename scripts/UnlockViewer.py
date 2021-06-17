import pywinauto
import sys

from pywinauto.keyboard import send_keys
from pywinauto import Application

from sys import path
path.append('./scripts/')
import GenOTP

def GetWindow():
    app = Application(backend="uia").connect(path=r'C:\Program Files (x86)\Remote Utilities - Viewer/rutview.exe')
    app.windows()

    dlg = app["Remote Utilities - Viewer"]
    dlg.set_focus()
    dlg.type_keys('{BACKSPACE}')
    # TODO:
        # Move the secret to Azure Vault.
    dlg.type_keys("test", set_foreground=False)
    dlg.type_keys('{ENTER}') # Unlock the viewer

if __name__ == "__main__":
    GetWindow()
