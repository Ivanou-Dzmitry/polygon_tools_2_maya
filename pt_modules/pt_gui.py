#******************************************************************************************************
# Created: polygon.by        
# Last Updated: 27 november 2019
# Version: 2.1.0      
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
import webbrowser
import maya.mel

import pt_gen_func as genf
reload (genf)

import pt_set_func as setf
reload (setf)

import pt_uv_func as uvf
reload (uvf)

import pt_texel_func as tef
reload (tef)

import pt_tools_func as tools
reload (tools)

import pt_check_func as check
reload (check)

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtUiTools import *

class PTGUI(QDialog):
    CONTROL_NAME = 'Polygon_Tools_2_1_1'
    DOCK_LABEL_NAME = 'Polygon Tools 2.1.1'
            
    def __init__(self, parent=None):
        super (PTGUI, self).__init__(parent)
        self.window_name = self.CONTROL_NAME
        self.setSizeGripEnabled(False)
        
        #Create Global layout
        self.main_layout = parent.layout()
        self.main_layout.setContentsMargins(0, 0, 0, 0)
		
        #Vertical layout
        self.pt_main_layout = QVBoxLayout()
        self.pt_main_layout.setAlignment(Qt.AlignTop)
        self.pt_main_layout.setContentsMargins(5,5,5,10)
        self.pt_main_layout.setSpacing(5)
    
        #Tab widget
        self.tabPt = QTabWidget()
        self.tabPt.setTabPosition(QTabWidget.North)
        self.tabPt.setTabShape(QTabWidget.Rounded)
        self.tabPt.setElideMode(Qt.ElideNone)
        self.tabPt.setDocumentMode(True)
        self.tabPt.setTabsClosable(False)
        self.tabPt.setMovable(True)
        self.tabPt.setObjectName("tabPt")
        
        #Create Tabs
        self.tabGen = genf.PT_Gen_Tab()
        self.tabTex = tef.PT_Texel_Tab()
        self.tabUv = uvf.PT_UV_Tab()
        self.tabTools = tools.PT_Toools_Tab()
        self.tabSet = setf.PT_Settings_Tab()
        self.tabCheck = check.PT_Check_Tab()
        
        #Add tabs to Tab
        self.tabPt.addTab(self.tabGen, "General")
        self.tabPt.addTab(self.tabTex, "Texel")
        self.tabPt.addTab(self.tabUv, "UV")
        self.tabPt.addTab(self.tabTools, "Tools")
        self.tabPt.addTab(self.tabCheck, "Checker")
        self.tabPt.addTab(self.tabSet, "Settings")
        
        #Copyright label        
        self.lblcopyright = QLabel(u'\N{COPYRIGHT SIGN}' + "polygon.by, 2019 | e-mail: info@polygon.by")
        
        #Help Button
        self.btnHelp = QPushButton("?")
        self.btnHelp.setMinimumWidth(23)
        self.btnHelp.setStyleSheet("background-color:#e83736;")
        
        #set layout to widget
        self.main_layout.addLayout(self.pt_main_layout)
        
        #set TabBar to layout
        self.pt_main_layout.addWidget(self.tabPt)
                
        self.tabMain_h_layout_01 = QHBoxLayout()
        self.tabMain_h_layout_01.setAlignment(Qt.AlignLeft)
        self.pt_main_layout.addLayout(self.tabMain_h_layout_01)
        
        #set copyright label
        self.tabMain_h_layout_01.addWidget(self.lblcopyright)
        self.tabMain_h_layout_01.addWidget(self.btnHelp)
        
        self.btnHelp.clicked.connect(self.helpOpen)
                    
    def helpOpen(self):
        try:
            help_link="https://docs.google.com/document/d/1BtnRSbD_boxEyUyMQwcEXeAYhmw91KjLsBWhV_11GWQ/edit?usp=sharing"
            webbrowser.open(help_link)
        except:
            print "Can't open link. Open it manually - https://docs.google.com/document/d/1BtnRSbD_boxEyUyMQwcEXeAYhmw91KjLsBWhV_11GWQ/edit?usp=sharing"
    
                                                                       
    def run(self):
        return self
        
    def __del__(self):
        print "-----------------------"
        print "PolygonTools cleanup operations"
        print ""
        
        JobCleaner()
            
        print ""
        print "PolygonTools was closed."
        print "------------------------"
        
def JobCleaner():
    if cmds.objExists('LOD_Group_PT'):
        cmds.headsUpDisplay( 'distanceHUD', rem=True )            
    
    try:
        #get Jobs List
        CurrentJobs = cmds.scriptJob( listJobs=True )
        
        #find string in Array
        if any("linearUnitChange" in s for s in CurrentJobs):
            #OurJob
            UnitJob = filter(lambda UnitJob: 'linearUnitChange' in UnitJob, CurrentJobs)[0]
            #get Job number
            UnitJobNumber = UnitJob.split(':')[0]                
            #kill job
            cmds.scriptJob( kill=int(UnitJobNumber))
        
            print "PolygonTools: UnitsCheckerJob was deleted. Job#: ", UnitJobNumber
    except:
        print "PolygonTools: Cant delete UnitsCheckerJob."
        
    try:
        #DeleteLodJob
        if any("LOD_0.lodVisibility" in s for s in CurrentJobs):
             LODJob = filter(lambda LODJob: 'LOD_0.lodVisibility' in LODJob, CurrentJobs)[0]
             LODJobNumber = LODJob.split(':')[0]
             cmds.scriptJob( kill=int(LODJobNumber))
            
             print "PolygonTools: VisibilityCheckerJob was deleted. Job#: ", LODJobNumber
    except:
        print "PolygonTools: Cant delete VisibilityCheckerJob."

    try:
        #DeleteLODCheckJobNumber
        if any("runLODCheckerJob" in s for s in CurrentJobs):
             LODCheckJob = filter(lambda LODCheckJob: 'runLODCheckerJob' in LODCheckJob, CurrentJobs)[0]
             LODCheckJobNumber = LODCheckJob.split(':')[0]
             cmds.scriptJob( kill=int(LODCheckJobNumber))
            
             print "PolygonTools: LODCheckerJob was deleted. Job#: ", LODCheckJobNumber
    except:
        print "PolygonTools: Cant delete  LODCheckerJob."
        
        
    try:
        #DeleteLODCheckJobNumber
        if any("NewSceneJob" in s for s in CurrentJobs):
             NewSceneJob = filter(lambda NewSceneJob: 'NewSceneJob' in NewSceneJob, CurrentJobs)[0]
             NewSceneJobNumber = NewSceneJob.split(':')[0]
             cmds.scriptJob( kill=int(NewSceneJobNumber))
            
             print "PolygonTools: NewSceneJob was deleted. Job#: ", NewSceneJobNumber
    except:
        print "PolygonTools: Cant delete NewSceneJob."
    

    #check userScript Dir
    UserScriptDir = cmds.internalVar(userScriptDir=True) + 'userSetup.mel'
    
    #if file exist delete some text from userSetup.mel 
    if os.path.isfile(UserScriptDir) == True: 
    
        with open(UserScriptDir, "r+") as userSetupmel:
            FileContent = userSetupmel.readlines()
            userSetupmel.seek(0)    
            for i in FileContent:
                if (i != "shelfButton -parent \"Custom\" -label \"PT\" -sourceType \"python\" -image1 $myScriptDir -command \"import polygon_tools as pt\\nreload(pt)\\npt.main()\";\r\n"):
                    userSetupmel.write(i)
            userSetupmel.truncate()
    