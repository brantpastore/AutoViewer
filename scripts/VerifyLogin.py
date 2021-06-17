# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 10:39:06 2021

@author: Brant
"""

import pywinauto
import sys

from pywinauto.keyboard import send_keys
from pywinauto import Application


# This selects the Connections ItemList and we Iterate over the ListItems to obtain the appropriate information.
def VerifyLoggedIn(SelectedDevice):
    app = Application(backend="uia").connect(path=r'C:\Program Files (x86)\Remote Utilities - Viewer/rutview.exe')
    app.windows()

    dlg = app["Remote Utilities - Viewer"]
    window = app.RemoteUtilitiesViewer
    window.set_focus()
    
    State = 3 # Initially this is an arbitrary value.
    
    print(SelectedDevice.legacy_properties()['Help'])
    
    #"Help description =Online" we can filter by this to select the appropriate machines
    # Iterate through out Item list of Connections, check if the device is online or offline. Add them to the appropriate list.
    if (SelectedDevice.legacy_properties()['Help'] == "Logging on"):
        State = 2
    elif (SelectedDevice.legacy_properties()['Help'] == "Logged On"):
        State = 1     
    elif (SelectedDevice.legacy_properties()['Help'] == "Online"):
        State = 0
        
    return State
        

if __name__ == "__main__":
    VerifyLoggedIn(args)