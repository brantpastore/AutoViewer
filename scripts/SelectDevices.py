# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 14:05:05 2021

@author: Brant
"""

import pywinauto
import sys

from pywinauto.keyboard import send_keys
from pywinauto import Application


# This selects the Connections ItemList and we Iterate over the ListItems to obtain the appropriate information.
def Select(State):
    app = Application(backend="uia").connect(path=r'C:\Program Files (x86)\Remote Utilities - Viewer/rutview.exe')
    app.windows()

    dlg = app["Remote Utilities - Viewer"]
    window = app.RemoteUtilitiesViewer
    window.set_focus()
    
    # Create our list of devices, so we can iterate through the machines and perform wizardry. Store the offline devices in a seperate list so we can log what hasn't been selected yet.
    OnlineDevices = []
    OfflineDevices = []

    
    # We need to get the status of the device (Wether its online or offline, we can grab this information from the 'Help' field.)
    #device = window.Connections.child_window(control_type="List").ListItems
    devices = window.Connections.child_window(control_type="List").items()
    
    #"Help description =Online" we can filter by this to select the appropriate machines
    # Iterate through out Item list of Connections, check if the device is online or offline. Add them to the appropriate list.
    for item in devices:
        if (item.legacy_properties()['Help'] == "Online"):
            #print("Device is online! Adding to Online list")
            OnlineDevices.append(item)
        else:
            #print("Device is offline. Added to Offline list")
            OfflineDevices.append(item)
            
            
    if (State == 1):
        return OnlineDevices
    elif (State == 0):
        return OfflineDevices

if __name__ == "__main__":
    Select(args)
