import pywinauto, sys
from pywinauto.keyboard import send_keys

from sys import path
path.append('./scripts/')
import GenOTP

def OTPWindow():
	app = pywinauto.application.Application()
	app.connect(path=r"C:/Program Files (x86)/Remote Utilities - Viewer/rutview.exe")
	app.windows()

	dlg = app['Enter one time password'] # Grab the specified window by title

	dlg.Edit.type_keys('^a^c{BACKSPACE}') # Clear the input box

	otp = GenOTP.RetrieveToken() # Retrieve OTP Code
	dlg.Edit.type_keys(otp) # Enter the OTP generated code 
	dlg.TButton.click() # Submit OTP Code


if __name__ == "__main__":
	OTPWindow()