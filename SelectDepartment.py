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

from sys import path
path.append('./scripts/')
import GenOTP

def SelectDepartment(parm):
    app = Application(backend="uia").connect(path=r'C:\Program Files (x86)\Remote Utilities - Viewer/rutview.exe')
    app.windows()

    dlg = app["Remote Utilities - Viewer"]
    window = app.RemoteUtilitiesViewer
    window.set_focus()

    #dlg.print_control_identifiers()

    #TODO:
    # Add switch for departments based on parameter passed.
    #window.TreeView.get_item([u'Clinical and Wellness']).select()
    #window.TreeView.get_item([u'Community Ambassadors']).select()
    #window.TreeView.get_item([u'Development & Marketing']).select()
    #window.TreeView.get_item([u'Donated']).select()
    #window.TreeView.get_item([u'Education']).select()
    #window.TreeView.get_item([u'Executive']).select()
    #window.TreeView.get_item([u'Finance']).select()
    #window.TreeView.get_item([u'HP Site']).select()
    #window.TreeView.get_item([u'Intervention']).select()
    #window.TreeView.get_item([u'MEL']).select()
    window.TreeView.get_item([u'Misc']).select()
    #window.TreeView.get_item([u'Operations']).select()
    #window.TreeView.get_item([u'PIT']).select() # Select the appropriate department
    #window.TreeView.get_item([u'Programs']).select()

    # "Connections" are updated when the TreeView item (Department) is selected
    #window.Connections.print_control_identifiers() # Display all 'Connection' identifiers

    window.Connections.
    #https://stackoverflow.com/questions/54310435/how-to-identify-ui-elements-when-multiple-ui-elements-have-same-ui-elements

    # Iterate over the Identifiers, and see if they're online or not.
    #"Help description =Online" we can filter by this to select the appropriate machines



if __name__ == "__main__":
    SelectDepartment(26)
