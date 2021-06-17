import pywinauto, sys
from pywinauto.keyboard import send_keys
from pywinauto import Application

import time

from sys import path
path.append('./scripts/')
import GenOTP

def HandleOTP():
    app = Application(backend="uia").connect(path=r'C:\Program Files (x86)\Remote Utilities - Viewer/rutview.exe')
    app.windows()
    
    time.sleep(6)
    otpWindow = app.RemoteUtilitiesViewer.Dialog2
    #window.dump_tree()

    
    #dlg = app['Enter one time password'] # Grab the specified window by title
    #try:
    #    dlg.wait('enabled', timeout=18)
    #except Exception:
    #    pass

    otpWindow.Edit.type_keys('^a^c{BACKSPACE}') # Clear the input box
    otp = GenOTP.RetrieveToken() # Retrieve OTP Code
    otpWindow.Edit.type_keys(otp) # Enter the OTP generated code 
    otpWindow.Button.click() # Submit OTP Code
    

if __name__ == "__main__":
	HandleOTP()