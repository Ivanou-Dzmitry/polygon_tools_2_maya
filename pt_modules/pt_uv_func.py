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

class PT_UV_Tab (QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent=parent)
        
        #Create Widgets
        self.tabUv_v_layout = QVBoxLayout(self)
        self.tabUv_v_layout.setAlignment(Qt.AlignTop)
        self.tabUv_v_layout.setContentsMargins(0,10,0,10)
        self.tabUv_v_layout.setSpacing(5)
        
        currentDir = os.path.dirname(__file__)
        try:
            iconScaleUV2  = QPixmap(currentDir +"/icons/scale_uv2_icon.png")
            iconScaleUV05  = QPixmap(currentDir +"/icons/scale_uv05_icon.png")
            iconMoveVUp  = QPixmap(currentDir +"/icons/move_v_up_icon.png")
            iconMoveVDown  = QPixmap(currentDir +"/icons/move_v_down_icon.png")
            iconMoveURight  = QPixmap(currentDir +"/icons/move_u_right_icon.png")
            iconMoveULeft  = QPixmap(currentDir +"/icons/move_u_left_icon.png")
            iconShowUV  = QPixmap(currentDir +"/icons/show_uv_icon.png")
            iconRemoveChecker  = QPixmap(currentDir +"/icons/remove_checker_icon.png")
        except:
            cmds.warning( "PolygonTools: Can't load icons for UV Tab! Check icon files in pt_modules/icons directory.")
                
        #label for info
        self.lblInfo_01 = QLabel("Select an object and click on the necessary checker or utility.")
        self.lblInfo_01.setMargin(2)
        
        #group for Checkers
        self.gboxCheckers = QGroupBox("Checker Textures")
        self.gboxCheckers.setMaximumWidth(340)
        self.gboxCheckers_v_layout = QVBoxLayout()
                
        #Red checker
        self.btnCheStd = QPushButton()
        self.btnCheStd.setMaximumWidth(68)
        self.btnCheStd.setMaximumHeight(68)
        
        #Digit checker
        self.btnCheDig = QPushButton()
        self.btnCheDig.setMaximumWidth(68)
        self.btnCheDig.setMaximumHeight(68)
        
        #Diagonal checker
        self.btnCheDiag = QPushButton()
        self.btnCheDiag.setMaximumWidth(68)
        self.btnCheDiag.setMaximumHeight(68)
        
        #Gradient checker
        self.btnCheGrad = QPushButton()
        self.btnCheGrad.setMaximumWidth(68)
        self.btnCheGrad.setMaximumHeight(68)        
        
        currentDir = os.path.dirname(__file__)
        
        #Red checker icon
        self.iconCheRed = QIcon() 
        checker_standard_path = currentDir +"/icons/checker_standard_icon.png"
        checkCheckerTextureFile(checker_standard_path)        
        self.iconCheRed.addPixmap(QPixmap(checker_standard_path), QIcon.Normal, QIcon.Off)
        self.btnCheStd.setIcon(self.iconCheRed)
        self.btnCheStd.setIconSize(QSize(64, 64))
        
        #Digit checker  icon
        self.iconCheDig = QIcon() 
        checker_digital_path = currentDir +"/icons/checker_digital_icon.png"
        checkCheckerTextureFile(checker_digital_path)
        self.iconCheDig.addPixmap(QPixmap(checker_digital_path), QIcon.Normal, QIcon.Off)
        self.btnCheDig.setIcon(self.iconCheDig)
        self.btnCheDig.setIconSize(QSize(64, 64))

        #Diagoanl checker  icon
        self.iconCheDiag = QIcon() 
        checker_diagonal_path = currentDir +"/icons/checker_diagonal_icon.png"
        checkCheckerTextureFile(checker_diagonal_path)
        self.iconCheDiag.addPixmap(QPixmap(checker_diagonal_path), QIcon.Normal, QIcon.Off)
        self.btnCheDiag.setIcon(self.iconCheDiag)
        self.btnCheDiag.setIconSize(QSize(64, 64))

        #Gradient checker  icon
        self.iconCheGrad = QIcon()
        checker_gradient_path = currentDir +"/icons/checker_gradient_icon.png"
        checkCheckerTextureFile(checker_gradient_path)
        self.iconCheGrad.addPixmap(QPixmap(checker_gradient_path), QIcon.Normal, QIcon.Off)
        self.btnCheGrad.setIcon(self.iconCheGrad)
        self.btnCheGrad.setIconSize(QSize(64, 64))
        
        self.gboxCheckRes = QGroupBox("Checker Texture Size Emulation (px)")
        self.gboxCheckRes.setMaximumWidth(340)
        self.gboxCheckRes.setMaximumHeight(50)
        self.gboxCheckRes.setEnabled(False)
        self.gboxCheckRes_h_layout = QHBoxLayout()
        
        self.rbtn256 = QRadioButton()
        self.rbtn256.setText("256")
        self.rbtn512 = QRadioButton()
        self.rbtn512.setText("512")
        self.rbtn1024 = QRadioButton()
        self.rbtn1024.setText("1K")
        self.rbtn2048 = QRadioButton()
        self.rbtn2048.setText("2K")
        self.rbtn4096 = QRadioButton()
        self.rbtn4096.setText("4K")
        self.rbtn8192 = QRadioButton()
        self.rbtn8192.setText("8K")
        
        #UV Utils
        self.gboxUVUtils = QGroupBox("UV Utilities")
        self.gboxUVUtils.setMaximumWidth(340)
        self.gboxUVUtils.setMaximumHeight(350)
        self.gboxUVUtils.setEnabled(True)
        self.gboxUVUtil_h_layout = QHBoxLayout()
        
        self.gboxUVUtil_v_layout1 = QVBoxLayout()
        self.gboxUVUtil_v_layout1.setAlignment(Qt.AlignTop)
        
        self.gboxUVUtil_v_layout2 = QVBoxLayout()
        self.gboxUVUtil_v_layout2.setAlignment(Qt.AlignTop)
        
        self.gboxUVUtil_v_layout3 = QVBoxLayout()
        self.gboxUVUtil_v_layout3.setAlignment(Qt.AlignTop)
        
        self.btnScale2 = QPushButton("x2")
        self.btnScale2.setIcon(iconScaleUV2)
        self.btnScale05 = QPushButton("x0.5")
        self.btnScale05.setIcon(iconScaleUV05)
        
        self.btnMoveUVLeft = QPushButton("-1U")
        self.btnMoveUVLeft.setIcon(iconMoveULeft)
        
        self.btnMoveUVRight = QPushButton("+1U")
        self.btnMoveUVRight.setIcon(iconMoveURight)
        
        self.btnMoveUVUp = QPushButton("+1V")
        self.btnMoveUVUp.setIcon(iconMoveVUp)
        
        self.btnMoveUVDown = QPushButton("-1V")
        self.btnMoveUVDown.setIcon(iconMoveVDown)
        
        self.btnViewUV = QToolButton()
        self.btnViewUV.setText("Show UV")
        self.btnViewUV.setIcon(iconShowUV)
        self.btnViewUV.setMaximumWidth(125) 
        self.btnViewUV.setCheckable(True)
        
        self.lblUvScale = QLabel("Scale UV")
        self.lblMoveUV = QLabel("Move UV")
        self.lblShowUV = QLabel("Additional")
        
        #layouting
        self.gboxCheckRes_h_layout.addWidget(self.rbtn256)
        self.gboxCheckRes_h_layout.addWidget(self.rbtn512)
        self.gboxCheckRes_h_layout.addWidget(self.rbtn1024)
        self.gboxCheckRes_h_layout.addWidget(self.rbtn2048)
        self.gboxCheckRes_h_layout.addWidget(self.rbtn4096)
        self.gboxCheckRes_h_layout.addWidget(self.rbtn8192)
        
        
        self.gboxUVUtil_v_layout1.addWidget(self.lblUvScale)
        self.gboxUVUtil_v_layout1.addWidget(self.btnScale2)
        self.gboxUVUtil_v_layout1.addWidget(self.btnScale05)
        
        self.gboxUVUtil_v_layout2.addWidget(self.lblMoveUV)
        self.gboxUVUtil_v_layout2.addWidget(self.btnMoveUVLeft)
        self.gboxUVUtil_v_layout2.addWidget(self.btnMoveUVRight)
        self.gboxUVUtil_v_layout2.addWidget(self.btnMoveUVUp)
        self.gboxUVUtil_v_layout2.addWidget(self.btnMoveUVDown)
        
        self.gboxUVUtil_v_layout3.addWidget(self.lblShowUV)
        self.gboxUVUtil_v_layout3.addWidget(self.btnViewUV)
        
        self.gboxUVUtil_h_layout.addLayout(self.gboxUVUtil_v_layout1)
        self.gboxUVUtil_h_layout.addLayout(self.gboxUVUtil_v_layout2)
        self.gboxUVUtil_h_layout.addLayout(self.gboxUVUtil_v_layout3)
        
        self.gboxCheckRes.setLayout(self.gboxCheckRes_h_layout)
        self.gboxUVUtils.setLayout(self.gboxUVUtil_h_layout)

        self.btnRemCheck = QPushButton("Remove Checker")
        self.btnRemCheck.setMaximumWidth(146)
        self.btnRemCheck.setIcon(iconRemoveChecker)
        self.btnRemCheck.setEnabled(False)
        
        self.gboxUVConclusion = QGroupBox("Conclusion")
        self.gboxUVConclusion.setMaximumWidth(340)
        self.gboxUVConclusion.setMinimumHeight(170)
        self.gboxUVConclusion_v_layout = QVBoxLayout()        

        #conclusion text here
        self.txtbrowUVConclusion = QTextBrowser()
        self.txtbrowUVConclusion.setHtml("") 
        
            
        #Add Widgets        
        self.gboxUVConclusion_v_layout.addWidget(self.txtbrowUVConclusion) 
        
        self.tabUv_v_layout.addWidget(self.lblInfo_01)
        
        #add gbox
        self.tabUv_v_layout.addWidget(self.gboxCheckers)
        
        self.gboxCheckers.setLayout(self.gboxCheckers_v_layout)
        
        self.tabUv_h_layout_01 = QHBoxLayout()
        self.tabUv_h_layout_01.setAlignment(Qt.AlignLeft)
        self.gboxCheckers_v_layout.addLayout(self.tabUv_h_layout_01)
        
        #add buttons
        self.tabUv_h_layout_01.addWidget(self.btnCheStd)
        self.tabUv_h_layout_01.addWidget(self.btnCheDig)
        self.tabUv_h_layout_01.addWidget(self.btnCheDiag)
        self.tabUv_h_layout_01.addWidget(self.btnCheGrad)
        
        #remove checker button
        self.gboxCheckers_v_layout.addWidget(self.btnRemCheck)
        
        self.tabUv_v_layout.addWidget(self.gboxCheckRes)
        
        self.tabUv_v_layout.addWidget(self.gboxUVUtils)
        
        #conclusion
        self.gboxUVConclusion.setLayout(self.gboxUVConclusion_v_layout)
        
        #conclusion area
        self.tabUv_v_layout.addWidget(self.gboxUVConclusion)

        
        #SIGNALS
        self.btnRemCheck.clicked.connect(self.btnRemCheckClicked)
        
        #checker buttons click
        self.btnCheStd.clicked.connect(self.btnCheStdClicked)
        self.btnCheDig.clicked.connect(self.btnCheDigClicked)
        self.btnCheDiag.clicked.connect(self.btnCheDiagClicked)
        self.btnCheGrad.clicked.connect(self.btnCheGradClicked)       
        
        self.rbtn256.toggled.connect(self.setTile256Toggled)         
        self.rbtn512.toggled.connect(self.setTile512Toggled)
        self.rbtn1024.toggled.connect(self.setTile1024Toggled)
        self.rbtn2048.toggled.connect(self.setTile2048Toggled)
        self.rbtn4096.toggled.connect(self.setTile4096Toggled)
        self.rbtn8192.toggled.connect(self.setTile8192Toggled)
        
        self.btnScale2.clicked.connect(self.btnScale2Clicked)
        self.btnScale05.clicked.connect(self.btnScale05Clicked)
        
        self.btnMoveUVLeft.clicked.connect(self.btnMoveUVLeftClicked)
        self.btnMoveUVRight.clicked.connect(self.btnMoveUVRightClicked)
        self.btnMoveUVUp.clicked.connect(self.btnMoveUVUpClicked)
        self.btnMoveUVDown.clicked.connect(self.btnMoveUVDownClicked)
        
        self.btnViewUV.pressed.connect(self.btnViewUVPressed)
        
        self.PreviousShadersArray = []
        self.ObjectsWithShadersArray = []

        #intro text
        current_languge = cfgl.configLoader()[14]
        self.txtbrowUVConclusion.setHtml( conclusion.uvTabIntroConclusion(current_languge) )        

        Created2DNodes = self.introShaderCheck()

        #if any 2d texture is present
        if len(Created2DNodes) > 0:        
            #get tile from first    
            Repeat = cmds.getAttr('pt_2dTexture_' + Created2DNodes[0] + '.repeatU')
            self.toggleTile(int(Repeat))
        else:
            self.rbtn256.setChecked(True)        

        if cmds.objExists('pt_uv_shader') == True and cmds.objExists('pt_shading_group_uv') == True and  cmds.objExists('pt_uv_texture') == True and cmds.objExists('pt_2dTUV') == True:
            self.btnViewUV.setText("Hide UV")
            self.btnViewUV.setChecked(True)
            print ("UV Shader integrity ok!")
        else:
            print("PolygonTools. UV Shader not yet created or its integrity broken!")

    def introShaderCheck(self):
        
        Created2DNodes = []

        #set some options if shader exist
        for i in range (1,5):
            
            Type = "0" + str(i)
            
            CheckResult = checkShaderIntegrity(Type)
            
            if (CheckResult == True):
                self.btnRemCheck.setEnabled(True)
                self.gboxCheckRes.setEnabled(True)

            if cmds.objExists( 'pt_2dTexture_' + Type ) == True:
                Created2DNodes.append(Type)
        
        return Created2DNodes

    #toggle and set tile
    def toggleTile (self, Repeat):

        #if tile was changed to incorrect
        GoodTileAray = [2, 4, 8, 16, 32, 64]

        if Repeat == 2:
            self.rbtn256.setChecked(True)

        if Repeat == 4:
            self.rbtn512.setChecked(True)

        if Repeat == 8:
            self.rbtn1024.setChecked(True)

        if Repeat == 16:
            self.rbtn2048.setChecked(True)

        if Repeat == 32:
            self.rbtn4096.setChecked(True)

        if Repeat == 64:
            self.rbtn8192.setChecked(True)
        
        #set to 256 if problems
        if Repeat not in GoodTileAray:
            self.rbtn256.setChecked(True)
            print "PolygonTools. Tile was fixed to 256x256"

        
    def showInfo(self, info_type, info_text):
        
        if info_type=="info":
            self.lblInfo_01.setText(info_text)
            self.lblInfo_01.setStyleSheet("background-color:#3D523D;")
            print "PolygonTools:", info_text
        
        if info_type=="warn":
            self.lblInfo_01.setText(info_text)
            self.lblInfo_01.setStyleSheet("background-color:#916666;")
            cmds.warning( "PolygonTools:" + info_text )


    def btnRemCheckClicked (self):

        current_languge = cfgl.configLoader()[14]
                
        for i in range(len(self.PreviousShadersArray)):
            try:
                cmds.sets(self.ObjectsWithShadersArray[i], e=True, forceElement = self.PreviousShadersArray[i])
            except:
                pass

        self.PreviousShadersArray = []
        self.ObjectsWithShadersArray = []
        
        print ""
        print "Delete Checker Shaders:"
        
        #delete all checkers
        for i in range(1,5):
            
            Type = "0" + str(i)

            DeletedElementsCount = 0
                
            try:
                cmds.delete('pt_shading_group_type_' + Type)
                DeletedElementsCount += 1
            except:
                pass
            
            try:    
                cmds.delete('pt_checker_shader_' + Type)
                DeletedElementsCount += 1
            except:
                pass                
            
            try:
                cmds.delete('pt_checker_texture_' + Type)
                DeletedElementsCount += 1
            except:
                pass

            try:                
                cmds.delete('pt_2dTexture_' + Type)
                DeletedElementsCount += 1
            except:
                pass
                
            if DeletedElementsCount > 0:
                print "PolygonTools. pt_shading_group_type_" + Type, "was removed!"             
                        
        #disable buttons            
        self.btnRemCheck.setEnabled(False)
        self.gboxCheckRes.setEnabled(False)
        print ""

        conclusion_text = conclusion.uvOperationConclusion (current_languge, "delete_checker")
        self.txtbrowUVConclusion.setHtml(conclusion_text)

        self.showInfo("info", "Remove pt-chaders operation complete!")

    def checkerRoutineFunctions(self, SelectedShapes):
        self.checkCheckerTextureRepeat()    
        
        cmds.select(SelectedShapes)

        self.btnRemCheck.setEnabled(True)
        self.gboxCheckRes.setEnabled(True)

        #delete colorsets
        for i in range(len(SelectedShapes)):
            CurrentColorSet = cmds.polyColorSet(SelectedShapes[i], q=True, currentColorSet=True)
            if CurrentColorSet != None:
                cmds.polyColorSet (SelectedShapes[i], delete=True )


    #Aassign std checker    
    def btnCheStdClicked (self):

        current_languge = cfgl.configLoader()[14]
                
        SelectionData = gen_func.checkSelection()
        
        SelectedShapes = SelectionData[0]
        
        if len(SelectedShapes) > 0:

            CurrentShaderData = getCurrentShader(SelectedShapes)
            
            self.PreviousShadersArray = CurrentShaderData[0]
            self.ObjectsWithShadersArray = CurrentShaderData[1]
            
            if checkShaderIntegrity("01") == True:
                changeCheckerTexture ("checker_standard", SelectedShapes)
            else:
                createCheckerMaterial("01")
                changeCheckerTexture ("checker_standard", SelectedShapes)
            
            self.checkerRoutineFunctions(SelectedShapes)

            conclusion_text = conclusion.uvOperationConclusion (current_languge, "assign_std_checker")
            self.txtbrowUVConclusion.setHtml(conclusion_text)

            self.showInfo("info", "Standard checker was assigned!")
        
        else:
            conclusion_text = conclusion.noSelection(current_languge, "assign_std_checker")
            self.txtbrowUVConclusion.setHtml(conclusion_text) 

            self.showInfo("warn", "Cant assign checker. Please select mesh object in Object Mode.")
          
    def btnCheDigClicked (self):

        current_languge = cfgl.configLoader()[14]

        SelectionData = gen_func.checkSelection()
        
        SelectedShapes = SelectionData[0]
        
        if len(SelectedShapes) > 0:

            CurrentShaderData = getCurrentShader(SelectedShapes)
            
            self.PreviousShadersArray = CurrentShaderData[0]
            self.ObjectsWithShadersArray = CurrentShaderData[1]
                
            if checkShaderIntegrity("02") == True:                
                changeCheckerTexture ("checker_digital", SelectedShapes)
            else:
                createCheckerMaterial("02")
                changeCheckerTexture ("checker_digital", SelectedShapes)
                
            self.checkerRoutineFunctions(SelectedShapes)

            conclusion_text = conclusion.uvOperationConclusion (current_languge, "assign_dig_checker")
            self.txtbrowUVConclusion.setHtml(conclusion_text)
            self.showInfo("info", "Digital checker was assigned!")
        
        else:
            conclusion_text = conclusion.noSelection(current_languge, "assign_dig_checker")
            self.txtbrowUVConclusion.setHtml(conclusion_text) 

            self.showInfo("warn", "Cant assign checker. Please select mesh object in Object Mode.")
        
    def btnCheDiagClicked (self):

        current_languge = cfgl.configLoader()[14]        

        SelectionData = gen_func.checkSelection()
        
        SelectedShapes = SelectionData[0]

        if len(SelectedShapes) > 0:

            CurrentShaderData = getCurrentShader(SelectedShapes)
            
            self.PreviousShadersArray = CurrentShaderData[0]
            self.ObjectsWithShadersArray = CurrentShaderData[1]
        
            if checkShaderIntegrity("03") == True:
                changeCheckerTexture ("checker_diagonal", SelectedShapes)
            else:
                createCheckerMaterial("03")
                changeCheckerTexture ("checker_diagonal", SelectedShapes)        

            self.checkerRoutineFunctions(SelectedShapes)

            conclusion_text = conclusion.uvOperationConclusion (current_languge, "assign_diag_checker")
            self.txtbrowUVConclusion.setHtml(conclusion_text)
            self.showInfo("info", "Diagonal checker was assigned!")

        else:
            conclusion_text = conclusion.noSelection(current_languge, "assign_diag_checker")
            self.txtbrowUVConclusion.setHtml(conclusion_text) 
            
            self.showInfo("warn", "Cant assign checker. Please select mesh object in Object Mode.")


    def btnCheGradClicked (self):

        current_languge = cfgl.configLoader()[14]        
        
        SelectionData = gen_func.checkSelection()
        
        SelectedShapes = SelectionData[0]

        if len(SelectedShapes) > 0:

            CurrentShaderData = getCurrentShader(SelectedShapes)
            
            self.PreviousShadersArray = CurrentShaderData[0]
            self.ObjectsWithShadersArray = CurrentShaderData[1]
        
            if checkShaderIntegrity("04") == True:
                changeCheckerTexture ("checker_gradient", SelectedShapes)
            else:
                createCheckerMaterial("04")
                changeCheckerTexture ("checker_gradient", SelectedShapes) 

            self.checkerRoutineFunctions(SelectedShapes)

            conclusion_text = conclusion.uvOperationConclusion (current_languge, "assign_grad_checker")
            self.txtbrowUVConclusion.setHtml(conclusion_text)
            self.showInfo("info", "Gradient checker was assigned!")

        else:
            conclusion_text = conclusion.noSelection(current_languge, "assign_grad_checker")
            self.txtbrowUVConclusion.setHtml(conclusion_text)
            
            self.showInfo("warn", "Cant assign checker. Please select mesh object in Object Mode.")


    def checkCheckerTextureRepeat(self):
        if self.rbtn256.isChecked() == True:
            setCheckerTextureRepeat(2, 2)
        
        if self.rbtn512.isChecked() == True:
            setCheckerTextureRepeat(4, 4)
        
        if self.rbtn1024.isChecked() == True:
            setCheckerTextureRepeat(8, 8)
        
        if self.rbtn2048.isChecked() == True:
            setCheckerTextureRepeat(16, 16)
        
        if self.rbtn4096.isChecked() == True:
            setCheckerTextureRepeat(32, 32)
        
        if self.rbtn8192.isChecked() == True:
            setCheckerTextureRepeat(64, 64)
    
        
    def setTile256Toggled (self):

        Nodes = check2DNodes()

        if Nodes == 0:
            self.gboxCheckRes.setEnabled(False)
            print("PolygonTools. Checker Shader not yet created or its integrity broken!")
        
        if self.rbtn256.isChecked() == True and (Nodes > 0):
            setCheckerTextureRepeat(2, 2)
            self.showInfo("info", "256x256 texture was emulated.")
        

    def setTile512Toggled (self):

        Nodes = check2DNodes()

        if Nodes == 0:
            self.gboxCheckRes.setEnabled(False)
            print("PolygonTools. Checker Shader integrity broken!")

        if self.rbtn512.isChecked() == True and (Nodes > 0):
            setCheckerTextureRepeat(4, 4)
            self.showInfo("info", "512x512 texture was emulated.")


    def setTile1024Toggled (self):

        Nodes = check2DNodes()

        if Nodes == 0:
            self.gboxCheckRes.setEnabled(False)
            print("PolygonTools. Checker Shader integrity broken!")

        if self.rbtn1024.isChecked() == True and (Nodes > 0):
            setCheckerTextureRepeat(8, 8)
            self.showInfo("info", "1024x1024 texture was emulated.")
            

    def setTile2048Toggled (self):

        Nodes = check2DNodes()

        if Nodes == 0:
            self.gboxCheckRes.setEnabled(False)
            print("PolygonTools. Checker Shader integrity broken!")

        if self.rbtn2048.isChecked() == True and (Nodes > 0):
            setCheckerTextureRepeat(16, 16)
            self.showInfo("info", "2048x2048 texture was emulated.")
            

    def setTile4096Toggled (self):

        Nodes = check2DNodes()

        if Nodes == 0:
            self.gboxCheckRes.setEnabled(False)
            print("PolygonTools. Checker Shader integrity broken!")

        if self.rbtn4096.isChecked() == True and (Nodes > 0):
            setCheckerTextureRepeat(32, 32)
            self.showInfo("info", "4096x4096 texture was emulated.")
            

    def setTile8192Toggled (self):

        Nodes = check2DNodes()

        if Nodes == 0:
            self.gboxCheckRes.setEnabled(False)
            print("PolygonTools. Checker Shader integrity broken!")

        if self.rbtn8192.isChecked() == True and (Nodes > 0):
            setCheckerTextureRepeat(64, 64)
            self.showInfo("info", "8192x8192 texture was emulated.")


    # x2 Scale UP
    def btnScale2Clicked(self):

        current_languge = cfgl.configLoader()[14]
        
        SelectionData = gen_func.checkSelection()
        SelectedShapes = SelectionData[0]

        if len(SelectedShapes) > 0:
            scaleUV (SelectedShapes, "Up", 2, 2)
            self.showInfo("info", "UV scaled Up.")
        else:
            conclusion_text = conclusion.noSelection(current_languge, "scale_uv_up")
            self.txtbrowUVConclusion.setHtml(conclusion_text) 
            self.showInfo("warn", "Cant assign checker. Please select mesh object in Object Mode.")


    # x0.5 Scale Down    
    def btnScale05Clicked(self):

        current_languge = cfgl.configLoader()[14]

        SelectionData = gen_func.checkSelection()
        SelectedShapes = SelectionData[0]

        if len(SelectedShapes) > 0:
            scaleUV (SelectedShapes, "Down", 0.5, 0.5)
            self.showInfo("info", "UV scaled Down.")
        else:
            conclusion_text = conclusion.noSelection(current_languge, "scale_uv_down")
            self.txtbrowUVConclusion.setHtml(conclusion_text) 
            self.showInfo("warn", "Cant assign checker. Please select mesh object in Object Mode.")


    def btnMoveUVRightClicked (self):

        current_languge = cfgl.configLoader()[14]

        SelectionData = gen_func.checkSelection()
        SelectedShapes = SelectionData[0]

        if len(SelectedShapes) > 0:
            moveUV (SelectedShapes, "Right", 1, 0)
            self.showInfo("info", "UV moved Right.")
        else:
            conclusion_text = conclusion.noSelection(current_languge, "move_uv_right")
            self.txtbrowUVConclusion.setHtml(conclusion_text) 
            self.showInfo("warn", "Cant assign checker. Please select mesh object in Object Mode.")


    def btnMoveUVLeftClicked (self):

        current_languge = cfgl.configLoader()[14]

        SelectionData = gen_func.checkSelection()
        SelectedShapes = SelectionData[0]

        if len(SelectedShapes) > 0:
            moveUV (SelectedShapes, "Left", -1, 0)
            self.showInfo("info", "UV moved Left.")
        else:
            conclusion_text = conclusion.noSelection(current_languge, "move_uv_left")
            self.txtbrowUVConclusion.setHtml(conclusion_text) 
            self.showInfo("warn", "Cant assign checker. Please select mesh object in Object Mode.")


    def btnMoveUVUpClicked (self):

        current_languge = cfgl.configLoader()[14]

        SelectionData = gen_func.checkSelection()
        SelectedShapes = SelectionData[0]

        if len(SelectedShapes) > 0:
            moveUV (SelectedShapes, "Up", 0, 1)
            self.showInfo("info", "UV moved Up.")
        else:
            conclusion_text = conclusion.noSelection(current_languge, "move_uv_up")
            self.txtbrowUVConclusion.setHtml(conclusion_text) 
            self.showInfo("warn", "Cant assign checker. Please select mesh object in Object Mode.")


    def btnMoveUVDownClicked (self):

        current_languge = cfgl.configLoader()[14]

        SelectionData = gen_func.checkSelection()
        SelectedShapes = SelectionData[0]

        if len(SelectedShapes) > 0:
            moveUV (SelectedShapes, "Down", 0, -1)
            self.showInfo("info", "UV moved Down.")
        else:
            conclusion_text = conclusion.noSelection(current_languge, "move_uv_down")
            self.txtbrowUVConclusion.setHtml(conclusion_text)
            self.showInfo("warn", "Cant assign checker. Please select mesh object in Object Mode.")             
    

    def btnViewUVPressed(self):

        current_languge = cfgl.configLoader()[14]

        SelectionData = gen_func.checkSelection()
        SelectedShapes = SelectionData[0]

        #delete colorsets
        for i in range(len(SelectedShapes)):
            CurrentColorSet = cmds.polyColorSet(SelectedShapes[i], q=True, currentColorSet=True)
            if CurrentColorSet != None:
                cmds.polyColorSet (SelectedShapes[i], delete=True )        
        
        #create and delete file
        if len(SelectedShapes) > 0:
            
            #if pressed
            if self.btnViewUV.isChecked() == True:                
                
                #delete shader
                if cmds.objExists('pt_uv_shader'):
                    DelUVShaders()
                    self.btnViewUV.setText("Show UV")
                
                #assign prev mat                                    
                for i in range(len(self.PreviousShadersArray)):
                    try:
                        cmds.sets(self.ObjectsWithShadersArray[i], e=True, forceElement = self.PreviousShadersArray[i])
                    except:
                        pass                    

                self.showInfo("info", "UV Snapshot was removed.")    
                
            else:
                try:                    
                    #get previous shader
                    CurrentShaderData = getCurrentShader(SelectedShapes)
            
                    self.PreviousShadersArray = CurrentShaderData[0]
                    self.ObjectsWithShadersArray = CurrentShaderData[1]

                    #remove old uv if exist
                    if cmds.objExists('pt_uv_shader') == True:
                        DelUVShaders()
                        self.btnViewUV.setText("Show UV")

                    #create and showe shader 
                    createUVTexture(SelectedShapes)

                    cmds.sets(SelectedShapes, e=True, forceElement='pt_shading_group_uv')
                    
                    cmds.select(SelectedShapes)      
                    
                    self.btnViewUV.setText("Hide UV")

                    conclusion_text = conclusion.uvOperationConclusion (current_languge, "assign_uv")
                    self.txtbrowUVConclusion.setHtml(conclusion_text)


                    self.showInfo("info", "UV Snapshot was assigned to objects.")                    
                except:
                    self.showInfo ("warn", "Can't create UV Snapshot.")
                
        else:
            conclusion_text = conclusion.noSelection(current_languge, "show_uv")
            self.txtbrowUVConclusion.setHtml(conclusion_text)            
            
            #If nothing selected
            self.btnViewUV.setChecked(True)
            
            #delete shader if not selected
            if cmds.objExists('pt_uv_shader'):
                DelUVShaders()
                self.btnViewUV.setText("Show UV")
                self.showInfo ("info", "UV Snapshot was removed.")
            else:
                self.showInfo ("warn", "Please select something. Mesh object for example...")


def createUVTexture (SelectedShapes):
    try:
        #get temp dir
        TmpDir = cmds.internalVar(userTmpDir=True)
        
        #filepath
        uvsnapshotfile_path = TmpDir + 'pt_uvsnapshot.jpg'

        #delete file with uv snapshot
        cmds.sysFile (uvsnapshotfile_path, delete=True )

        cmds.uvSnapshot(antiAliased=True, fileFormat="jpg", o=True, n=uvsnapshotfile_path, xr=1024, yr=1024 )
        
        #create and assign mat
        pt_2dTUV = cmds.shadingNode('place2dTexture', name='pt_2dTUV', asUtility=True)
        pt_uv_texture = cmds.shadingNode('file', name='pt_uv_texture', asTexture=True)
        pt_checker = cmds.shadingNode('lambert', asShader=True, name="pt_uv_shader")
        
        cmds.setAttr('pt_uv_texture'+'.fileTextureName', uvsnapshotfile_path , type="string")
        
        pt_shading_group_uv = cmds.sets(name='pt_shading_group_uv', renderable=True, empty=True)
        cmds.disconnectAttr('lambert1.outColor', 'pt_shading_group_uv.surfaceShader')
                
        cmds.connectAttr('pt_uv_shader'+'.outColor','pt_shading_group_uv'+'.surfaceShader')
        cmds.connectAttr('pt_uv_texture'+'.outColor','pt_uv_shader'+'.color')
        cmds.connectAttr('pt_2dTUV'+'.outUV','pt_uv_texture'+'.uvCoord')       
        
        #turn on textures in viewport
        CurrentState = cmds.modelEditor('modelPanel4', q = True, displayTextures=True)
        
        if CurrentState == False:
            cmds.modelEditor( modelPanel='modelPanel4', da="smoothShaded", displayTextures=True, displayLights="default", cameras=False, activeView=True)
        
        print ("PolygonTools. Texture based on UV-layout was created!")
    except:
        cmds.warning ("PolygonTools. Cant create UV-texture.")


def DelUVShaders():
    
    try:
        cmds.delete('pt_uv_shader')
    except:
        pass
    
    try:
        cmds.delete('pt_shading_group_uv')
    except:
        pass
        
    try:
        cmds.delete('pt_uv_texture')
    except:
        pass

    try:
        cmds.delete('pt_2dTUV')  
    except:
        pass


def setCheckerTextureRepeat (u, v):
    
    ChangeResult = []
    
    for j in range(1, 4):    
        
        Type = "0" + str(j)
                
        if cmds.objExists( 'pt_2dTexture_' + Type ) == True:
            try:
                cmds.setAttr('pt_2dTexture_' + Type + '.repeatU', u)
                cmds.setAttr('pt_2dTexture_' + Type + '.repeatV', v)
                ChangeResult.append(True)
            except:
                cmds.warning("PolygonTools. Cant repeat pt_2dTexture_" + Type + " UV!")
        else:
            ChangeResult.append(False)
    
    return ChangeResult        
                

def checkShaderIntegrity(CheckerType):
    
    Type = CheckerType
    
    ShaderIntegrity = []
    
    if (cmds.objExists('pt_shading_group_type_' + Type) == True):
        ShaderIntegrity.append(True)
    else:
        ShaderIntegrity.append(False)
        
    if (cmds.objExists('pt_checker_shader_' + Type) == True):
        ShaderIntegrity.append(True)
    else:
        ShaderIntegrity.append(False)
    
    if (cmds.objExists('pt_2dTexture_'  + Type) == True):
        ShaderIntegrity.append(True)
    else:
        ShaderIntegrity.append(False)
    
    if (cmds.objExists('pt_checker_texture_' + Type) == True):
        ShaderIntegrity.append(True)
    else:
        ShaderIntegrity.append(False)
        
    if sum(ShaderIntegrity) == 4:
        print "PolygonTools. Checker Shader", Type, "integrity ok!"
        return True
    elif sum(ShaderIntegrity) in range(1, 4):
        print "PolygonTools. Checker Shader", Type, "integrity broken!"
        return False        
    elif sum(ShaderIntegrity) == 0:                
        return 0
                        

def checkCheckerTextureFile (FilePath):    
    
    try:
        os.path.getsize(FilePath)
        CheckFileResult = True
    except:
        cmds.warning(FilePath + " not exist. Check files. Try to re-install PolygonTools.")
        CheckFileResult = False
    
    return CheckFileResult
                

def changeCheckerTexture (CheckerType, SelectedShapes):
    
    #type selector
    if CheckerType == "checker_standard":
        Type = "01"

    if CheckerType == "checker_digital":
        Type = "02"

    if CheckerType == "checker_diagonal":
        Type = "03"

    if CheckerType == "checker_gradient":
        Type = "04"        
                 
    CurrentDir = os.path.dirname(__file__) 

    PathToCheckerFile = CurrentDir + "/" + CheckerType + ".tga"

    #turn on textures in viewport
    CurrentState = cmds.modelEditor('modelPanel4', q = True, displayTextures=True)
    
    if CurrentState == False:
        cmds.modelEditor( modelPanel='modelPanel4', da="smoothShaded", displayTextures=True, displayLights="default", cameras=False, activeView=True)

    
    #check files
    if checkCheckerTextureFile (PathToCheckerFile) == True:

        cmds.setAttr('pt_checker_texture_' + Type + '.fileTextureName', PathToCheckerFile , type="string")
        
        #assign to all selected shapes
        for i in range(len(SelectedShapes)):            
            cmds.sets(SelectedShapes[i], e=True, forceElement='pt_shading_group_type_' + Type)
            
        ChangeCheckerResult = True
        
    else:
        ChangeCheckerResult = False
        cmds.warning ("PolygonTools. Checker texture not found. Check files or try to re-install PolygonTools.")
            
    return ChangeCheckerResult


def createCheckerMaterial(CheckerType):
    
    #set tupe
    Type = CheckerType
    
    #delete all checkers
    try:
        cmds.delete('pt_shading_group_type_' + Type)
    except:
        pass
    
    try:
        cmds.delete('pt_checker_shader_' + Type)
    except:
        pass                
    
    try:
        cmds.delete('pt_checker_texture_' + Type)
    except:
        pass
    
    try:
        cmds.delete('pt_2dTexture_' + Type)
    except:
        pass
    

    #create if not exists        
    if cmds.objExists( 'pt_shading_group_type_' + Type ) == False:
        try:        
            PT2DTexture = cmds.shadingNode('place2dTexture', name = 'pt_2dTexture_' + Type, asUtility = True)
            PTCheckerTexture = cmds.shadingNode('file', name = 'pt_checker_texture_' + Type, asTexture = True)
            PTCheckerShader = cmds.shadingNode('lambert', asShader = True, name = "pt_checker_shader_" + Type)
                        
            cmds.setAttr('pt_checker_texture_' + Type + '.fileTextureName', "" , type = "string")
                        
            PTShadingGroup = cmds.sets (name = 'pt_shading_group_type_' + Type, renderable = True, empty = True)
            cmds.disconnectAttr( 'lambert1.outColor', 'pt_shading_group_type_' + Type + '.surfaceShader' )
                               
            cmds.connectAttr('pt_checker_shader_' + Type + '.outColor','pt_shading_group_type_' + Type + '.surfaceShader')
            cmds.connectAttr('pt_checker_texture_' + Type + '.outColor','pt_checker_shader_' + Type + '.color')
            cmds.connectAttr('pt_2dTexture_' + Type + '.outUV','pt_checker_texture_' + Type + '.uvCoord')            
            
            print "PolygonTools. Material for checker type", CheckerType, "was created!"
            
            CreateCheckerMaterial = True
        except:
            print "PolygonTools. Can't create material for checker type", CheckerType
            
            CreateCheckerMaterial = False
    
    return CreateCheckerMaterial
    
    
def getCurrentShader (SelectedShapes):
    
    PreviousShadersArray = []
    ObjectsWithShadersArray = []
    
    SkipNames = ['pt_shading_group_type_01', 'pt_shading_group_type_02', 'pt_shading_group_type_03', 'pt_shading_group_type_04']
    
    for i in range(len(SelectedShapes)):
        #try to get shader
        try:
            CurShader = cmds.listConnections(SelectedShapes[i], type='shadingEngine')[0]
        except:
            CurShader = 'initialShadingGroup'
        
        #print CurShader 
        if CurShader not in SkipNames:
            PreviousShadersArray.append(CurShader)
        else:
            PreviousShadersArray.append('initialShadingGroup')
        
        ObjectsWithShadersArray.append(SelectedShapes[i])    
    
    return PreviousShadersArray, ObjectsWithShadersArray
    

def check2DNodes():
    
    Nodes = 0
    
    for i in range (1,4):
    
        Type = "0" + str(i)
    
        if cmds.objExists( 'pt_2dTexture_' + Type ) == True:
            Nodes += 1
    
    return Nodes

# Scale
def scaleUV ( SelectedShapes, Action, sU, sV ):
    
    print "UV Scale:"

    try:
        for i in range(len(SelectedShapes)):
            SelectedFacesTemp = [ SelectedShapes[i] + '.f[:]']
            cmds.select(SelectedFacesTemp)
            cmds.polyEditUV( pivotU=0, pivotV=0, scaleU=sU, scaleV=sV )
            print "PolygonTools. UV successfully scaled", Action, "for", gen_func.shortNamer(SelectedShapes[i])
        
        cmds.select(SelectedShapes)

    except:
        pass

# Move
def moveUV ( SelectedShapes, Action, vU, vV ):
    
    print "UV Move:"
    
    try:
        for i in range(len(SelectedShapes)):
            SelectedFacesTemp = [ SelectedShapes[i] + '.f[:]']
            cmds.select(SelectedFacesTemp)
            cmds.polyEditUV( uValue = vU, vValue = vV )
            print "PolygonTools. UV successfully moved", Action, "for", gen_func.shortNamer(SelectedShapes[i])
        
        cmds.select(SelectedShapes)

    except:
        pass
