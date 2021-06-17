# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 11:21:52 2021

@author: Brant
"""

import pywinauto
import sys

from pywinauto.keyboard import send_keys
from pywinauto import Application
import HandleOTPWindow
import VerifyLogin


# This selects the Connections ItemList and we Iterate over the ListItems to obtain the appropriate information.
def Login(Device):
    app = Application(backend="uia").connect(path=r'C:\Program Files (x86)\Remote Utilities - Viewer/rutview.exe')
    app.windows()

    dlg = app["Remote Utilities - Viewer"]
    window = app.RemoteUtilitiesViewer
    window.set_focus()
    
    if (VerifyLogin.VerifyLoggedIn(Device) == 1):
        return
    elif (VerifyLogin.VerifyLoggedIn(Device) == 0):
        Device.click_input(button='left', double=True) # Double click logs into the device
 
        
    HandleOTPWindow.HandleOTP() # Handle 2FA OTP code
    
    ActiveDevice = Device
    return ActiveDevice
        

# Iterate over the devices and compare the 'Name' property with our DeviceName string
def UsingName(Devices, DeviceName):    
    ActiveDevice = Devices
    
    for device in Devices:
        if (device.legacy_properties()['Name'] == DeviceName):
            print("Found ", device)
            ActiveDevice = Login(device)
            
        
    print (ActiveDevice)
    return ActiveDevice
            
            