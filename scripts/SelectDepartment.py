# -*- coding: utf-8 -*-
"""
Created on Wed May 26 11:59:09 2021

@author: Brant Pastore

Departments are folders we create, we can select them by name and view the associated devices.
"""

import pywinauto
import sys

from pywinauto.keyboard import send_keys
from pywinauto import Application

def SelectDepartment(parm):
    app = Application(backend="uia").connect(path=r'C:\Program Files (x86)\Remote Utilities - Viewer/rutview.exe')
    app.windows()

    dlg = app["Remote Utilities - Viewer"]
    window = app.RemoteUtilitiesViewer
    window.set_focus()

    #TODO:
    # Add switch for departments based on parameter passed.
    #window.TreeView.get_item([u'Device Directory']).select()


if __name__ == "__main__":
    SelectDepartment(26)
