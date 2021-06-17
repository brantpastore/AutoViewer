import pywinauto
import sys
import time

from pywinauto.keyboard import send_keys
from pywinauto import Application, Desktop

import warnings
warnings.filterwarnings("ignore")


def SendCommand(command):    
    app = pywinauto.application.Application().connect(best_match='TerminalTfmTelnet0')
    app.windows()

    dlg = app['TfmTelnet'] # Grab the terminal window
    dlg.set_focus()

	# Clear the text field
    dlg.Edit.type_keys('{BACKSPACE 30}')
    #dlg.Edit.type_keys('test')

    print ("Sending command: ", command)
    dlg.Edit.type_keys(command, pause=None,with_spaces=True) # Keep spaces between commands.
    dlg.Edit.type_keys('{ENTER}')
    
if __name__ == "__main__":
    SendCommand("test")