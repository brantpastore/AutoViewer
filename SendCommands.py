# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 10:46:42 2021

@author: Brant
"""

from sys import path
path.append('./scripts/')
import SelectDevices
import LoginToDevice
import LogoutOfDevice
import VerifyLogin
import TerminalCommands

if __name__ == "__main__":
    OnlineDevices = SelectDevices.Select(1) # 1 = Online devices
    OfflineDevices = SelectDevices.Select(0) # 0 = Offline Devices
    
    print("Found: " + str(len(OnlineDevices)) + " online devices.")
    
    ActiveDevice = LoginToDevice.UsingName(OnlineDevices, 'TestPC.build.local')

    
    