# -*- coding: utf-8 -*-
"""
Created on Wed May 26 20:23:51 2021

@author: Brant Pastore
This is more POC, we can use this for future automation tasks.
"""

import pywinauto
import sys

from pywinauto.keyboard import send_keys
from pywinauto import Application

from sys import path
path.append('./scripts/')
import GenOTP

def SelectDepartment(parm):
    app = Application(backend="uia").connect(path=r'C:\Program Files (x86)\Remote Utilities - Viewer/rutview.exe')
    app.windows()

    dlg = app["is online"] # The window contains "<Devicename> is online, so lets connect to that window.
    window = app.RemoteUtilitiesViewer
    window.set_focus()

    print("New Online Device!") # Temporary alert



if __name__ == "__main__":
    SelectDepartment(26)
