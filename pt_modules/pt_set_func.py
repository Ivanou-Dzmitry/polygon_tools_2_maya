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
import maya.cmds as cmds
import platform

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtUiTools import *

sys.path.append('..')
import pt_config_loader as cfgl
reload(cfgl)

#GUI    
class PT_Settings_Tab (QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent=parent)
        
        #set layoit
        self.tabSet_v_layout = QVBoxLayout(self)
        self.tabSet_v_layout.setAlignment(Qt.AlignTop)
        self.tabSet_v_layout.setContentsMargins(0,10,0,10)
        self.tabSet_v_layout.setSpacing(5)
        
        currentDir = os.path.dirname(__file__)
        try:
            iconRusLang  = QPixmap(currentDir +"/icons/ruslang_icon.png")
            iconEngLang  = QPixmap(currentDir +"/icons/englang_icon.png")
            iconReset  = QPixmap(currentDir +"/icons/reset_icon.png")
        except:
            cmds.warning( "PolygonTools: Can't load icons for Settings Tab! Check icon files in pt_modules/icons directory.")
                
        self.gboxSet = QGroupBox("Units Setup")
        self.gboxSet.setMaximumWidth(340)
        self.gboxSet_v_layout = QVBoxLayout()

        #Top Label
        self.lblInfo_01 = QLabel()

        #Units
        self.cboxSysUnits = QComboBox()
        self.cboxSysUnits.addItems(["m","cm","mm"])
        
        #Units label
        self.lblSysUnits = QLabel("Working Units ")
        
        self.btnReset = QPushButton("Reset All Values to Default")
        #self.btnReset.setMaximumWidth(200)
        self.btnReset.setMinimumWidth(200)
        self.btnReset.setMinimumHeight(30)
        self.btnReset.setIcon(iconReset)          
        
        self.lblSysInfo = QLabel("Python Info:")
        
        self.gboxConclusionLang = QGroupBox("Conclusion Language")
        self.gboxConclusionLang.setMaximumWidth(340)
        self.gboxConclusionLang_v_layout = QVBoxLayout()
        
        #layout for buttons
        self.tabSet_h_layout_02 = QHBoxLayout()
        self.tabSet_h_layout_02.setAlignment(Qt.AlignLeft)

        #lang icons
        self.btnRusLang = QToolButton()
        self.btnRusLang.setCheckable(True)
        self.btnRusLang.setIcon(iconRusLang)
         
        self.btnEngLang = QToolButton() 
        self.btnEngLang.setIcon(iconEngLang)
        self.btnEngLang.setCheckable(True)        
        
        #add button to the layout
        self.tabSet_h_layout_02.addWidget(self.btnEngLang)
        self.tabSet_h_layout_02.addWidget(self.btnRusLang)        
        self.gboxConclusionLang_v_layout.addLayout(self.tabSet_h_layout_02)        
        
        self.gboxSysInfo = QGroupBox("System Info")
        self.gboxSysInfo.setMaximumWidth(340)
        self.gboxSysInfo_v_layout = QVBoxLayout()                
        
        #Add Widgets
        
        self.tabSet_v_layout.addWidget(self.lblInfo_01)
        
        self.tabSet_v_layout.addWidget(self.gboxSet)
        self.gboxSet.setLayout(self.gboxSet_v_layout)
        
        #Horiz Layout for Set        
        self.tabSet_h_layout_01 = QHBoxLayout()
        self.tabSet_h_layout_01.setAlignment(Qt.AlignLeft)
        
        self.gboxSet_v_layout.addLayout(self.tabSet_h_layout_01)
        
        self.tabSet_h_layout_01.addWidget(self.lblSysUnits)
        self.tabSet_h_layout_01.addWidget(self.cboxSysUnits)
        
        #conclusion
        self.gboxConclusionLang.setLayout(self.gboxConclusionLang_v_layout)
        self.tabSet_v_layout.addWidget(self.gboxConclusionLang)
        
        self.tabSet_v_layout.addWidget(self.gboxSysInfo)
        self.gboxSysInfo.setLayout(self.gboxSysInfo_v_layout)
        
        self.gboxSysInfo_v_layout.addWidget(self.lblSysInfo)
        self.lblSysInfo.setWordWrap(True)
        
        self.tabSet_v_layout.addWidget(self.btnReset)
        
        #get Pyton version
        self.lblSysInfo.setText("Python: " + (platform.sys.version))
        
        #SIGNALS
        self.cboxSysUnits.activated.connect(self.setWorkUnits)

        #change lang
        self.btnEngLang.pressed.connect(self.btnEngLangPressed)
        self.btnRusLang.pressed.connect(self.btnRusLangPressed)
        
        self.btnReset.clicked.connect(self.btnResetPressed)           
        
        self.checkUnits()
        
        #lang selector
        current_languge = cfgl.configLoader()[14]
        
        # check buttons
        if current_languge == "eng":
            self.btnRusLang.setChecked(False)
            self.btnEngLang.setChecked(True)
        elif current_languge == "rus":
            self.btnRusLang.setChecked(True)
            self.btnEngLang.setChecked(False)     


    #eng lang ON
    def btnEngLangPressed(self):
        
        self.btnRusLang.setChecked(False)

        #for press again
        if self.btnEngLang.isChecked() == True:
            self.btnRusLangPressed()
        
        #change lang
        path_config = cfgl.configLoader()[99:101]
        cfgl.ConfigWriter('Languge', 'current_languge', 'eng', path_config[0], path_config[1])
        
    #rus lang ON
    def btnRusLangPressed(self):
        
        self.btnEngLang.setChecked(False)

        #for press again
        if self.btnRusLang.isChecked() == True:
            self.btnEngLangPressed()

        #change lang
        path_config = cfgl.configLoader()[99:101]
        cfgl.ConfigWriter('Languge', 'current_languge', 'rus', path_config[0], path_config[1])

        #change working units    
    def setWorkUnits(self):
        
        #load path and config        
        path_config = cfgl.configLoader()[99:101] 
        
        if self.cboxSysUnits.currentIndex() == 0:
            cmds.currentUnit( linear='m' )
            self.lblInfo_01.setText("Units changed to m")
            print "Units changed to m"
            cfgl.ConfigWriter('Units', 'Custom_System_type_units', 'm', path_config[0], path_config[1]) 
    
        if self.cboxSysUnits.currentIndex() == 1:
            cmds.currentUnit( linear='cm' )
            self.lblInfo_01.setText("Units changed to cm")
            print "Units changed to cm"
            cfgl.ConfigWriter('Units', 'Custom_System_type_units', 'cm', path_config[0], path_config[1]) 

        if self.cboxSysUnits.currentIndex() == 2:
            cmds.currentUnit( linear='mm' )
            self.lblInfo_01.setText("Units changed to mm")
            print "Units changed to mm"
            cfgl.ConfigWriter('Units', 'Custom_System_type_units', 'mm', path_config[0], path_config[1]) 
        
            
    #compare units in cfg and system
    def checkUnits(self):
        
        #load custom units from cfg file cfgl.configLoader()[9]
        custom_sys_units = cfgl.configLoader()[9]
    
        cur_work_units = cmds.currentUnit(query=True)
        
        #check units change Job
        UnitsCheckerJob = cmds.scriptJob( runOnce=False, event=['linearUnitChanged', self.UnitChanger])

        
        if custom_sys_units != cur_work_units:
            cmds.currentUnit( linear=custom_sys_units )
            
            if custom_sys_units == 'm':
                self.cboxSysUnits.setCurrentIndex(0)

            if custom_sys_units == 'cm':
                self.cboxSysUnits.setCurrentIndex(1)

            if custom_sys_units == 'mm':
                self.cboxSysUnits.setCurrentIndex(2)
            
            print "PolygonTools: Units changed to ", custom_sys_units
            self.lblInfo_01.setText("Units changed to " + custom_sys_units)
            
        else:
            if custom_sys_units == 'm':
                self.cboxSysUnits.setCurrentIndex(0)

            if custom_sys_units == 'cm':
                self.cboxSysUnits.setCurrentIndex(1)

            if custom_sys_units == 'mm':
                self.cboxSysUnits.setCurrentIndex(2)
            
            print "PolygonTools: Units is ", custom_sys_units
            self.lblInfo_01.setText("Units is " + custom_sys_units)
            
    def UnitChanger(self):
        CurUnits = cmds.currentUnit(query=True)
        
        if CurUnits == 'm':
            self.cboxSysUnits.setCurrentIndex(0)

        if CurUnits == 'cm':
            self.cboxSysUnits.setCurrentIndex(1)

        if CurUnits == 'mm':
            self.cboxSysUnits.setCurrentIndex(2)

        
        self.lblInfo_01.setText("Units changed to " + CurUnits)
        
        print("PolygonTools: Units was changed!")        
    
    def btnResetPressed(self):
        
        path_config = cfgl.configLoader()[99:101]  
        
        #restore default values
        cfgl.CreateDefaultConfig(path_config[1], path_config[0])
