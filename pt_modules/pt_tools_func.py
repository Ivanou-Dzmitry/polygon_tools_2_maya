# This Python file uses the following encoding: utf-8
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
import maya.mel
import math 

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

#GUI    
class PT_Toools_Tab (QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent=parent)
        
        #set layoit
        self.tabTool_v_layout = QVBoxLayout(self)
        self.tabTool_v_layout.setAlignment(Qt.AlignTop)
        self.tabTool_v_layout.setContentsMargins(0,10,0,10)
        self.tabTool_v_layout.setSpacing(5)
        
        currentDir = os.path.dirname(__file__)
        try:
            iconFBXExport  = QPixmap(currentDir +"/icons/fbxexport_icon.png")
            iconDelMat  = QPixmap(currentDir +"/icons/delete_mat_icon.png")
            iconMateMat  = QPixmap(currentDir +"/icons/mate_mat_icon.png")
            iconGlossMat  = QPixmap(currentDir +"/icons/gloss_mat_icon.png")
            iconIntersect  = QPixmap(currentDir +"/icons/intersection_icon.png")
            iconRetop  = QPixmap(currentDir +"/icons/retop_icon.png")
            iconLod  = QPixmap(currentDir +"/icons/lod_check_icon.png")
            iconRendPrev  = QPixmap(currentDir +"/icons/render_prev_icon.png")            
        except:
            cmds.warning( "PolygonTools: Can't load icons for Tools Tab! Check icon files in pt_modules/icons directory.")
        
        
        #label for info
        self.lblInfo_01 = QLabel("Select an object and click on the necessary tool.")
        self.lblInfo_01.setMargin(2)
        
        #Mat Tools Group
        self.gboxMats = QGroupBox("Materials")
        self.gboxMats.setMaximumWidth(340)
        self.gboxMats.setMaximumHeight(100)
        self.gboxMats_h_layout = QHBoxLayout()
        
        self.btnDelMat = QPushButton("Delete")
        self.btnDelMat.setMinimumWidth(100)
        self.btnDelMat.setIcon(iconDelMat)

        self.btnGlossMat = QPushButton("Gloss")
        self.btnGlossMat.setMinimumWidth(50)
        self.btnGlossMat.setIcon(iconGlossMat)

        self.btnMateMat = QPushButton("Mate")
        self.btnMateMat.setMinimumWidth(50)
        self.btnMateMat.setIcon(iconMateMat)
        
        #add elements
        self.gboxMats_h_layout.addWidget(self.btnDelMat)
        self.gboxMats_h_layout.addWidget(self.btnGlossMat)
        self.gboxMats_h_layout.addWidget(self.btnMateMat)
        
        #st layout
        self.gboxMats.setLayout(self.gboxMats_h_layout)
        
        #Export Tools Group
        self.gboxExport = QGroupBox("Export")
        self.gboxExport.setMaximumWidth(340)
        self.gboxExport.setMaximumHeight(100)
        self.gboxExport_h_layout = QHBoxLayout()
        self.gboxExport_h_layout.setAlignment(Qt.AlignLeft)
        
        self.btnFBXExp = QPushButton("To FBX")
        self.btnFBXExp.setMinimumWidth(75)
        self.btnFBXExp.setMaximumWidth(75)
        self.btnFBXExp.setIcon(iconFBXExport)
        
        self.gboxExport_h_layout.addWidget(self.btnFBXExp)
        
        self.gboxExport.setLayout(self.gboxExport_h_layout)
        
        #LOD Group
        self.gboxLOD = QGroupBox("LOD")
        self.gboxLOD.setMaximumWidth(340)
        self.gboxLOD.setMaximumHeight(220)
        self.gboxLOD.setMinimumHeight(220)
        self.gboxLOD_h_layout = QHBoxLayout()
        self.gboxLOD_h_layout.setSizeConstraint(QLayout.SetMinimumSize)
        
        
        #left column
        self.gboxLOD_v_layout1 = QVBoxLayout()
        self.gboxLOD_v_layout1.setAlignment(Qt.AlignLeft)
        self.gboxLOD_v_layout1.setAlignment(Qt.AlignTop)

        #Rightn column
        self.gboxLOD_v_layout2 = QVBoxLayout()
        self.gboxLOD_v_layout2.setAlignment(Qt.AlignLeft)
        self.gboxLOD_v_layout2.setAlignment(Qt.AlignTop)

        #h for emulator
        self.gboxLOD_h_layout1 = QHBoxLayout()
        self.gboxLOD_h_layout1.setAlignment(Qt.AlignLeft)
        
        #h for button
        self.gboxLOD_h_layout2 = QHBoxLayout()
        self.gboxLOD_h_layout2.setAlignment(Qt.AlignRight)
        self.gboxLOD_h_layout2.setContentsMargins(0,66,0,0)
        

        
        self.lblDist = QLabel("Switch range")
        self.lblLOD0 = QLabel("LOD0")
        self.lblLOD4 = QLabel("LOD4")
        self.lblDistEmulation = QLabel("Virtual Distance")
        
        
        self.sldLOD = QSlider()
        self.sldLOD.setOrientation(Qt.Horizontal)
        self.sldLOD.setMinimumHeight(20)
        self.sldLOD.setMinimum(0)
        self.sldLOD.setMaximum(4)
        self.sldLOD.setTickInterval(1)
        self.sldLOD.setValue(0)
        self.sldLOD.setEnabled(False)

        self.lblLodDist = QLabel("Distance:")
        self.lblLodDist.setMinimumWidth(100)
        
        self.btnLODcheck = QToolButton()
        self.btnLODcheck.setText("LOD Check")
        self.btnLODcheck.setIcon(iconLod)
        self.btnLODcheck.setMinimumWidth(75)
        self.btnLODcheck.setCheckable(True)
        
        if cmds.objExists('LOD_Group_PT'):
            self.btnLODcheck.setChecked(True)            
            cmds.headsUpDisplay('distanceHUD', label="LOD Distance:", command=self.distanceChecker, attachToRefresh=True, visible=True, section=1, block=0, labelFontSize='large')
            self.sldLOD.setEnabled(True)        
        
        self.spnLOD1 = QSpinBox()
        self.spnLOD1.setFixedWidth(90)
        self.spnLOD1.setMinimum(5)
        self.spnLOD1.setMaximum(200)
        self.spnLOD1.setValue(10)
        self.spnLOD1.setSingleStep(5)
        self.spnLOD1.setPrefix("LOD1: ")
        self.spnLOD1.setSuffix("m")

        self.spnLOD2 = QSpinBox()
        self.spnLOD2.setFixedWidth(90)
        self.spnLOD2.setMinimum(10)
        self.spnLOD2.setMaximum(400)
        self.spnLOD2.setValue(20)
        self.spnLOD2.setSingleStep(10)
        self.spnLOD2.setPrefix("LOD2: ")
        self.spnLOD2.setSuffix("m")

        self.spnLOD3 = QSpinBox()
        self.spnLOD3.setFixedWidth(90)
        self.spnLOD3.setMinimum(20)
        self.spnLOD3.setMaximum(600)
        self.spnLOD3.setValue(30)
        self.spnLOD3.setSingleStep(10)
        self.spnLOD3.setPrefix("LOD3: ")
        self.spnLOD3.setSuffix("m")

        self.spnLOD4 = QSpinBox()
        self.spnLOD4.setFixedWidth(90)
        self.spnLOD4.setMinimum(30)
        self.spnLOD4.setMaximum(800)
        self.spnLOD4.setValue(40)
        self.spnLOD4.setSingleStep(10)
        self.spnLOD4.setPrefix("LOD4: ")
        self.spnLOD4.setSuffix("m")
        
        self.gboxLOD_v_layout1.addWidget(self.lblLodDist)
                
        self.gboxLOD_v_layout1.addWidget(self.lblDist)
        self.gboxLOD_v_layout1.addWidget(self.spnLOD1)
        self.gboxLOD_v_layout1.addWidget(self.spnLOD2)
        self.gboxLOD_v_layout1.addWidget(self.spnLOD3)
        self.gboxLOD_v_layout1.addWidget(self.spnLOD4)
        
        self.gboxLOD_v_layout2.addWidget(self.lblDistEmulation)
        self.gboxLOD_h_layout1.addWidget(self.lblLOD0)
        self.gboxLOD_h_layout1.addWidget(self.sldLOD)
        self.gboxLOD_h_layout1.addWidget(self.lblLOD4)
        
        self.gboxLOD_h_layout2.addWidget(self.btnLODcheck)
        
        self.gboxLOD_v_layout2.addLayout(self.gboxLOD_h_layout1)
        self.gboxLOD_v_layout2.addLayout(self.gboxLOD_h_layout2)
        
        self.gboxLOD_h_layout.addLayout(self.gboxLOD_v_layout1)
        self.gboxLOD_h_layout.addLayout(self.gboxLOD_v_layout2)
        
        self.gboxLOD.setLayout(self.gboxLOD_h_layout)
        
        #Intersect
        self.gboxIntersect = QGroupBox("Check Intersection")        
        self.gboxIntersect.setMaximumWidth(340)
        self.gboxIntersect_h_layout = QHBoxLayout()
        self.gboxIntersect_h_layout.setAlignment(Qt.AlignLeft)
        
        
        #Intersect
        self.gboxRetopo = QGroupBox("Retopology")
        self.gboxRetopo.setMaximumWidth(340)
        self.gboxRetopo_h_layout = QHBoxLayout()
        self.gboxRetopo_h_layout.setAlignment(Qt.AlignLeft)

        #Common Tools Group
        self.gboxCommon = QGroupBox("Common")
        self.gboxCommon.setMaximumWidth(340)
        self.gboxCommon.setMaximumHeight(100)
        self.gboxCommon_v_layout = QVBoxLayout()
        
        self.btnPrevRend = QPushButton("Render Preview")
        self.btnPrevRend.setIcon(iconRendPrev)        
        self.btnPrevRend.setMinimumWidth(110)
        self.btnPrevRend.setMaximumWidth(110)
                
        #intersect gui
        self.lblFlyDist = QLabel("Depth (mm): ")
        self.lblFlyDist.setMaximumWidth(65)
        self.edtFlyDist = QLineEdit()
        self.edtFlyDist.setMaxLength(2)
        self.edtFlyDist.setMaximumWidth(40)

        self.btnCheckFly = QToolButton()
        self.btnCheckFly.setText("Check")
        self.btnCheckFly.setStyleSheet("background-color:#5c4553;")
        self.btnCheckFly.setIcon(iconIntersect)
        self.btnCheckFly.setMaximumWidth(65)
        self.btnCheckFly.setCheckable(True)

        if cmds.objExists('pt_flying_edges'):
            self.btnCheckFly.setChecked(True)
        else:
            self.btnCheckFly.setChecked(False)
        
        self.com_h_layout_01 = QHBoxLayout()
        self.com_h_layout_01.setAlignment(Qt.AlignLeft)
        self.com_h_layout_01.setContentsMargins(0,0,0,0)
        self.com_h_layout_01.setSpacing(10)

        self.gboxCommon_v_layout.addWidget(self.btnPrevRend)
        
        self.gboxIntersect_h_layout.addWidget(self.lblFlyDist)
        self.gboxIntersect_h_layout.addWidget(self.edtFlyDist)
        self.gboxIntersect_h_layout.addWidget(self.btnCheckFly)
        
        self.gboxCommon_v_layout.addLayout(self.com_h_layout_01)
        
        self.gboxCommon.setLayout(self.gboxCommon_v_layout)
        self.gboxIntersect.setLayout(self.gboxIntersect_h_layout)
        
        #Retopo gui
        self.lblTargFaceCount = QLabel("Target Face Count: ")
        self.lblTargFaceCount.setMaximumWidth(100)
        self.edtTargFaceCount = QLineEdit()
        self.edtTargFaceCount.setText("100")
        self.edtTargFaceCount.setMaxLength(6)
        self.edtTargFaceCount.setMaximumWidth(55)
        self.btnSetFaceCount = QPushButton("Set")
        self.btnSetFaceCount.setIcon(iconRetop)
        self.btnSetFaceCount.setStyleSheet("background-color:#454e5c;")
        self.btnSetFaceCount.setMaximumWidth(65)

        self.gboxToolConclusion = QGroupBox("Conclusion")
        self.gboxToolConclusion.setMaximumWidth(340)
        self.gboxToolConclusion.setMinimumHeight(170)
        self.gboxToolConclusion_v_layout = QVBoxLayout()        

        #conclusion text here
        self.txtbrowToolConclusion = QTextBrowser()
        self.txtbrowToolConclusion.setHtml("")

        self.gboxToolConclusion_v_layout.addWidget(self.txtbrowToolConclusion) 

        self.gboxRetopo_h_layout.addWidget(self.lblTargFaceCount)
        self.gboxRetopo_h_layout.addWidget(self.edtTargFaceCount)
        self.gboxRetopo_h_layout.addWidget(self.btnSetFaceCount)
        
        self.gboxRetopo.setLayout(self.gboxRetopo_h_layout)
        
        #Add Base elements
        self.tabTool_v_layout.addWidget(self.lblInfo_01)        
        self.tabTool_v_layout.addWidget(self.gboxMats)
        self.tabTool_v_layout.addWidget(self.gboxExport)
        self.tabTool_v_layout.addWidget(self.gboxLOD)
        self.tabTool_v_layout.addWidget(self.gboxIntersect)
        self.tabTool_v_layout.addWidget(self.gboxRetopo)
        self.tabTool_v_layout.addWidget(self.gboxCommon)      

        #conclusion
        self.gboxToolConclusion.setLayout(self.gboxToolConclusion_v_layout)
        
        #conclusion area
        self.tabTool_v_layout.addWidget(self.gboxToolConclusion)

        #signals
        self.btnDelMat.clicked.connect(self.btnDelMatClicked)
        self.btnGlossMat.clicked.connect(self.btnGlossMatClicked)        
        self.btnMateMat.clicked.connect(self.btnMateMatClicked)    
        self.btnFBXExp.clicked.connect(self.btnFBXExpClicked)
        self.btnLODcheck.clicked.connect(self.btnLODcheckClicked)  
        
        self.spnLOD1.editingFinished.connect(self.lod1FinEdit)
        self.spnLOD2.editingFinished.connect(self.lod2FinEdit)
        self.spnLOD3.editingFinished.connect(self.lod3FinEdit)
        self.spnLOD4.editingFinished.connect(self.lod4FinEdit)
        
        #Change lod Slider
        self.sldLOD.sliderReleased.connect(self.currentLOD)
        self.sldLOD.valueChanged.connect(self.lodSwitcher)
        self.sldLOD.sliderPressed.connect(self.lodsldPressed)
        
        self.btnPrevRend.clicked.connect(self.btnPrevRendClicked)
        
        self.btnCheckFly.clicked.connect(self.btnCheckFlyClicked)
        
        self.edtFlyDist.editingFinished.connect(self.saveIntersetValue)
        
        self.edtTargFaceCount.editingFinished.connect(self.saveRetopoValue)
        
        self.btnSetFaceCount.clicked.connect(self.btnSetFaceCountClicked)

        #intro text
        current_languge = cfgl.configLoader()[14]
        self.txtbrowToolConclusion.setHtml( conclusion.toolTabIntroConclusion(current_languge) )          
        
        self.checkLODValues()
        
        global sldPressed
        
        sldPressed = ''
        
        self.checkToolsValues()
        
    
    def showInfo(self, info_type, info_text):
        
        if info_type=="info":
            self.lblInfo_01.setText(info_text)
            self.lblInfo_01.setStyleSheet("background-color:#3D523D;")
            print "PolygonTools:", info_text
        
        if info_type=="warn":
            self.lblInfo_01.setText(info_text)
            self.lblInfo_01.setStyleSheet("background-color:#916666;")
            cmds.warning( "PolygonTools: " + info_text )

        if info_type=="lod":
            self.lblInfo_01.setText(info_text)
            self.lblInfo_01.setStyleSheet("background-color:#3D523D;")
            
        if info_type=="fin":
            self.lblInfo_01.setText(info_text)
            self.lblInfo_01.setStyleSheet("background-color:#9E557A;")
            print "PolygonTools:", info_text
            
  
    #delete material    
    def btnDelMatClicked (self):
        
        current_languge = cfgl.configLoader()[14]        
        
        SelectionData = gen_func.checkSelection()
        
        SelectedShapes = SelectionData[0]

        if len(SelectedShapes) > 0:

            deleteMaterial(SelectedShapes)
            
            cmds.select( SelectedShapes )
            
            self.showInfo ("info", "All materials removed from the object!")             

            self.txtbrowToolConclusion.setHtml( conclusion.toolOperationConclusion(current_languge, "DelMat") )          

        else:
            conclusion_text = conclusion.noSelection(current_languge, "del_mat")
            self.txtbrowToolConclusion.setHtml(conclusion_text) 

            self.showInfo ("warn", "Please select something for delete. Mesh object for example..")    

    #assign gloss
    def btnGlossMatClicked (self):
        
        current_languge = cfgl.configLoader()[14]        
        
        SelectionData = gen_func.checkSelection()
        
        SelectedShapes = SelectionData[0]
         
        #assign gloss shader
        if len(SelectedShapes) > 0:
            
            createGlossMaterial(SelectedShapes)
            
            cmds.select( SelectedShapes )

            self.showInfo ("info", "Gloss shader was asigned!")

            self.txtbrowToolConclusion.setHtml( conclusion.toolOperationConclusion(current_languge, "GlossMat") )          

        else:
            conclusion_text = conclusion.noSelection(current_languge, "gloss_mat")
            self.txtbrowToolConclusion.setHtml(conclusion_text) 

            self.showInfo ("warn", "Please select something for assign. Mesh object for example..")       

    #assign Mate
    def btnMateMatClicked (self):
        
        current_languge = cfgl.configLoader()[14]        
        
        SelectionData = gen_func.checkSelection()
        
        SelectedShapes = SelectionData[0]
         
        #assign gloss shader
        if len(SelectedShapes) > 0:
            
            createMateMaterial( SelectedShapes )

            cmds.select( SelectedShapes )

            self.showInfo ("info", "Mate shader was asigned!")           

            self.txtbrowToolConclusion.setHtml( conclusion.toolOperationConclusion(current_languge, "MateMat") )           

        else:
            conclusion_text = conclusion.noSelection(current_languge, "mate_mat")
            self.txtbrowToolConclusion.setHtml(conclusion_text) 

            self.showInfo ("warn", "Please select something for assign. Mesh object for example..")           

    #exp to fbx
    def btnFBXExpClicked (self):
        
        current_languge = cfgl.configLoader()[14]        
        
        SelectionData = gen_func.checkSelection()
        
        SelectedShapes = SelectionData[0]
        
        #get path to file
        PathToFile = cmds.file( query=True, sceneName=True, shn=0)
        
        #get path
        PathToSave = os.path.dirname(PathToFile)
            
        if len(SelectedShapes) > 0:
            
            #get name
            ObjectName = gen_func.shortNamer(SelectedShapes[0])
            
            #create full path
            FullPathToFBXfile = PathToSave + "/" + ObjectName + ".fbx"

            if PathToSave == '':
                self.showInfo ("warn", "Please save current scene before Export!")
                self.txtbrowToolConclusion.setHtml( conclusion.toolOperationConclusion(current_languge, "FBXExpProblem") )           
            else:
                
                ExportResult = exportToFBX(FullPathToFBXfile)
                
                if ExportResult == True:
                    self.showInfo ("info", "Export Complete! Path to FBX file: \n" + FullPathToFBXfile)
                    
                    self.txtbrowToolConclusion.setHtml( conclusion.toolOperationConclusion(current_languge, "FBXExp") )           
                else:
                    self.showInfo ("warn", "Problems with export.")
        else:
            conclusion_text = conclusion.noSelection(current_languge, "fbx_exp")
            self.txtbrowToolConclusion.setHtml(conclusion_text) 
            
            self.showInfo ("warn", "Please select something for export. Mesh object for example..")    
    
    #lod check
    def runLODCheckerJob(self):
        if cmds.objExists('LOD_Group_PT') == True:
            #check attribute
            LODCheckerJob = cmds.scriptJob( runOnce=False, attributeChange=['LOD_0.lodVisibility', self.checkLODVis])
            maya.mel.eval('headsUpDisplay -e -vis 1 HUDObjDetDistFromCam -s 2 -lfs large -dfs large -dp 1;')
            self.btnLODcheck.setChecked(True)
            self.sldLOD.setEnabled(True)
        else:
            #new scene without LOD
            self.NewSceneJob()
        
    #if new scene (for lod)            
    def NewSceneJob(self):
        #new scene without LOD
        #print "New Scene"
        maya.mel.eval('headsUpDisplay -e -vis 0 HUDObjDetDistFromCam -s 2 -lfs large -dfs large -dp 1;')
        self.sldLOD.setValue(0)
        self.sldLOD.setEnabled(False)
        self.btnLODcheck.setChecked(False)
        self.spnLOD1.setStyleSheet("")
        self.spnLOD2.setStyleSheet("")
        self.spnLOD3.setStyleSheet("")
        self.spnLOD4.setStyleSheet("")

    #lod val from file            
    def checkLODValues (self):
        
        #check lod group
        ScenOpenedJob = cmds.scriptJob( runOnce=False, event=['SceneOpened', self.runLODCheckerJob])
        
        #new scene Opened
        NewScenJob = cmds.scriptJob( runOnce=False, event=['NewSceneOpened', self.NewSceneJob])

        #get start values
        currentlod1val = self.spnLOD1.value()
        currentlod2val = self.spnLOD2.value()
        currentlod3val = self.spnLOD3.value()
        currentlod4val = self.spnLOD4.value()
        
        data_from_config = cfgl.configLoader()[5:9]
        
        #get config values
        configlod1val = data_from_config[0]
        configlod2val = data_from_config[1]
        configlod3val = data_from_config[2]
        configlod4val = data_from_config[3]
        
        
        #set config values
        if currentlod1val != configlod1val:
            self.spnLOD1.setValue(int(configlod1val))
             
        if currentlod2val != configlod2val:
            self.spnLOD2.setValue(int(configlod2val))

        if currentlod3val != configlod3val:
            self.spnLOD3.setValue(int(configlod3val))

        if currentlod4val != configlod4val:
            self.spnLOD4.setValue(int(configlod4val))

        if cmds.objExists('LOD_Group_PT'):
            self.checkLODVis()
        
    #run lod check
    def btnLODcheckClicked (self):
        
        cmds.select( clear=True )

        current_languge = cfgl.configLoader()[14]        
        
        SelectionData = gen_func.checkSelection()
        
        SelectedShapes = SelectionData[0]

        #check        
        if (self.btnLODcheck.isChecked()==True) and len(SelectedShapes) == 0:
            
            if cmds.objExists('LOD_Group_PT') == False:
                maya.mel.eval('LevelOfDetailGroup;')
                                
                if cmds.objExists('LOD_Group_1'):
                    cmds.rename('LOD_Group_1', 'LOD_Group_PT')
                
                cmds.setAttr ("LOD_Group_PT.useScreenHeightPercentage", 0)
                
                cmds.group(empty=True, n="LOD_3")
                cmds.group(empty=True, n="LOD_4")
                
                cmds.parent( 'LOD_3', 'LOD_Group_PT' )
                cmds.parent( 'LOD_4', 'LOD_Group_PT' )
                            
                cmds.setAttr ("LOD_Group_PT.threshold[0]", self.spnLOD1.value())
                cmds.setAttr ("LOD_Group_PT.threshold[1]", self.spnLOD2.value())
                cmds.setAttr ("LOD_Group_PT.threshold[2]", self.spnLOD3.value())
                cmds.setAttr ("LOD_Group_PT.threshold[3]", self.spnLOD4.value())
                
                #check visibility of LODs
                LODCheckerJob = cmds.scriptJob( runOnce=False, attributeChange=['LOD_0.lodVisibility', self.checkLODVis])
                
                self.sldLOD.setEnabled(True)
                
                self.checkLODVis()
                
                #HUD
                cmds.headsUpDisplay('distanceHUD', label="LOD Distance:", command=self.distanceChecker, attachToRefresh=True, visible=True, section=1, block=0, labelFontSize='large')
                
                self.showInfo ("info", "LOD groups created. Put LODs to the appropriate groups.")

                self.txtbrowToolConclusion.setHtml( conclusion.toolOperationConclusion(current_languge, "LOD") )
    
        #uncheck
        if self.btnLODcheck.isChecked() == False:

            if cmds.objExists('LOD_Group_PT'):
                cmds.select( 'LOD_Group_PT', replace=True )
                maya.mel.eval('LevelOfDetailUngroup;')
                                                
                self.sldLOD.setValue(0)
                self.sldLOD.setEnabled(False)
                
                self.spnLOD1.setStyleSheet("")
                self.spnLOD2.setStyleSheet("")
                self.spnLOD3.setStyleSheet("")
                self.spnLOD4.setStyleSheet("")
                
                cmds.headsUpDisplay( 'distanceHUD', rem=True )
                self.lblLodDist.setText ("Distance: ")
                
                self.showInfo ("fin", "LOD groups was deleted.")  

    #dist checker        
    def distChecker(self):
        
        #get start values
        lod1val = self.spnLOD1.value()
        lod2val = self.spnLOD2.value()
        lod3val = self.spnLOD3.value()
        lod4val = self.spnLOD4.value() 
        
        path_config = cfgl.configLoader()[99:101]
        
        #compare values and Write to File if they different
        if lod1val >= lod2val:
             self.spnLOD2.setValue(lod1val + 10) #next lod cant less then previous
             currentlod2val = str(self.spnLOD2.value())
             cfgl.ConfigWriter('LOD_distance', 'lod2', currentlod2val, path_config[0], path_config[1])
             
        lod2val = self.spnLOD2.value()    
                    
        if lod2val >= lod3val:
             self.spnLOD3.setValue(lod2val + 10)
             currentlod3val = str(self.spnLOD3.value())
             cfgl.ConfigWriter('LOD_distance', 'lod3', currentlod3val, path_config[0], path_config[1])
        
        lod3val = self.spnLOD3.value()

        if lod3val >= lod4val:
             self.spnLOD4.setValue(lod3val + 10)
             currentlod4val = str(self.spnLOD4.value())
             cfgl.ConfigWriter('LOD_distance', 'lod4', currentlod4val, path_config[0], path_config[1])

        
        if cmds.objExists('LOD_Group_PT'):     
            cmds.setAttr ("LOD_Group_PT.threshold[0]", self.spnLOD1.value())
            cmds.setAttr ("LOD_Group_PT.threshold[1]", self.spnLOD2.value())
            cmds.setAttr ("LOD_Group_PT.threshold[2]", self.spnLOD3.value())
            cmds.setAttr ("LOD_Group_PT.threshold[3]", self.spnLOD4.value())
      
    #edit lod values
    def lod1FinEdit(self):
        #write new values to config
        path_config = cfgl.configLoader()[99:101]
        currentlod1val = str(self.spnLOD1.value())
        cfgl.ConfigWriter('LOD_distance', 'lod1', currentlod1val, path_config[0], path_config[1])

        self.distChecker()
    
        
    def lod2FinEdit(self):
        #write new values to config
        path_config = cfgl.configLoader()[99:101]
        currentlod2val = str(self.spnLOD2.value())
        cfgl.ConfigWriter('LOD_distance', 'lod2', currentlod2val, path_config[0], path_config[1])

        self.distChecker()
    

    def lod3FinEdit(self):
        #write new values to config
        path_config = cfgl.configLoader()[99:101]
        currentlod3val = str(self.spnLOD3.value())
        cfgl.ConfigWriter('LOD_distance', 'lod3', currentlod3val, path_config[0], path_config[1])

        self.distChecker()
    

    def lod4FinEdit(self):
        #write new values to config
        path_config = cfgl.configLoader()[99:101]
        currentlod4val = str(self.spnLOD4.value())
        cfgl.ConfigWriter('LOD_distance', 'lod4', currentlod4val, path_config[0], path_config[1])

        self.distChecker()
    
    #check lod vis
    def checkLODVis(self):
        if cmds.objExists('LOD_Group_PT') == True:
            
            CurrentJobs = cmds.scriptJob( listJobs=True )
            if any("LOD_0.lodVisibility" in s for s in CurrentJobs):
                pass
            else:
                LODCheckerJob = cmds.scriptJob( runOnce=False, attributeChange=['LOD_0.lodVisibility', self.checkLODVis])
            
            #get lod visibility
            lod0vis=cmds.getAttr('LOD_0.lodVisibility')
            lod1vis=cmds.getAttr('LOD_1.lodVisibility')
            lod2vis=cmds.getAttr('LOD_2.lodVisibility')
            lod3vis=cmds.getAttr('LOD_3.lodVisibility')
            lod4vis=cmds.getAttr('LOD_4.lodVisibility')
            
            self.lblLodDist.setText("Distance: " + str(self.distanceChecker()))
            
            #change color and slider position
            if lod0vis == True:
                self.spnLOD1.setStyleSheet("")
                self.spnLOD2.setStyleSheet("")
                self.spnLOD3.setStyleSheet("")
                self.spnLOD4.setStyleSheet("")
                self.sldLOD.setValue(0)
                self.showInfo ("lod", "LOD 0 is displayed.")
        
            if lod1vis == True:
                self.spnLOD1.setStyleSheet("background-color:#005826;")
                self.spnLOD2.setStyleSheet("")
                self.spnLOD3.setStyleSheet("")
                self.spnLOD4.setStyleSheet("")
                self.sldLOD.setValue(1)
                self.showInfo ("lod", "LOD 1 is displayed.")

            if lod2vis == True:
                self.spnLOD1.setStyleSheet("")
                self.spnLOD2.setStyleSheet("background-color:#005826;")
                self.spnLOD3.setStyleSheet("")
                self.spnLOD4.setStyleSheet("")
                self.sldLOD.setValue(2)
                self.showInfo ("lod", "LOD 2 is displayed.")

            if lod3vis == True:
                self.spnLOD1.setStyleSheet("")
                self.spnLOD2.setStyleSheet("")
                self.spnLOD3.setStyleSheet("background-color:#005826;")
                self.spnLOD4.setStyleSheet("")
                self.sldLOD.setValue(3)
                self.showInfo ("lod", "LOD 3 is displayed.")
        
            if lod4vis == True:
                self.spnLOD1.setStyleSheet("")
                self.spnLOD2.setStyleSheet("")
                self.spnLOD3.setStyleSheet("")
                self.spnLOD4.setStyleSheet("background-color:#005826;")
                self.sldLOD.setValue(4)
                self.showInfo ("lod", "LOD 4 is displayed.")


    #distance checker        
    def distanceChecker(self):
        if cmds.objExists('LOD_Group_PT'):
            vector1 = (cmds.getAttr('persp.translate'))[0]
            vector2 = (cmds.getAttr('LOD_Group_PT.translate'))[0]
    
            xd = vector1[0] - vector2[0]
            yd = vector1[1] - vector2[1]
            zd = vector1[2] - vector2[2]
    
            distance = math.sqrt( xd*xd + yd*yd + zd*zd )
                
            return round(distance, 2)    


    #current lod is        
    def currentLOD (self):
        #set slider status
        global sldPressed
        sldPressed = False
        
        #set normal LOD values and reset styles
        cmds.setAttr('LOD_Group_PT.displayLevel[0]', 0)
        cmds.setAttr('LOD_Group_PT.displayLevel[1]', 0)
        self.spnLOD1.setStyleSheet("")
        cmds.setAttr('LOD_Group_PT.displayLevel[2]', 0)
        self.spnLOD2.setStyleSheet("")
        cmds.setAttr('LOD_Group_PT.displayLevel[3]', 0)
        self.spnLOD3.setStyleSheet("")
        cmds.setAttr('LOD_Group_PT.displayLevel[4]', 0)
        self.spnLOD4.setStyleSheet("")
        
        self.checkLODVis()


    def lodsldPressed(self):
        #set slider status
        global sldPressed
        sldPressed = True
        
        
    def lodSwitcher(self):
        
        global sldPressed 
                
        LOD = self.sldLOD.value()
        
        #change visibility LODs only if Slider pressed
        if (LOD==0) and (sldPressed == True):
            cmds.setAttr('LOD_Group_PT.displayLevel[0]', 1)
            cmds.setAttr('LOD_Group_PT.displayLevel[1]', 2)
            
        
        if (LOD==1) and (sldPressed == True):
            cmds.setAttr('LOD_Group_PT.displayLevel[0]', 2)
            cmds.setAttr('LOD_Group_PT.displayLevel[1]', 1)
            cmds.setAttr('LOD_Group_PT.displayLevel[2]', 2)
            

        if (LOD==2) and (sldPressed == True):
            cmds.setAttr('LOD_Group_PT.displayLevel[1]', 2)
            cmds.setAttr('LOD_Group_PT.displayLevel[2]', 1)
            cmds.setAttr('LOD_Group_PT.displayLevel[3]', 2)

        if (LOD==3) and (sldPressed == True):
            cmds.setAttr('LOD_Group_PT.displayLevel[2]', 2)
            cmds.setAttr('LOD_Group_PT.displayLevel[3]', 1)
            cmds.setAttr('LOD_Group_PT.displayLevel[4]', 2)
            

        if (LOD==4) and (sldPressed == True):
            cmds.setAttr('LOD_Group_PT.displayLevel[3]', 2)
            cmds.setAttr('LOD_Group_PT.displayLevel[4]', 1)
            
        
    #render UV    
    def btnPrevRendClicked (self):        

        current_languge = cfgl.configLoader()[14]   

        #get path to file
        PathToSceneFile = cmds.file( query=True, sceneName=True, shn=0)
        
        #get name with extension
        filename = os.path.basename(PathToSceneFile)
        
        #get part of name
        raw_name, extension = os.path.splitext(filename)
        
        #get full path with name
        PathToSavePreview = os.path.dirname(PathToSceneFile) + "/" + raw_name + "_preview.jpg"
        
        if PathToSceneFile == '':
                self.showInfo ("warn", "For render preview first of all please save scene!")   
                self.txtbrowToolConclusion.setHtml( conclusion.toolOperationConclusion(current_languge, "RenderPreviewProblem") ) 
        else:
            
            renderResult = renderPreview(PathToSavePreview)
            
            if renderResult == True:
                self.showInfo ("info", "Preview successfully saved to: \n" + PathToSavePreview)

                self.txtbrowToolConclusion.setHtml( conclusion.toolOperationConclusion(current_languge, "RenderPreview") ) 
            else:
                self.showInfo ("warn", 'Can\'t save preview!')
    

    #check intersection
    def btnCheckFlyClicked (self):
                    
        current_languge = cfgl.configLoader()[14]        
        
        
        # button not pressed - no obj
        if (self.btnCheckFly.isChecked()==True) and (cmds.objExists('pt_flying_edges') == False):
            
            SelectionData = gen_func.checkSelection()        
            SelectedShapes = SelectionData[0]
            
            # one mesh object only
            if (len(SelectedShapes) == 1):                                        
                    try:
                        #get radius and div 2
                        IntersectionRadius = ((float(self.edtFlyDist.text()))/1000)/2
                    except:
                        self.edtFlyDist.setText("10")
                        IntersectionRadius = 0.01
                        cmds.warning("Invalid value out of range (1-99)! Value set to default - 10mm")
                        self.saveIntersetValue()

                    ExtrudeResult = openEdgesExtrude(IntersectionRadius)

                    if ExtrudeResult == True:
                
                        self.showInfo ("info", "If you see the red lines - check the intersection between objects.") 

                        self.txtbrowToolConclusion.setHtml( conclusion.toolOperationConclusion(current_languge, "CheckIntersect") )      
                                        
                        cmds.select(clear=True)
                    else:
                        self.showInfo ("warn", "There are no open edges on the model.")
                        self.btnCheckFly.setChecked(False)
                        cmds.select(SelectedShapes)
            else: #no selection
                conclusion_text = conclusion.noSelection(current_languge, "check_intersect")
                self.txtbrowToolConclusion.setHtml(conclusion_text) 
                
                self.showInfo ("warn", "Please select one Mesh object with default Attributes!")
                self.btnCheckFly.setChecked(False)
        
        # button pressed - obj present
        elif (self.btnCheckFly.isChecked() == False) and (cmds.objExists('pt_flying_edges') == True):                                                
                
                cmds.delete('pt_flying_edges')
                self.showInfo ("info", "Previous intersection check was cleaned.")
                if current_languge == "eng":
                    self.txtbrowToolConclusion.setHtml("Previous intersection check was cleaned.")
                else:
                    self.txtbrowToolConclusion.setHtml("Проверочная геометрия проверки пересечений была успешно удалена.")
                    
        # button pressed - no obj (alredy deleted)
        elif (self.btnCheckFly.isChecked() == False) and (cmds.objExists('pt_flying_edges') == False):                                                
                
                self.showInfo ("info", "Previous intersection already cleaned.")
                if current_languge == "eng":
                    self.txtbrowToolConclusion.setHtml("Previous intersection already cleaned.")
                else:
                    self.txtbrowToolConclusion.setHtml("Проверочная геометрия проверки пересечений уже была удалена. Скорее всего - вручную. Нельзя удалить удаленное)")
                    
    def checkToolsValues(self):
        
        current_intersection_depth = self.edtFlyDist.text()
        current_targ_face_count = int(self.edtTargFaceCount.text())
        
        #load data from config
        data_from_config = cfgl.configLoader()[12:14] 
        
        #For Intersection
        try:
            config_intersection_depth = data_from_config[0]
            int(config_intersection_depth)
                        
            #set intersect depth
            if current_intersection_depth != config_intersection_depth:
                self.edtFlyDist.setText(config_intersection_depth)
                
        except:
            self.saveIntersetValue()
        
        #For Retopo    
        try:
            config_targ_face_count = data_from_config[1]
            int(config_targ_face_count)

            #set face count
            if current_targ_face_count != config_targ_face_count:
                self.edtTargFaceCount.setText(config_targ_face_count)
        except:
            self.saveRetopoValue()
            
    
    #save value
    def saveIntersetValue(self):
        
        try:
            int(self.edtFlyDist.text())
            path_config = cfgl.configLoader()[99:101]            
            current_intersection_depth = self.edtFlyDist.text()
            cfgl.ConfigWriter('Tools', 'intersection_depth', current_intersection_depth, path_config[0], path_config[1])
        except:
            cmds.warning("intersection_depth: Invalid value or value out of range (1-99)! Value set to default - 10mm")
            path_config = cfgl.configLoader()[99:101]
            current_intersection_depth = '10'
            self.edtFlyDist.setText(current_intersection_depth)
            cfgl.ConfigWriter('Tools', 'intersection_depth', current_intersection_depth, path_config[0], path_config[1])


    #save value
    def saveRetopoValue(self):
        
        try:
            int(self.edtTargFaceCount.text())
            path_config = cfgl.configLoader()[99:101]            
            current_targ_face_count = self.edtTargFaceCount.text()
            cfgl.ConfigWriter('Tools', 'target_face_count', current_targ_face_count, path_config[0], path_config[1])
        except:
            cmds.warning("target_face_count: Invalid value or value out of range (10-999999)! Value set to default - 100 faces")
            path_config = cfgl.configLoader()[99:101]
            current_targ_face_count = '100'
            self.edtTargFaceCount.setText(current_targ_face_count)
            cfgl.ConfigWriter('Tools', 'target_face_count', current_intersection_depth, path_config[0], path_config[1])

            
    #retop        
    def btnSetFaceCountClicked (self):
        
        #get count in range 10-999999
        try:
            current_targ_face_count = int(self.edtTargFaceCount.text())
            if (current_targ_face_count < 10):
                 current_targ_face_count = 10
                 self.edtTargFaceCount.setText("10")
                 cmds.warning ("PolygonTools: Minimum Target Face Count is 10.")
        except:
            self.edtTargFaceCount.setText("100")
            current_targ_face_count = 100
            self.showInfo ("warn", "Please input correct faces value in range 10-999999." +"\n" + "Value set to default - 100 faces")
        
        current_languge = cfgl.configLoader()[14]        
        
        SelectionData = gen_func.checkSelection()
        
        SelectedShapes = SelectionData[0]
        
        #assign mate shader
        if len(SelectedShapes) > 0:
            
            print "Retopolgy list:"

            for i in range(len(SelectedShapes)):
                cmds.select(SelectedShapes[i])
                selectedComponent = cmds.ls( sl=True )
                try:
                    cmds.polyRetopo (selectedComponent[0])
                    cmds.setAttr("polyRetopo1.targetFaceCount", current_targ_face_count)
                    cmds.delete(SelectedShapes[i], constructionHistory=True )
                    print ("Current polycount of " + gen_func.shortNamer(SelectedShapes[i]) + " is " + str(cmds.polyEvaluate( f=True )) + " faces.")
                except:
                    pass
            
            if len(SelectedShapes) == 1:
                self.showInfo ("info", "Retopology complete for " + gen_func.shortNamer(SelectedShapes[0]) + ". See log for details.")
            elif len(SelectedShapes) > 1:
                self.showInfo ("info", "Retopology complete for " + str(len(SelectedShapes)) + " objects. See log for details.")
            
            self.txtbrowToolConclusion.setHtml( conclusion.toolOperationConclusion(current_languge, "Retop") )   

        else:
            conclusion_text = conclusion.noSelection(current_languge, "retop")
            self.txtbrowToolConclusion.setHtml(conclusion_text) 
            
            self.showInfo ("warn", "Please select one Mesh object for retop!")


def createMateMaterial(SelectedShapes):
    
    if (cmds.objExists('pt_mate_shader') == False) or (cmds.objExists('pt_shading_group_mate') == False):

        try:
            cmds.delete('pt_shading_group_mate')
            DeletedElementsCount += 1
        except:
            pass

        try:
            cmds.delete('pt_mate_shader')
            DeletedElementsCount += 1
        except:
            pass

        pt_mate_mat = cmds.shadingNode('lambert', asShader=True, name="pt_mate_shader")
        cmds.sets(name='pt_shading_group_mate', renderable=True, empty=True)
        cmds.defaultNavigation(connectToExisting=True, source='pt_mate_shader', destination='pt_shading_group_mate')
    
    if (cmds.objExists('pt_mate_shader') == True) and (cmds.objExists('pt_shading_group_mate') == True):                
        cmds.sets(SelectedShapes, e=True, forceElement='pt_shading_group_mate')

    print ("PolygonTools. Mate shader was created.")


def createGlossMaterial(SelectedShapes):
    
    if (cmds.objExists('pt_gloss_shader') == False) or (cmds.objExists('pt_shading_group_gloss') == False):

        try:
            cmds.delete('pt_shading_group_gloss')
            DeletedElementsCount += 1
        except:
            pass

        try:
            cmds.delete('pt_gloss_shader')
            DeletedElementsCount += 1
        except:
            pass

        pt_gloss_mat = cmds.shadingNode('blinn', asShader=True, name="pt_gloss_shader")
        cmds.setAttr('pt_gloss_shader'+'.specularColor', 1, 1, 1, type="double3")
        cmds.sets(name='pt_shading_group_gloss', renderable=True, empty=True)
        cmds.defaultNavigation(connectToExisting=True, source='pt_gloss_shader', destination='pt_shading_group_gloss')
        
    if (cmds.objExists('pt_gloss_shader') == True) and (cmds.objExists('pt_shading_group_gloss') == True):
        cmds.sets(SelectedShapes, e=True, forceElement='pt_shading_group_gloss')  

    print ("PolygonTools. Gloss shader was created.")

def deleteMaterial (SelectedShapes):

    cmds.shadingNode('lambert', asShader=True, name="pt_dummy_shader")
    cmds.sets(name='pt_shading_group_dummy', renderable=True, empty=True)
    cmds.defaultNavigation(connectToExisting=True, source='pt_dummy_shader', destination='pt_shading_group_dummy')
    cmds.sets(SelectedShapes, e=True, forceElement='pt_shading_group_dummy')
    
    #delete shaders
    cmds.delete('pt_dummy_shader')
    cmds.delete('pt_shading_group_dummy')

def exportToFBX(FullPathToFBXfile):
    try:
        maya.mel.eval('FBXResetExport;')
        maya.mel.eval('FBXExportCameras -v false')
        maya.mel.eval('FBXExportLights -v false')
        maya.mel.eval('FBXExportScaleFactor 1.0')
        maya.mel.eval('FBXExportConvertUnitString m')
        maya.mel.eval('FBXExportConstraints -v false')
        maya.mel.eval('FBXExportEmbeddedTextures -v false')
        maya.mel.eval('FBXExportGenerateLog -v false')
        maya.mel.eval('FBXExportInAscii -v false')
        maya.mel.eval('FBXExportInputConnections -v false')
        maya.mel.eval('FBXExportInstances -v false')
        maya.mel.eval('FBXExportLights -v false')
        maya.mel.eval('FBXExportShapes -v false')
        maya.mel.eval('FBXExportSkins -v false')
        maya.mel.eval('FBXExportSmoothingGroups -v true')
        maya.mel.eval('FBXExportSmoothMesh -v false')
        maya.mel.eval('FBXExportUpAxis y')
        maya.mel.eval('FBXExportTangents -v false')
        maya.mel.eval('FBXExportTriangulate -v false')
        cmds.file(FullPathToFBXfile, force=True, options='v=0', typ="FBX export", exportSelected=True)
        return True          
    except:
        return False
        

def renderPreview (PathToSavePreview):
    try:                
        #switch to persp
        cmds.modelEditor( modelPanel='modelPanel4', da="smoothShaded", displayTextures=True, grid=True, displayLights="default", cameras=False, activeView=True)
    
        #camera setup default view
        cmds.xform('persp', t=(24,18,24), ro=(-27.938, 45.000, 0.000))
        cmds.tumble('perspShape', pivotPoint=(0,0,0))
        cmds.viewFit()    
        
        #render image
        cmds.playblast(startTime=1, endTime=1,  format="image", completeFilename=PathToSavePreview, sequenceTime=False, \
        clearCache=True, viewer=False, showOrnaments=True, fp=0, percent=100, compression="jpg", quality=100, widthHeight=[1920, 1080])

        return True
    except: 
        return False

def openEdgesExtrude (IntersectionRadius):

    PTProgressWindow = cmds.window(title="PolygonTools Progress Bar", minimizeButton=False, maximizeButton=False)
    cmds.columnLayout(PTProgressWindow )
    
    try:
        maya.mel.eval("{ string $c[];string $f[];convertToSelectionBorder(-1, true, $c, $f); };")
        
        selectedComponents = cmds.ls( selection=True, flatten=True )
        
        progressControl = cmds.progressBar(maxValue=len(selectedComponents), width=300)
        cmds.showWindow( PTProgressWindow )
        
        #array for elements
        openEdges=[]
        openEdgesPoly=[]
        
        for i in range(len(selectedComponents)):
            cmds.select(selectedComponents[i])    
            curve_name = "pt_curve_" + str(i)
            openEdges.append(curve_name)
            #create shapes from curves
            maya.mel.eval("polyToCurve -form 0 -degree 1 -conformToSmoothMeshPreview 0 -n " + curve_name + ";")
            #if i%100 == 0:
            cmds.progressBar(progressControl, edit=True, step=1)
        
        #create shape of extrude       
        cmds.circle(name="pt_circle_fly_test", center=(0,0,0), normal=(0,1,0), sweep=360, radius=IntersectionRadius, degree=1, ut=False, tolerance=0, sections=4, ch=True)        
        
        for i in range(len(openEdges)):
            cmds.extrude("pt_circle_fly_test", openEdges[i], ch=True, range=False, polygon=0, et=2, ucp=1, upn=True, fixedPath=True, rotation=0, scale=1, rsp=True, name="pt_fly_nurbs_"+str(i))
            cmds.nurbsToPoly("pt_fly_nurbs_" + str(i), eta=False, constructionHistory=True, polygonType=1, name="pt_fly_poly_" + str(i))
            
            openEdgesPoly.append("pt_fly_poly_" + str(i))
            
            #delete temp geo
            cmds.delete(openEdges[i])
            cmds.delete("pt_fly_nurbs_"+str(i))    
            cmds.progressBar(progressControl, edit=True, step=1)
        
        cmds.delete("pt_circle_fly_test")
                    
        cmds.select(openEdgesPoly)
            
        #Unite
        
        cmds.polyUnite(n='pt_flying_edges' )
        #delete temp geo
        cmds.delete(openEdgesPoly)
        
        ExampleNodes = cmds.ls(sl=True)
        
        #paint
        for n in ExampleNodes:
            cmds.setAttr(n+'.overrideEnabled', 1)
            cmds.setAttr(n+'.overrideRGBColors', 1)
            cmds.setAttr(n+'.overrideColorRGB', 1.0, 0.0, 0.0)
        
        return True
    except:
        return False
    finally:
        cmds.deleteUI( PTProgressWindow , window=True ) 