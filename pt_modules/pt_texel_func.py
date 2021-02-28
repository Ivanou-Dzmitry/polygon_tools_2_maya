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
import maya.cmds as cmds
import maya.mel
import math
import time
import random
from decimal import Decimal

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtUiTools import *

import pt_conclusion as conclusion
reload(conclusion)

import pt_gen_func as gen_func
reload(gen_func)

sys.path.append('..')
import pt_config_loader as cfgl
reload(cfgl)

class PT_Texel_Tab (QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent=parent)
        
        #Create Widgets
        self.tabTex_v_layout = QVBoxLayout(self)
        self.tabTex_v_layout.setAlignment(Qt.AlignTop)
        self.tabTex_v_layout.setContentsMargins(0,10,0,10)
        self.tabTex_v_layout.setSpacing(5)
        
        currentDir = os.path.dirname(__file__)
        try:
            iconGetTex  = QPixmap(currentDir +"/icons/gettexel_icon.png")
            iconCheckTex  = QPixmap(currentDir +"/icons/checktexel_icon.png")
            iconSetTex  = QPixmap(currentDir +"/icons/settexel_icon.png")
            iconCleanCheck  = QPixmap(currentDir +"/icons/cleancheck_icon.png")
        except:
            cmds.warning( "PolygonTools: Can't load icons for Texel Tab! Check icon files in pt_modules/icons directory.")
        
        
        #Top Label
        self.lblInfo_01 = QLabel()
        self.lblInfo_01.setWordWrap(True)
        self.lblInfo_01.setMargin(2)
                
        #groupbox Prepare
        self.gboxGetTexel = QGroupBox("Get Texel Density")
        self.gboxGetTexel.setMaximumWidth(340)
        self.gboxGetTexel_v_layout = QVBoxLayout()
        
        #groupbox Prepare
        self.gboxSetTexel = QGroupBox("Set Texel Density")
        self.gboxSetTexel.setMaximumWidth(340)
        self.gboxSetTexel_v_layout = QVBoxLayout()     
        
        self.chkUseInUVI = QCheckBox()
        self.chkUseInUVI.setText("Use texel value when checking texel density")
        self.chkUseInUVI.setChecked(True)
        
        #Map Res label
        self.lblMapRes = QLabel("Map size (px)")
        
        #System Units cmbox
        self.cboxTexRes = QComboBox()
        self.cboxTexRes.addItems(["64", "128", "256x128", "256", "512x256", "512", "1024x512", "1024", "2048x1024", "2048", "4096x2048", "4096", "8192"])
        
        self.btnCalcTex = QPushButton("Get Texel")
        self.btnCalcTex.setStyleSheet("background-color:#3d664f;")
        self.btnCalcTex.setMinimumWidth(90)
        self.btnCalcTex.setMinimumHeight(30)
        self.btnCalcTex.setIcon(iconGetTex)
        
        #set tex button
        self.btnSetTex = QPushButton("Set Texel")
        self.btnSetTex.setStyleSheet("background-color:#3d6666;")
        self.btnSetTex.setMaximumWidth(90)
        self.btnSetTex.setMinimumHeight(30)
        self.btnSetTex.setIcon(iconSetTex)
        
        self.edtSetTex = QLineEdit()
        self.edtSetTex.setFixedWidth(50)
        self.edtSetTex.setMaxLength(4)
        self.edtSetTex.setText("400")
        
        self.lblSetTexel = QLabel("Desired texel (px/m) ")
        self.lblSetTexel.setMaximumWidth(115)
        
        self.lblMapSize = QLabel("Map size: ")

        #end set block
        
        self.lblTexel = QLabel("Texel: ")
        self.lblTexel.setMaximumWidth(340)
        self.lblTexel.setStyleSheet('background-color: black; padding: 5px;')
        
        #groupbox Prepare
        self.gboxCheckTexel = QGroupBox("Check Texel Density")
        self.gboxCheckTexel.setMaximumWidth(340)
        self.gboxCheckTexel_v_layout = QVBoxLayout()     

        self.lblInRangeInfo = QLabel("Texel has not been checked yet.")
        self.lblInRangeInfo.setWordWrap(True)
        
        #Progress Bar
        self.pbChekProgress = QProgressBar()
        self.pbChekProgress.setValue(0)
        self.pbChekProgress.setMaximumWidth(340)
        
        self.lblTexel02 = QLabel("Texel")
        self.lblTexel02.setMaximumWidth(25)
        
        self.edtCurTexel = QLineEdit()
        self.edtCurTexel.setFixedWidth(50)
        self.edtCurTexel.setMaxLength(4)
        self.edtCurTexel.setText("256")
        
        self.btnCheckTexel = QPushButton("Check Texel")
        self.btnCheckTexel.setStyleSheet("background-color:#663d5b;")
        self.btnCheckTexel.setMinimumWidth(100)
        self.btnCheckTexel.setMaximumWidth(100)
        self.btnCheckTexel.setMinimumHeight(30)
        self.btnCheckTexel.setIcon(iconCheckTex)
        
        self.lblDiff = QLabel("Range +/- (%)")
        self.lblDiff.setFixedWidth(75)
        
        #Diff spinbox
        self.spnDiff = QSpinBox()
        self.spnDiff.setMinimum(1)
        self.spnDiff.setMaximum(30)
        self.spnDiff.setValue(10)
        
        #Texel label
        self.lblAddCheckHeader = QLabel("Additional Checks")
        
        self.lblTinyIt = QLabel("Tiny Polygons (m" + u'\N{SUPERSCRIPT TWO}'+")")
        self.lblTinyIt.setFixedWidth(95)
        
        self.edtTinyIt = QLineEdit()
        self.edtTinyIt.setFixedWidth(50)
        self.edtTinyIt.setMaxLength(7)
        self.edtTinyIt.setText("0.0001")
        
        self.lblPolyTinyAr = QLabel("Count: ")
        #self.lblPolyTinyAr.setMaximumWidth(120)
        self.lblPolyTinyAr.setVisible(False)
        
        self.btnSelectTinyFace = QPushButton("Not checked yet")
        self.btnSelectTinyFace.setMaximumWidth(160)
        
        self.lblTinyPX = QLabel("Tiny UV Shells (px)")
        self.lblTinyPX.setFixedWidth(95)
        
        self.edtTinyPX = QLineEdit()
        self.edtTinyPX.setFixedWidth(50)
        self.edtTinyPX.setMaxLength(1)
        self.edtTinyPX.setInputMask("D")
        self.edtTinyPX.setText("1")
        
        self.lblUVTinyAr = QLabel("Count: ")
        #self.lblUVTinyAr.setMaximumWidth(120)
        self.lblUVTinyAr.setVisible(False)
        
        self.btnSelectTinyUVShell = QPushButton("Not checked yet")
        self.btnSelectTinyUVShell.setMaximumWidth(160)
                
        self.btnCleanCheck = QPushButton("Clean Check")
        self.btnCleanCheck.setStyleSheet("background-color:#665c63;")
        self.btnCleanCheck.setMaximumWidth(100)
        self.btnCleanCheck.setMinimumWidth(100)
        self.btnCleanCheck.setMinimumHeight(30)
        self.btnCleanCheck.setIcon(iconCleanCheck)        
        
        self.gboxTexConclusion = QGroupBox("Conclusion")
        self.gboxTexConclusion.setMaximumWidth(340)
        self.gboxTexConclusion.setMinimumHeight(170)
        self.gboxTexConclusion_v_layout = QVBoxLayout()

        #conclusion text here
        self.txtbrowTexConclusion = QTextBrowser()
        self.txtbrowTexConclusion.setHtml("")
            
        self.gboxTexConclusion_v_layout.addWidget(self.txtbrowTexConclusion) 

        
        #Add to layout
        self.tabTex_v_layout.addWidget(self.lblInfo_01)
        
        #add texel group box
        self.tabTex_h_layout = QHBoxLayout()
        self.tabTex_h_layout.setAlignment(Qt.AlignLeft)
        self.tabTex_h_layout.setContentsMargins(0,0,0,0)
        self.tabTex_h_layout.setSpacing(10)

        self.tabTex_h_layout.addWidget(self.lblMapRes)
        self.tabTex_h_layout.addWidget(self.cboxTexRes)
        self.tabTex_h_layout.addWidget(self.btnCalcTex)
        
        self.gboxGetTexel_v_layout.addLayout(self.tabTex_h_layout)
        
        self.gboxGetTexel_v_layout.addWidget(self.lblTexel)
        self.gboxGetTexel_v_layout.addWidget(self.chkUseInUVI)
        
        #add texel group box
        self.tabTex_v_layout.addWidget(self.gboxGetTexel)
        self.gboxGetTexel.setLayout(self.gboxGetTexel_v_layout)
        
        self.gboxSetTexel_v_layout.addWidget(self.lblMapSize)

        self.tabTex_h_Setlayout = QHBoxLayout()
        self.tabTex_h_Setlayout.setAlignment(Qt.AlignLeft)
        self.tabTex_h_Setlayout.setContentsMargins(0,0,0,0)
        self.tabTex_h_Setlayout.setSpacing(10)
        
        self.gboxSetTexel_v_layout.addLayout(self.tabTex_h_Setlayout)
        
        self.tabTex_h_Setlayout.addWidget(self.lblSetTexel)
        self.tabTex_h_Setlayout.addWidget(self.edtSetTex)
        self.tabTex_h_Setlayout.addWidget(self.btnSetTex)
        
        #add SET texel group box
        self.tabTex_v_layout.addWidget(self.gboxSetTexel)
        self.gboxSetTexel.setLayout(self.gboxSetTexel_v_layout)
        
        self.gboxCheckTexel_v_layout.addWidget(self.lblInRangeInfo)
        self.gboxCheckTexel_v_layout.addWidget(self.pbChekProgress)
        
        #add layout for CurTexel
        self.tabTex_h_layout_02 = QHBoxLayout()
        self.tabTex_h_layout_02.setAlignment(Qt.AlignLeft)
        self.tabTex_h_layout_02.setSpacing(10)
        self.gboxCheckTexel_v_layout.addLayout(self.tabTex_h_layout_02)
        
        self.tabTex_h_layout_02.addWidget(self.lblTexel02)
        self.tabTex_h_layout_02.addWidget(self.edtCurTexel)
        
        #add layout for lblDiff
        self.tabTex_h_layout_03 = QHBoxLayout()
        self.tabTex_h_layout_03.setAlignment(Qt.AlignLeft)
        self.tabTex_h_layout_03.setSpacing(10)
        self.gboxCheckTexel_v_layout.addLayout(self.tabTex_h_layout_03)
        
        self.tabTex_h_layout_03.addWidget(self.lblDiff)
        self.tabTex_h_layout_03.addWidget(self.spnDiff)
        
        #add layout for CurTexel
        self.tabTex_h_layout_05 = QHBoxLayout()
        self.tabTex_h_layout_05.setAlignment(Qt.AlignLeft)
        self.tabTex_h_layout_05.setSpacing(10)
        self.tabTex_h_layout_05.setContentsMargins(0,0,0,10)
        self.gboxCheckTexel_v_layout.addLayout(self.tabTex_h_layout_05)
        
        self.tabTex_h_layout_05.addWidget(self.btnCheckTexel)
        self.tabTex_h_layout_05.addWidget(self.btnCleanCheck)
        
        self.tex_h_line_02 = QFrame()
        self.tex_h_line_02.setFrameShape(QFrame.HLine)
        self.tex_h_line_02.setFrameShadow(QFrame.Sunken)
        self.gboxCheckTexel_v_layout.addWidget(self.tex_h_line_02)
        
        self.gboxCheckTexel_v_layout.addWidget(self.lblAddCheckHeader)
        
        #add layout for TinyIt
        self.tabTex_h_layout_04 = QHBoxLayout()
        self.tabTex_h_layout_04.setAlignment(Qt.AlignLeft)
        self.tabTex_h_layout_04.setSpacing(10)
        self.gboxCheckTexel_v_layout.addLayout(self.tabTex_h_layout_04)
        
        self.tabTex_h_layout_04.addWidget(self.lblTinyIt)
        self.tabTex_h_layout_04.addWidget(self.edtTinyIt)
        self.tabTex_h_layout_04.addWidget(self.lblPolyTinyAr)
        self.tabTex_h_layout_04.addWidget(self.btnSelectTinyFace)
        
        #add layout for TinyPX
        self.tabTex_h_layout_05 = QHBoxLayout()
        self.tabTex_h_layout_05.setAlignment(Qt.AlignLeft)
        self.tabTex_h_layout_05.setSpacing(10)
        self.gboxCheckTexel_v_layout.addLayout(self.tabTex_h_layout_05)
        
        self.tabTex_h_layout_05.addWidget(self.lblTinyPX)
        self.tabTex_h_layout_05.addWidget(self.edtTinyPX)
        self.tabTex_h_layout_05.addWidget(self.lblUVTinyAr)
        self.tabTex_h_layout_05.addWidget(self.btnSelectTinyUVShell)

        #H-Line 4
        self.tex_h_line_04 = QFrame()
        self.tex_h_line_04.setFrameShape(QFrame.HLine)
        self.tex_h_line_04.setFrameShadow(QFrame.Sunken)
        self.gboxCheckTexel_v_layout.addWidget(self.tex_h_line_04)
                        
        #group Check
        self.tabTex_v_layout.addWidget(self.gboxCheckTexel)
        self.gboxCheckTexel.setLayout(self.gboxCheckTexel_v_layout)
        
        #conclusion
        self.gboxTexConclusion.setLayout(self.gboxTexConclusion_v_layout)
        
        #conclusion area
        self.tabTex_v_layout.addWidget(self.gboxTexConclusion)
        

        #SIGNALS
        
        #Calculate Texel
        self.btnCalcTex.clicked.connect(self.btnCalcTexClicked)
        
        #SetTexel
        self.btnSetTex.clicked.connect(self.btnSetTexelClicked)
        
        #changes in texel
        self.edtCurTexel.editingFinished.connect(self.checkTexelValue)
        
         #changes in Tiny It
        self.edtTinyIt.textChanged.connect(self.tinyChanged)
        self.edtTinyIt.editingFinished.connect(self.tinyFinEdit)
        
        #changes in TinyPX
        self.edtTinyPX.editingFinished.connect(self.tinyPXFinEdit)
        
        self.btnCheckTexel.clicked.connect(self.btnCheckTexelClicked)
        
        self.btnCleanCheck.clicked.connect(self.btnCleanCheckClicked)
        
        self.spnDiff.editingFinished.connect(self.diffFinEdit)
        
        self.cboxTexRes.activated.connect(self.textureResChange)
        
        self.btnSelectTinyFace.clicked.connect(self.btnSelectTinyFacesClicked)
        self.btnSelectTinyUVShell.clicked.connect(self.btnSelectTinyUVShellsClicked)
        
        self.edtSetTex.editingFinished.connect(self.checkDesiredTexel)
        
        self.checkTexelValues()
        
        #arrays for mistakes
        self.tiny_uv_arr=[]
        self.tiny_geo_arr=[]
        
        self.btnSelectTinyFace.setDisabled(True)
        self.btnSelectTinyUVShell.setDisabled(True)
        
        self.checkSquareMap()
        
        self.lblInfo_01.setText("Texel operations not yet performed!")
        
        #lang selector
        current_languge = cfgl.configLoader()[14]
        self.txtbrowTexConclusion.setHtml( conclusion.texTabIntroConclusion(current_languge) )

    def showInfo(self, info_type, info_text):
        
        if info_type=="info":
            self.lblInfo_01.setText(info_text)
            self.lblInfo_01.setStyleSheet("background-color:#3D523D;")
            print "PolygonTools:", info_text
        
        if info_type=="warn":
            self.lblInfo_01.setText(info_text)
            self.lblInfo_01.setStyleSheet("background-color:#916666;")
            cmds.warning( "PolygonTools: " + info_text )

    #select tiny Faces    
    def btnSelectTinyFacesClicked (self):
        
        current_languge = cfgl.configLoader()[14]
        
        if len(self.tiny_geo_arr) == 1:
            try:
                cmds.select(self.tiny_geo_arr[0])
                cmds.modelEditor( modelPanel='modelPanel4', da="wireframe", grid=False, displayLights="default", cameras=False, activeView=True)
                self.showInfo ("info", "Tiny Faces was selected.")

                conclusion_text = conclusion.selectTinyConclusion(current_languge, "Face", True)
                self.txtbrowTexConclusion.setHtml(conclusion_text) 
                
            except:
                self.showInfo ("warn", "Can not select Tiny Faces")
                self.btnSelectTinyFace.setDisabled(True)
                self.btnSelectTinyFace.setText("Not checked yet")
                
                conclusion_text = conclusion.selectTinyConclusion(current_languge, "Face", False)
                self.txtbrowTexConclusion.setHtml(conclusion_text)                 
                
    #select tiny UV
    def btnSelectTinyUVShellsClicked (self):
        
        current_languge = cfgl.configLoader()[14]
        
        if len(self.tiny_uv_arr) == 1:
            try:
                maya.mel.eval('TextureViewWindow;')
                cmds.select(self.tiny_uv_arr[0])
                self.showInfo ("info", "Tiny UV Shells was selected.")

                conclusion_text = conclusion.selectTinyConclusion(current_languge, "UV", True)
                self.txtbrowTexConclusion.setHtml(conclusion_text) 
                
            except:
                self.showInfo ("warn", "Can not select Tiny UV Shells.")
                self.btnSelectTinyUVShell.setDisabled(True)
                self.btnSelectTinyUVShell.setText("Not checked yet")

                conclusion_text = conclusion.selectTinyConclusion(current_languge, "UV", False)
                self.txtbrowTexConclusion.setHtml(conclusion_text) 

    
    def textureResChange(self):
        path_config = cfgl.configLoader()[99:101]
        current_resolution_value = str(self.cboxTexRes.currentIndex())
        cfgl.ConfigWriter('Texel', 'Map_resolution', current_resolution_value, path_config[0], path_config[1])
        
        #check Square or Not
        self.checkSquareMap()   
        
    def diffFinEdit(self):
        #Write to config
        path_config = cfgl.configLoader()[99:101]
        current_diff_value = str(self.spnDiff.value())
        cfgl.ConfigWriter('In-Range', 'Difference', current_diff_value, path_config[0], path_config[1])
        
    def tinyPXFinEdit(self):
        #Write to config
        path_config = cfgl.configLoader()[99:101]
        current_tiny_value = self.edtTinyPX.text()
        cfgl.ConfigWriter('In-Range', 'Tiny UV', current_tiny_value, path_config[0], path_config[1])
        
    def checkTexelValue(self):
        try:
            self.lblInfo_01.setText("")
            
            #Write to config
            path_config = cfgl.configLoader()[99:101]
            current_texel_value = self.edtCurTexel.text()
            cfgl.ConfigWriter('In-Range', 'Texel', current_texel_value, path_config[0], path_config[1])
            
        except:
            self.showInfo ("warn", "Please input correct Integer value in range 1-10000. Now default value (256) was returned.")
            self.edtCurTexel.setText("256")
            
 
    def checkDesiredTexel(self):
        
        try:
            texel = (float(self.edtSetTex.text())/100)
            
            if (texel<0.01):
                self.setTexelWarningText()
            
            #Write to config
            path_config = cfgl.configLoader()[99:101]
            current_desired_texel = self.edtSetTex.text()
            cfgl.ConfigWriter('Texel', 'desired_texel', current_desired_texel, path_config[0], path_config[1])        
                         
        except:
            self.setTexelWarningText()        
        
    
    #Slider move
    def texelChanger(self):
        self.lblInfo_01.setText("")
     
    #problems with Tiny I Fixer   
    def tinyWarning(self):
        self.showInfo ("warn", "Please input correct Float value in range 0.0001-1000. Now default value (0.0001) was returned.")
        self.edtTinyIt.setText("0.0001")            
        
    def tinyChanged(self):
        try:
            tiny_it = float(self.edtTinyIt.text())
            
            if (tiny_it < 0.0001) or (tiny_it > 1000):
                self.tinyWarning()
        except:
            self.tinyWarning()
    
    def tinyFinEdit(self):
        try:
            tiny_it = float(self.edtTinyIt.text())
            
            if (tiny_it<0.0001) or (tiny_it>1000):
                self.tinyWarning()
            
            #Write to config
            path_config = cfgl.configLoader()[99:101]
            current_tinit_value = self.edtTinyIt.text()
            cfgl.ConfigWriter('In-Range', 'Tiny_it', current_tinit_value, path_config[0], path_config[1])
                            
        except:
            self.tinyWarning()
    
    
    #calc texel        
    def btnCalcTexClicked(self):
        
        selectedTextureIndex = int(self.cboxTexRes.currentIndex())
        selectedTextureArea = resolutionSelected(selectedTextureIndex)
        
        #randomPoly, uv_area[0], geo_area, cur_work_units, gp_ratio, texel, matrix            
        texelData = CalculateTexel(selectedTextureArea)
        
        #get current language
        current_languge = cfgl.configLoader()[14]
        
        if texelData != False:
        
            print "-----------------------------------------"
            print "     PolygonTools TEXEL STATISTICS"    
            print "-----------------------------------------"
    
            if texelData[1] == 0:
                print ("UV-Face Area: No UV-layout on selected face. Its problem!")  
            else:
                print ("UV-Face Area: "+ str(texelData[1]))  

            print ("Geo-Face Area: " + str(texelData[2]) +" "+ texelData[3] + u'\N{SUPERSCRIPT TWO}')     
            print ("Texture size: " + self.cboxTexRes.currentText() +" px") 
            print ("Texture area: " + str(selectedTextureArea) +" px")
        
            
            if (self.chkUseInUVI.isChecked()==True) and texelData[5] > 0.0:   
                self.edtCurTexel.setText(str(int(texelData[5])))        
            else:
                self.edtCurTexel.setText("1")
            
            if texelData[6] == 3:
                self.lblTexel.setText("Texel: " + str(int(texelData[5])) + " px/" + texelData[3])  
                self.lblTexel.setStyleSheet('background-color: black; padding: 5px;')  
            else:
                self.lblTexel.setText("Texel: " + str(int(texelData[5])) + " px/" + texelData[3] + " | Object with Scale transformation!")    
                self.lblTexel.setStyleSheet('background-color: #9e0b0f; padding: 5px;')
                print "ATTENTION! Object with Scale transformation!"

            print ""
                                                
            if texelData[0] == False:
                self.showInfo ("info", "Texel successfully calculated for selected polygon.")
                #set conclusion text
                conclusion_text = conclusion.calcTexelConclusion(current_languge, int(texelData[5]), True)
            else:
                self.showInfo ("warn", "Texel successfully calculated for random polygon.")
                #set conclusion text
                conclusion_text = conclusion.calcTexelConclusion(current_languge, int(texelData[5]), False) 
    
            #conclusion output
            self.txtbrowTexConclusion.setHtml(conclusion_text)        
            
            print "-----------------------------------------"    
        else:
            self.showInfo ("warn", "Can't Get Texel. Please select one Face.")
            self.lblTexel.setText("Texel:")
            self.lblTexel.setStyleSheet('background-color: black; padding: 5px;')  
            
            conclusion_text = conclusion.noSelection(current_languge, "check_texel")
            self.txtbrowTexConclusion.setHtml(conclusion_text) 

    #set texel
    def btnSetTexelClicked (self):
        
        SelectionData = gen_func.checkSelection()
        
        #shapes array
        SelectedShapes = SelectionData[0]

        current_languge = cfgl.configLoader()[14]
        
        self.checkDesiredTexel()
        
        if len(SelectedShapes) > 0:
            
            print""
            
            try:
                #get map res
                MapResValue = self.cboxTexRes.currentText()
                
                #get texel
                TexelValue = (str(float(self.edtSetTex.text())/100))
                
                for i in range(len(SelectedShapes)):
                    cmds.select(SelectedShapes[i])
                    #set texel 
                    maya.mel.eval('texSetTexelDensity ' + TexelValue + ' ' + MapResValue + ';')
                    print (gen_func.shortNamer(SelectedShapes[i]) + ". Texel has been set to " + str(float(TexelValue)*100) + " px/m for map size " + MapResValue + "x" + MapResValue + "px")
                
                print ""
                    
                #return selection
                cmds.select (SelectedShapes)
                
                uvOutsideData = gen_func.uvRangeStat(SelectedShapes)
                
                if uvOutsideData[1] != []:
                    shapesOutside = False
                else:
                    shapesOutside = True                                  
                                    
                #conclusion output
                conclusion_text = conclusion.setTexelConclusion(current_languge, int(self.edtSetTex.text()), shapesOutside, len(SelectedShapes))
                self.txtbrowTexConclusion.setHtml(conclusion_text)        
                
                print ""                                
                
                LongText = ("The number of objects on which the texel is changed: " + str(len(SelectedShapes)) + "\n" + "Texel has been set to " + str(float(TexelValue)*100) + " px/m for map size " + MapResValue + "x" + MapResValue + "px")
                self.showInfo("info", LongText)
            except:
                self.setTexelWarningText()
                            
        else:
            self.showInfo("warn", "Can't Set Texel. Please select mesh object in Object Mode.")
            conclusion_text = conclusion.noSelection(current_languge, "set_texel")
            self.txtbrowTexConclusion.setHtml(conclusion_text) 


    def btnCheckTexelClicked(self):
        
        GreenBox =  ("<font color='#80ff80'>" + u'\N{BLACK SQUARE}' + "</font> In-Range: ")
        BlueBox =  (u'\N{BOX DRAWINGS LIGHT VERTICAL}' + " <font color='#80c0ff'>" + u'\N{BLACK SQUARE}' + "</font> Streched: ")
        RedBox =  (u'\N{BOX DRAWINGS LIGHT VERTICAL}' + "<font color='#ffc0c0'>" + u'\N{BLACK SQUARE}' + "</font> Compressed: ")

        self.lblInfo_01.setText("")
        self.checkTexelValue()
        
        self.btnSelectTinyUVShell.setDisabled(True)
        self.btnSelectTinyUVShell.setText("Not checked yet")
        
        self.btnSelectTinyFace.setDisabled(True)
        self.btnSelectTinyFace.setText("Not checked yet")
        
        SelectionData = gen_func.checkSelection()
        
        #shapes array
        selectedShapes = SelectionData[0]

        current_languge = cfgl.configLoader()[14]        
               
        if len(selectedShapes) > 0:
            try:              
                all_sel_obj = cmds.ls ( selection=True, objectsOnly=True, long=1, shortNames=1 )    

                #total polygons
                totalpoly = cmds.polyEvaluate( face=True )
                
                #set range from 0 to max polycount            
                self.pbChekProgress.setRange ( 0, 100 )
                self.pbChekProgress.setValue(0)
                
                #turn on vertex color
                for i in range(len(selectedShapes)):
                    cmds.polyColorPerVertex (selectedShapes[i], colorDisplayOption=1 )
                
                #get selected texture
                selected_texture_index = int(self.cboxTexRes.currentIndex())
                
                print "-----------------------------------------"
                print " PolygonTools. Check Texle Density"
                print "-----------------------------------------"
                
                current_time = time.strftime("%H:%M:%S ", time.localtime())
                print "Check Start at", current_time
                
                print "" 

                #texture area
                selected_texture_area = resolutionSelected(selected_texture_index)
                #print "Selected Texture Area:", selected_texture_area 
                
                #get curent texel
                current_texel = float(self.edtCurTexel.text())
                                
                #get curent diff
                DifferenceMargin = float(self.spnDiff.value())
                                                            
                #get current tiny
                tiny_polygon_area = float(self.edtTinyIt.text())
                
                
                CurrentTinyUVValue = int(self.edtTinyPX.text())
                print "Current Tiny UV:", CurrentTinyUVValue
                
                SelectedResolution = self.cboxTexRes.currentText()

                #main func
                CheckTexelData = CheckTexel (selectedShapes, selected_texture_index, current_texel, DifferenceMargin, tiny_polygon_area, SelectedResolution, CurrentTinyUVValue, True)
                
                #global_inrange_arr, global_streched_arr, global_compressed_arr, global_tiny_uv_arr, global_tiny_geo_arr
                
                correct=[]
                streched=[]
                compressed=[]
                
                self.tiny_uv_arr = []
                self.tiny_geo_arr = []
                
                for k in range(len(selectedShapes)):                
                    for i in range(len(CheckTexelData)):
                        if i == 0:
                            correct.append(len(CheckTexelData[i][k]))
                        if i == 1:                        
                            streched.append(len(CheckTexelData[i][k]))
                        if i == 2:
                            compressed.append(len(CheckTexelData[i][k]))
                        if i == 3:
                            if CheckTexelData[i][k] != []:
                                self.tiny_uv_arr.append(CheckTexelData[i][k])                            
                        if i == 4:
                            if CheckTexelData[i][k] != []:
                                self.tiny_geo_arr.append(CheckTexelData[i][k])                
                                                
                self.pbChekProgress.setValue(100)
                
                TinyFace = False
                TinyUV = False
                
                if self.tiny_uv_arr != [] and len(selectedShapes) == 1:
                    self.btnSelectTinyUVShell.setDisabled(False)
                    self.btnSelectTinyUVShell.setText("Select " + str(len(self.tiny_uv_arr[0])) + " tiny UV Shell(s)")
                    TinyUV = True
                elif self.tiny_uv_arr != []:
                    self.btnSelectTinyUVShell.setText("Tiny UV Shells on " + str(len(self.tiny_uv_arr)) + " objects")
                    TinyUV = True
                
                if self.tiny_geo_arr != [] and len(selectedShapes) == 1:
                    self.btnSelectTinyFace.setDisabled(False)
                    self.btnSelectTinyFace.setText("Select " + str(len(self.tiny_geo_arr[0])) + " tiny face(s)")
                    TinyFace = True
                elif self.tiny_geo_arr != []:
                    self.btnSelectTinyFace.setText("Tiny faces on " + str(len(self.tiny_geo_arr)) + " objects")
                    TinyFace = True

                
                print ""
                                                    
                LongText = ("Check texel density complete! See log for details." +"\n" + "Number of checked objects: " + str(len(selectedShapes)))
                self.showInfo("info", LongText)                

                print ""

                self.lblInRangeInfo.setText(GreenBox + str(sum(correct)) + RedBox + str(sum(streched)) + BlueBox + str(sum(compressed)))
                print ("Correct: " + str(sum(correct)) + " | Streched: " + str(sum(streched)) + " | Compressed: " + str(sum(compressed)))

                print ""
                
                print "Objects with Tiny geometry area:", len(self.tiny_geo_arr)
                
                print "Objects with Tiny UV Shells:", len(self.tiny_uv_arr)
                            
                print ""
                
                current_time = time.strftime("%H:%M:%S ", time.localtime())
                print "Check complete at", current_time 
                print "-----------------------------------------"

                conclusion_text = conclusion.checkTexelConclusion(current_languge, DifferenceMargin, correct, streched, compressed, TinyUV, TinyFace)
                self.txtbrowTexConclusion.setHtml(conclusion_text) 
                
                cmds.select( selectedShapes )
            
            except:
                self.showInfo("warn", "Error. Can't Check Texel. Please select mesh object in Object Mode.")
                self.pbChekProgress.setValue(0)
                conclusion_text = conclusion.noSelection(current_languge, "set_texel")
                self.txtbrowTexConclusion.setHtml(conclusion_text)

        else:
            self.showInfo("warn", "Can't Check Texel. Please select mesh object in Object Mode.")
            conclusion_text = conclusion.noSelection(current_languge, "check_texel")
            self.txtbrowTexConclusion.setHtml(conclusion_text) 
            
    
    
    def btnCleanCheckClicked(self):
        
        SelectionData = gen_func.checkSelection()
                
        #shapes array
        selectedShapes = SelectionData[0]

        current_languge = cfgl.configLoader()[14]        
        
        if len(selectedShapes) > 0:
            try:
                for i in range(len(selectedShapes)):
                    CurrentColorSet = cmds.polyColorSet(selectedShapes[i], q=True, currentColorSet=True)
                    if CurrentColorSet != None:
                        cmds.polyColorSet (selectedShapes[i], delete=True )
                        print gen_func.shortNamer(selectedShapes[i]), "was cleaned."         

                self.showInfo("info", "Check Texel Density results have been cleared!")
                self.lblInRangeInfo.setText("Previous check results have been cleared!")
                
                self.btnSelectTinyUVShell.setText("Not checked yet")
                self.btnSelectTinyFace.setText("Not checked yet")
                
                self.btnSelectTinyFace.setDisabled(True)
                self.btnSelectTinyUVShell.setDisabled(True)
                
                self.tiny_uv_arr=[]
                self.tiny_geo_arr=[]
                
                self.pbChekProgress.setValue(0)
                cmds.select( selectedShapes )
                
                conclusion_text = conclusion.CleanCheckClicked(current_languge, True)
                self.txtbrowTexConclusion.setHtml(conclusion_text) 
            except:
                self.showInfo("warn", "There is nothing to clean! Try to clean after checking.")
                
                conclusion_text = conclusion.CleanCheckClicked(current_languge, False)
                self.txtbrowTexConclusion.setHtml(conclusion_text) 
        else:
            self.showInfo("warn", "Can't clean check texel density results. Please select already checked mesh object in Object Mode.")
            
            conclusion_text = conclusion.noSelection(current_languge, "clean_check")
            self.txtbrowTexConclusion.setHtml(conclusion_text) 

    def checkTexelValues(self):
        
        #current values
        current_texel = self.edtCurTexel.text()
        current_diff = str(self.spnDiff.value())
        current_tinyit = self.edtTinyIt.text()
        current_tinypx = self.edtTinyPX.text()
        current_desired_texel = self.edtSetTex.text()
        
        #load data from config
        data_from_config = cfgl.configLoader()[0:12]
        
        #values from config
        config_resolution = int(data_from_config[0])
        config_texel = data_from_config[1] 
        config_diff = data_from_config[2]
        config_tinyit = data_from_config[3]
        config_tinypx = data_from_config[4]
        config_desired_texel = data_from_config[11]
                        
        #compare values
        self.cboxTexRes.setCurrentIndex(config_resolution)
        
        #change values if need
        
        #setcurtexel
        if current_texel != config_texel:
             self.edtCurTexel.setText(config_texel)
        
        #set diff
        if current_diff != config_diff:
             self.spnDiff.setValue(int(config_diff))

        #set tinyit
        if current_tinyit != config_tinyit:
             self.edtTinyIt.setText(config_tinyit)

        #set tinypx
        if current_tinypx != config_tinypx:
             self.edtTinyPX.setText(config_tinypx)
        
        #set desired_texel     
        if current_desired_texel != config_desired_texel:
             self.edtSetTex.setText(config_desired_texel)
    
            
    def setTexelWarningText(self):
            self.showInfo("warn", "Please input correct Integer value in range 1-9999. Now default value (400) was returned.")
            self.edtSetTex.setText("400")
            
    def checkSquareMap(self):
        try:
            mapres = int(self.cboxTexRes.currentText())
            
            self.btnSetTex.setEnabled(True)
            self.edtSetTex.setEnabled(True)
            self.lblMapSize.setText("Map size: " + self.cboxTexRes.currentText() + "px")
        except:
            self.btnSetTex.setEnabled(False)
            self.edtSetTex.setEnabled(False)
            self.lblMapSize.setText("Map size: Please select square map! Now it\'s " + self.cboxTexRes.currentText())
            
def CalculateTexel(selectedTextureArea):

    #getselection
    pt_selection = cmds.ls( selection=True, long=True  )
    
    if ".f[" in pt_selection[0]: #if face selected
        SelName = pt_selection[0] 
        head, sep, tail = SelName.partition('.') #find transform name - head 
        pt_selection = []
        pt_selection.append(head)
        ParentsArray = pt_selection[0].split('|')[1:]
        TransformNameArray = ['|'.join(ParentsArray[:i]) for i in xrange(1, 1 + len(ParentsArray))]
    else:        
        #get all array
        ParentsArray = cmds.ls(pt_selection, long=True)[0].split('|')[1:]
        #get split names
        TransformNameArray = ['|'.join(ParentsArray[:i]) for i in xrange(1, 1 + len(ParentsArray))]

    try:
        transform_matrix = []
        TransformMatrixArray = []
        
        #get scale transform
        for k in range(len(TransformNameArray)):                    
            transform_matrix = []
            transform_matrix = cmds.xform(TransformNameArray[k], q=True, scale=True, relative=True)
            TransformMatrixArray.append(sum(transform_matrix))
    except:
        transform_matrix = 0
        
    try:
        transform_matrix = sum(TransformMatrixArray)/len(TransformMatrixArray) #avg Transform value
    except:
        transform_matrix = 0

    #Selected Face UV area
    uv_area = cmds.polyEvaluate( ufa=True )
    
    #random polygon selection attribute
    randomPoly = False

    try:    
        #try random polygon texel
        if uv_area == []:
            current_shape_poly = cmds.polyEvaluate(pt_selection, f=True ) 
            random_poly_number = str(random.randrange(0, current_shape_poly, 1))
            cmds.select(pt_selection[0] + '.f[' + random_poly_number + ']')
            uv_area = cmds.polyEvaluate( ufa=True ) 
            #if no UV
            if uv_area == []:
                uv_area = [0]
            print "PolygonTools: Attention! Random polygon selected for checking texel, #", random_poly_number
            randomPoly = True                
        
        #Selected Face Geo area
        geo_area_raw = cmds.polyEvaluate( fa=True )
        
        cur_work_units = cmds.currentUnit(query=True)
        
        #Depends of Units system         
        geo_area = (geo_area_raw[0]/10000)    
    
        #geometry-poly ration
        gp_ratio = math.sqrt(uv_area[0]/geo_area) 
                         
        #texel calculation
        texel = math.ceil (gp_ratio*(math.sqrt(selectedTextureArea)))
             
        return randomPoly, uv_area[0], geo_area, cur_work_units, gp_ratio, texel, transform_matrix
    except:
        cmds.warning("For calculate texel density please Freeze Transformations and Delete History. Select only one face on one object!")
        return False

def resolutionSelected(selected_texture_index):
    
    if selected_texture_index == 0:
        selected_texture_area = pow(64,2)
        
    if selected_texture_index == 1:
        selected_texture_area=pow(128,2)
        
    if selected_texture_index == 2:
        selected_texture_area=256*128
        
    if selected_texture_index == 3:
        selected_texture_area=pow(256,2)
        
    if selected_texture_index == 4:
        selected_texture_area=512*256
        
    if selected_texture_index == 5:
        selected_texture_area=pow(512,2)
        
    if selected_texture_index == 6:
        selected_texture_area=1024*512
        
    if selected_texture_index == 7:
        selected_texture_area=pow(1024,2)
        
    if selected_texture_index == 8:
        selected_texture_area=2048*1024
        
    if selected_texture_index == 9:
        selected_texture_area=pow(2048,2)
        
    if selected_texture_index == 10:
        selected_texture_area=4096*2048
        
    if selected_texture_index == 11:
        selected_texture_area=pow(4096,2)
        
    if selected_texture_index == 12:
        selected_texture_area=pow(8192,2)
    
    return selected_texture_area
    
        
def CheckTexel(selectedShapes, selectedTextureIndex, CurrentTexel, differenceMargin, tinyPolygonArea, textureResolution, currentTinyValue, Colorize):


    PTProgressWindow = cmds.window(title="PolygonTools Progress Bar", minimizeButton=False, maximizeButton=False)
    cmds.columnLayout(PTProgressWindow )

    PolyCount = cmds.polyEvaluate(selectedShapes, f=True )
    progressControl = cmds.progressBar(maxValue=PolyCount, width=300)
    cmds.showWindow( PTProgressWindow )

    #texture area
    selectedTextureArea = resolutionSelected(selectedTextureIndex)
    print "Selected Texture Area:", selectedTextureArea
    
    #distortion value
    DistortionValue = (CurrentTexel/100)*differenceMargin
    print "Tolerance from the current texel value:", DistortionValue 
    
    print ""
    
    #hi texel range
    HiTexelValue = CurrentTexel + DistortionValue
    print "Highest texel:", HiTexelValue
    
    print "Current texel:", CurrentTexel
    
    #low texel range
    LowTexelValue = CurrentTexel - DistortionValue
    print "Lowest texel:", LowTexelValue
    
    print ""

    #get 1 pixel area for current map
    tinyPixelValue = Decimal(1.0/selectedTextureArea)
    #print "tinyPixelValue", tinyPixelValue     
    print ("1 pixel area for " + textureResolution + " texture is " + str(tinyPixelValue )) 

    currentTinyHeightWidth  = ((1.0/math.sqrt(selectedTextureArea)*currentTinyValue))
    print "Tiny Height or Width:", currentTinyHeightWidth
    
    print ""
    
    #global arrays
    global_inrange_arr =[]
    global_streched_arr =[]
    global_compressed_arr =[]
    global_tiny_uv_arr = []
    global_tiny_geo_arr = []        
    
        
    for i in range(len(selectedShapes)):
        
        #get polycount
        CurrentObjectPolycount = cmds.polyEvaluate(selectedShapes[i], face=True )

        #arrays for polygons            
        in_range_arr = []
        streched_arr = []
        compressed_arr = []
        tiny_uv_arr = []
        tiny_geo_arr = []        

        for l in range(0, CurrentObjectPolycount):
            
            #select polygon
            cmds.select(selectedShapes[i] + '.f['+ str(l) +']')
            
            #selected face name
            SelectedFaceName = (selectedShapes[i] + '.f['+ str(l) +']')
            
            #get uv area
            SelectedFaceUVArea = cmds.polyEvaluate( ufa=True )

            if SelectedFaceUVArea == []:
                SelectedFaceUVArea = [0]
            
            #condert to decimal value
            DecimalUVArea = Decimal(SelectedFaceUVArea[0])
             
            #get geo area
            GeoAreaRaw = cmds.polyEvaluate( fa=True )
            GeoArea = (GeoAreaRaw[0]/10000)              
            
            #get element bbox
            UVBbox = cmds.polyEvaluate( boundingBoxComponent2d=True )
            
            #get width height
            HeightUVElement = UVBbox[0][1] - UVBbox[0][0]
            WidthUVElement = UVBbox[1][1] - UVBbox[1][0]
                
            #check area and W and H of uv and compare with user value
            if (DecimalUVArea < tinyPixelValue) or (HeightUVElement <= currentTinyHeightWidth ) or (WidthUVElement <= currentTinyHeightWidth):
                tiny_uv_arr.append (SelectedFaceName)

            #check geo area with user value
            if GeoArea <= tinyPolygonArea:
                tiny_geo_arr.append (SelectedFaceName)
            
            #get gpratio
            try:
                UVGeoRatio = math.sqrt(SelectedFaceUVArea[0]/GeoArea)
            except:
                UVGeoRatio = 0
                cmds.warning("PolygonTools. Problem with geometry area of selected face!")

            #get texel
            TexelValue = math.ceil (UVGeoRatio*(math.sqrt(selectedTextureArea)))
            
            #texel equal Inrange
            if (TexelValue <= HiTexelValue) and (TexelValue >= LowTexelValue):
                in_range_arr.append(SelectedFaceName)                
            
            #texel bigger Streched   
            if TexelValue > HiTexelValue:
                streched_arr.append(SelectedFaceName)
            
            #texel smaller Compressed
            if TexelValue < LowTexelValue:
                compressed_arr.append(SelectedFaceName)
            
            cmds.progressBar(progressControl, edit=True, step=1)
        
        print i, " - Information for", gen_func.shortNamer(selectedShapes[i])

        #paint polygons
        if Colorize == True:                                
            try: 
                cmds.select(in_range_arr)
                cmds.polyColorPerVertex ( rgb = (0.25, 1.0, 0.25) )                
            except:
                pass
            
            try:
                cmds.select(streched_arr)
                cmds.polyColorPerVertex ( rgb = (1.0, 0.5, 0.5) )                
            except:
                pass   
    
            try:
                cmds.select(compressed_arr)
                cmds.polyColorPerVertex ( rgb = (0.25, 0.5, 1.0) )
            except:
                pass
                
        try:
            print "In-Range:", str(len(in_range_arr))
        except:
            print ("In-Range: 0")
            
        try:
            print "Streched:", str(len(streched_arr))
        except:
            print ("Streched: 0")

        try:
            print "Compressed:", str(len(compressed_arr))
        except:
            print ("Compressed: 0")

        try:
            print "Tiny UV Shells:", str(len(tiny_uv_arr))
        except:
            print ("Tiny UV Shells: 0")

        try:
            print "Tiny Faces:", str(len(tiny_geo_arr))
        except:
            print ("Tiny Faces: 0")
                    
        print ""        
        
        #global arrays
        global_inrange_arr.append ( in_range_arr )
        global_streched_arr.append ( streched_arr )
        global_compressed_arr.append ( compressed_arr )        
        global_tiny_uv_arr.append ( tiny_uv_arr )
        global_tiny_geo_arr.append ( tiny_geo_arr )         


    cmds.deleteUI( PTProgressWindow , window=True ) 

    return  global_inrange_arr, global_streched_arr, global_compressed_arr, global_tiny_uv_arr, global_tiny_geo_arr