# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 14:04:51 2021

@author: Brant
"""
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 11:21:52 2021

@author: Brant
"""

import pywinauto
import sys

from pywinauto.keyboard import send_keys
from pywinauto import Application
import LoginToDevice


# This selects the Connections ItemList and we Iterate over the ListItems to obtain the appropriate information.
def LoginToDeviceUsingName(DeviceList, DeviceName):    
    for device in DeviceList:
        if (Device.legacy_properties()['Name'] == DeviceName):
            LoginToDevice.Login(device)