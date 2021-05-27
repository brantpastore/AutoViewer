import pywinauto, sys
from pywinauto.keyboard import send_keys

import warnings
warnings.filterwarnings("ignore")

# Function to convert our program arguments to a string
def listToString(s): 
    # initialize an empty string
    str1 = " " 
    # return string  
    return (str1.join(s))


def TerminalWindow(command):
	app = pywinauto.application.Application()
	app.connect(path=r"C:/Program Files (x86)/Remote Utilities - Viewer/rutview.exe")
	app.windows()

	dlg = app['TfmTelnet'] # Grab the terminal window

	# Clear the text field
	dlg.Edit.type_keys('{BACKSPACE 30}')

	print ("Sending command")
	dlg.Edit.type_keys(command, pause=None,with_spaces=True) # Make sure we speed this up, and keep spaces between commands.
	dlg.Edit.type_keys('{ENTER}')
	

	dlg.print_control_identifiers()

if __name__ == "__main__":
	args = sys.argv
	args.pop(0) # we have to remove the file name from the list
	args = listToString(args) # Convert the list to a string.

	print("Running command: ", args)
	TerminalWindow(args)