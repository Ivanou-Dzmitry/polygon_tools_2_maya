#******************************************************************************************************
# Created: polygon.by        
# Last Updated: 27 november 2019
# Version: 2.1.1
#
# Authors:
#"Mango Team"
# Dzmitry Ivanou
# Dzmitry Dzrynou
#
# Much thanks to Yury Ruskevich, Aleksander Kuzmin, CGCode Telegram Channel and Alexander Plechkov for some good ideas an support.
#
#******************************************************************************************************
# MODIFY THIS AT YOUR OWN RISK

import os
import sys
import weakref
import maya.cmds as cmds
import maya._OpenMayaUI as omui

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtUiTools import * 
from shiboken2 import wrapInstance

import pt_modules.pt_gui as gui
reload(gui)

def pt_dock_window(dialog_class):
    try:
        gui.JobCleaner()
        cmds.deleteUI(dialog_class.CONTROL_NAME)
        print 'PolygonTools is already running. Source: {}'.format(dialog_class.CONTROL_NAME)
        print "PolygonTools: Restart..."
        print ""
        
    except:
        pass
    
    main_control = cmds.workspaceControl(dialog_class.CONTROL_NAME, ttc=["AttributeEditor", -1], label = dialog_class.DOCK_LABEL_NAME)
    
    # setup Widget
    cmds.evalDeferred(lambda *args: cmds.workspaceControl(main_control, e=True, restore=False, floating=True, ih=820, iw=350, minimumWidth=350, heightProperty='fixed', wp='fixed'))
    
    #obtain the Maya main window widget as a PySide2 widget
    control_widget = omui.MQtUtil_findControl(main_control)
    
    control_wrap = wrapInstance(long(control_widget), QDialog)
    control_wrap.setAttribute(Qt.WA_DeleteOnClose)
   
    ptwin = dialog_class(control_wrap)
    
    return ptwin


#main function for run
def main():
    print "---------------------"
    print "PolygonTools started!"
    print "---------------------"
    
    ptdlg = pt_dock_window(gui.PTGUI)
