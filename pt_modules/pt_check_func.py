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

import pt_conclusion as conclusion
reload(conclusion)

import pt_gen_func as gen_func
reload(gen_func)

sys.path.append('..')
import pt_config_loader as cfgl
reload(cfgl)

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtUiTools import *

#GUI    
class PT_Check_Tab (QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent=parent)
        
        #set layoit
        self.tabCheck_v_layout = QVBoxLayout(self)
        self.tabCheck_v_layout.setAlignment(Qt.AlignTop)
        self.tabCheck_v_layout.setContentsMargins(0,10,0,10)
        self.tabCheck_v_layout.setSpacing(5)

        currentDir = os.path.dirname(__file__)
        try:
            iconChecker  = QPixmap(currentDir +"/icons/checker_icon.png")
        except:
            cmds.warning( "PolygonTools: Can't load icons for Checker Tab! Check icon files in pt_modules/icons directory.")
        
        self.btnCheck = QPushButton("Check")
        self.btnCheck.setMaximumWidth(75)
        self.btnCheck.setIcon(iconChecker)
        self.btnCheck.setStyleSheet("background-color:#375218;")
        
        self.pbChekProgress = QProgressBar()
        self.pbChekProgress.setRange(0,100)
        self.pbChekProgress.setValue(0)
        self.pbChekProgress.setMaximumWidth(255)

                
        self.lblInfo = QLabel("Please select one ore more Mesh objects and press Check button.")
        self.lblInfo.setMinimumHeight(20)
        self.lblInfo.setMargin(5)
        
        self.tabCheck_h_layout_01 = QHBoxLayout()
        self.tabCheck_h_layout_01.setAlignment(Qt.AlignLeft)
        self.tabCheck_h_layout_01.setContentsMargins(0,0,0,0)
        self.tabCheck_h_layout_01.setSpacing(10)       
        
        self.tabCheck_v_layout.addLayout(self.tabCheck_h_layout_01)
        
        self.tabCheck_h_layout_01.addWidget(self.btnCheck)
        self.tabCheck_h_layout_01.addWidget(self.pbChekProgress)
        
        self.tabCheck_v_layout.addWidget(self.lblInfo)
    
        #colors
        global green
        green = ("<font color='#8dc63f'>" + u'\N{Full Block}' + "</font>")
        
        global red
        red = ("<font color='#ed1c24'>" + u'\N{Full Block}' + "</font>")
        
        global black
        black = ("<font color='#000000'>" + u'\N{Full Block}' + "</font>")
        
        global orange
        orange = ("<font color='#ff5001'>" + u'\N{Full Block}' + "</font>")
        
        global yellow
        yellow = ("<font color='#ffd101'>" + u'\N{Full Block}' + "</font>")
        

        global ckecksText
        ckecksText = []
        
        global checkLabels
        checkLabels = []

        global checkMarks
        checkMarks = []
        
        global fixButtons
        fixButtons = []
        
        checkLayouts = []
        
        #Checks
        ckecksText.append("1. Correct system units")
        ckecksText.append("2. Correct file, object and material name.")
        ckecksText.append("3. Pivot should be in the Center of coordinates [0,0,0]")
        ckecksText.append("4. Pivot inside of Objects Bounding Box")
        ckecksText.append("5. No hidden objects and layers on scene")
        ckecksText.append("6. Backface Culling enabled")
        ckecksText.append("7. The object hasn\'t transformation")
        ckecksText.append("8. Correct Polygons")
        ckecksText.append("9. Correct Material on the scene")
        ckecksText.append("10. UV shells in [0,1] area")
        ckecksText.append("11. Quantity of UV Sets")
        ckecksText.append("12. UV-utilization")
        
        #create checks structure
        for i in range(len(ckecksText)):
            
            #create labels names
            label_name = "self.lblItem_" + ckecksText[i]
            
            #label mark
            label_mark = "self.lblItem_Mark_" + ckecksText[i]
            
            #fix button
            fix_but_name = "self.btnFixItem_" + ckecksText[i]
            
            #create layouts names
            layout_name =  "self.tabCheck_h_lay_" + ckecksText[i]
            
            #create label
            label_name = QLabel()

            #add to array
            checkLabels.append(label_name)
            
            #create mark
            label_mark = QLabel()
            label_mark.setText( black )
            #add to array
            checkMarks.append(label_mark)
            
            #create button
            fix_but_name = QPushButton("Fix")
            fix_but_name.setEnabled(False)
            fix_but_name.setMaximumHeight(20)
            fixButtons.append(fix_but_name)
            
            #set check text
            label_name.setText(ckecksText[i])
            label_name.setFixedWidth(290)
            
            #create layout
            layout_name = QHBoxLayout()
            layout_name.setAlignment(Qt.AlignLeft)
            layout_name.setContentsMargins(0,10,0,0)
            layout_name.setSpacing(10)
            
            #add to array
            checkLayouts.append(layout_name)
            
            #add layout
            self.tabCheck_v_layout.addLayout(layout_name)
            
            #add label to layout
            layout_name.addWidget(label_name)
            layout_name.addWidget(label_mark)
            layout_name.addWidget(fix_but_name)
    
        self.gboxCheckerConclusion = QGroupBox("Conclusion")
        self.gboxCheckerConclusion.setMaximumWidth(340)
        self.gboxCheckerConclusion.setMinimumHeight(170)
        self.gboxCheckerConclusion_v_layout = QVBoxLayout()        

        #conclusion text here
        self.txtbrowCheckerConclusion = QTextBrowser()
        self.txtbrowCheckerConclusion.setHtml("")

        self.gboxCheckerConclusion_v_layout.addWidget(self.txtbrowCheckerConclusion)    

        self.gboxCheckerConclusion.setLayout(self.gboxCheckerConclusion_v_layout)

        self.tabCheck_v_layout.addWidget(self.gboxCheckerConclusion)     

        #SIGNALS
        self.btnCheck.clicked.connect(self.btnCheckClicked)
        
        fixButtons[0].clicked.connect(self.unitsFix01)
        fixButtons[2].clicked.connect(self.pivotPointFix03)
        fixButtons[3].clicked.connect(self.pivotInsideBBoxFix04)
        fixButtons[4].clicked.connect(self.hiddenfrozenObjectsFix05)
        fixButtons[5].clicked.connect(self.backFaceCullingFix06)
        fixButtons[6].clicked.connect(self.transformationFix07)
        fixButtons[7].clicked.connect(self.correctPolygonsFix08)
        fixButtons[8].clicked.connect(self.materialFix09)
        
        #no fixable
        fixButtons[1].setText("     ")
        fixButtons[9].setText("     ")
        fixButtons[10].setText("     ")
        fixButtons[11].setText("     ")

        #arrays
        self.ObjWithPivotError = []
        self.ObjWithBBoxError = []
        self.ObjWithBackCull = []
        self.ObjWithTransform = []
        self.ObjWithPolyErrors = []
        self.ObjWithMatProblems = []
        self.ObjWithManyUVSets = []
        self.AllUVAreas = []
        self.hiddenObjects = []
        self.CheckErrorCount = []

        #intro text
        current_language = cfgl.configLoader()[14]
        self.txtbrowCheckerConclusion.setHtml(conclusion.checkerTabIntroConclusion(current_language))

    #set check result to Zero
    def zeroResult(self):        
        for i in range(len(ckecksText)):
            checkLabels[i].setText(ckecksText[i])
            checkMarks[i].setText( black )
            fixButtons[i].setEnabled(False)
        
        self.pbChekProgress.setValue(0)
        self.lblInfo.setStyleSheet("")
        
    def btnCheckClicked (self):

        current_language = cfgl.configLoader()[14]        
        
        SelectionData = gen_func.checkSelection()
        
        SelectedShapes = SelectionData[0]

                
        if len(SelectedShapes) > 0:

            CheckConclusion = []
            self.CheckErrorCount = []
            
            print "PolygonTools. Check start!"
            print ""

            if len(SelectedShapes) == 1:
                self.lblInfo.setText(gen_func.shortNamer(SelectedShapes[0]) + " will be checked.")
            elif len(SelectedShapes) > 1:
                self.lblInfo.setText(str(len(SelectedShapes)) + " objects will be checked.")
            
            cmds.delete( ch=True )
            
            CheckConclusion.append(self.unitsCheck01())
            self.pbChekProgress.setValue(7)
            print checkLabels[0].text()

            LongLine = "------------------------------"
            print LongLine
            
            #names
            CheckConclusion.append(self.namesCheck02(SelectedShapes))            
            self.pbChekProgress.setValue(14)
            print checkLabels[1].text() 

            print LongLine
            
            #pivot
            CheckConclusion.append(self.pivotPointPos03(SelectedShapes))
            self.pbChekProgress.setValue(21)
            print checkLabels[2].text()

            print LongLine
            
            CheckConclusion.append(self.pivotInsideBBox04(SelectedShapes))
            self.pbChekProgress.setValue(28)
            print checkLabels[3].text()
            
            print LongLine
            
            #freeze
            CheckConclusion.append(self.hiddenfrozenObjects05())
            self.pbChekProgress.setValue(35)
            print checkLabels[4].text()
            
            print LongLine
            
            CheckConclusion.append(self.backFaceCulling06(SelectedShapes))
            self.pbChekProgress.setValue(42)
            print checkLabels[5].text()

            print LongLine
            
            CheckConclusion.append(self.transformationCheck07(SelectedShapes))
            self.pbChekProgress.setValue(49)
            print checkLabels[6].text()

            print LongLine
            
            CheckConclusion.append(self.correctPolygonsCheck08(SelectedShapes))
            self.pbChekProgress.setValue(56)
            print checkLabels[7].text()

            print LongLine
            
            CheckConclusion.append(self.materialCheck09(SelectedShapes))
            self.pbChekProgress.setValue(63)
            print checkLabels[8].text()

            print LongLine
            
            CheckConclusion.append(self.uvBorderCheck10(SelectedShapes))
            self.pbChekProgress.setValue(70)
            print checkLabels[9].text()

            print LongLine
            
            CheckConclusion.append(self.uvSetsCountCheck11(SelectedShapes))
            self.pbChekProgress.setValue(77)
            print checkLabels[10].text()

            print LongLine
            
            CheckConclusion.append(self.uvUtilCheck12(SelectedShapes))
            self.pbChekProgress.setValue(84)
            print checkLabels[11].text()

            print LongLine
            
            self.pbChekProgress.setValue(100)

            try:
                cmds.select(SelectedShapes)
            except:
                cmds.select(clear=True)

            FoundErrors = sum(self.CheckErrorCount)/len((self.CheckErrorCount))

            conclusion_text = conclusion.checkResult(current_language, CheckConclusion)
            self.txtbrowCheckerConclusion.setHtml(conclusion_text) 
            
            if len(SelectedShapes) == 1:
                self.lblInfo.setText("Check complete for " + str(gen_func.shortNamer(SelectedShapes[0])) + " mesh. " + str(FoundErrors) + " check errors.")
            if len(SelectedShapes) > 1:
                self.lblInfo.setText("Check complete for " + str(len(SelectedShapes)) + " objects. " + str(FoundErrors) + " check errors. See log for details.")

            self.lblInfo.setStyleSheet("background-color:#598527;")
            print "PolygonTools.", self.lblInfo.text()
            print "-------------"

        else:
            conclusion_text = conclusion.noSelection(current_language, "checker")
            self.txtbrowCheckerConclusion.setHtml(conclusion_text) 
            self.lblInfo.setText("To start checking please select one or more mesh objects!")     
            cmds.warning(self.lblInfo.text())   
            self.zeroResult()

    #1 Units checker
    def unitsCheck01 (self):

        #get Units custom and current
        try:
            custom_sys_units = cfgl.configLoader()[9]
            cur_work_units = cmds.currentUnit(query=True)

            if custom_sys_units == cur_work_units:
                checkMarks[0].setText( green )
                fixButtons[0].setEnabled(False)
                checkLabels[0].setText('1. System units is correct. It\'s \"' + cur_work_units + "\"")            
                return True
            else:
                checkMarks[0].setText( red )
                fixButtons[0].setEnabled(True)
                checkLabels[0].setText('1. System units is not correct. It\'s \"' + cur_work_units + "\"")    
                return False

        except:
            cmds.warning("PolygonTools. Problem with units checking.")
            self.CheckErrorCount.append(1)
        
        
    #1 Units fixer
    def unitsFix01(self):

        try:
            #get custom units
            custom_sys_units = cfgl.configLoader()[9]
            
            #set custom units
            cmds.currentUnit( linear=custom_sys_units )
            
            checkMarks[0].setText( green )
            fixButtons[0].setEnabled(False)
            checkLabels[0].setText('1. System units is fixed. Now It\'s \"' + custom_sys_units + "\"")
            
            self.lblInfo.setText ('System units is fixed. Now It\'s \"' + custom_sys_units + "\"")
            print  "PolygonTools.", self.lblInfo.text()

            conclusion_text = conclusion.fixConclusion(current_language, "1", True)
            self.txtbrowCheckerConclusion.setHtml(conclusion_text) 
        except:
            cmds.warning ("PolygonTools. Can\'t fix system units.")
            conclusion_text = conclusion.fixConclusion(current_language, "1", False)
            self.txtbrowCheckerConclusion.setHtml(conclusion_text) 


    #2 Names
    def namesCheck02 (self, SelectedShapes):
        
        #names error array
        try:
            NameErrors = namesChecker(SelectedShapes)
        except:
            checkMarks[1].setText( red )
            checkLabels[1].setText("2. Can't check names")
            cmds.warning ("PolygonTools. Can\'t check names.")
            self.CheckErrorCount.append(1)

        if len(NameErrors) == 0:
            checkMarks[1].setText( green )
            checkLabels[1].setText('2. Names is normal or correct')
            return True
        
        #show errors
        if len(NameErrors) == 1:
            checkMarks[1].setText( yellow )
            checkLabels[1].setText('2. Check: ' + NameErrors[0])
            return False
        elif len(NameErrors) > 1:
            checkMarks[1].setText( orange )
            all_errors = ""
            all_errors = (', '.join(NameErrors))
            checkLabels[1].setText('2. Check: ' + all_errors)
            return False

    #3 Pivot Point
    def pivotPointPos03 (self, SelectedShapes):

        Errors = []
        
        self.ObjWithPivotError = []
        
        #get world space pivot point
        for i in range(len(SelectedShapes)):

            if cmds.objExists(SelectedShapes[i]) == True:
                #get all array
                ParentsArray = cmds.ls(SelectedShapes[i], long=True)[0].split('|')[1:-1]
                #get split names
                TransformNameArray = ['|'.join(ParentsArray[:i]) for i in xrange(1, 1 + len(ParentsArray))]
                 
                for k in range(len(TransformNameArray)):
                    pivot_point_pos = cmds.xform ( TransformNameArray[k], q=True, ws=True, pivots=True )
    
                    if sum(pivot_point_pos) != 0:
                        self.ObjWithPivotError.append(TransformNameArray[k])
                        print len(self.ObjWithPivotError), "-", TransformNameArray[k], "- check the Pivot Point position | Scale", pivot_point_pos[0:3], "| Rotate", pivot_point_pos[3:6]    
            else:
                Errors.append(SelectedShapes[i])

        self.CheckErrorCount.append(len(Errors))
        
        if len(Errors) > 0:
            print ""
            print "ATTENTION! These objects have not been checked because they do not exist or contain serious errors (", len(Errors), "):"
            print ('\n'.join(Errors)) 
            
        print ""

        if len(self.ObjWithPivotError) == 0:
            checkMarks[2].setText( green )
            checkLabels[2].setText('3. Pivot in the center of coordinates [0,0,0]')
            fixButtons[2].setEnabled(False)
            return True
        else:
            checkMarks[2].setText( yellow )
            checkLabels[2].setText('3. Check the Pivot Point position (' +str(len(self.ObjWithPivotError)) + ")")
            fixButtons[2].setEnabled(True) 
            print len(self.ObjWithPivotError), "objects found with problems."
            #print ('\n'.join(self.ObjWithPivotError))   
            #print "Objects with problems:", self.ObjWithPivotError
            print ""
            return False


    #3 FIX
    def pivotPointFix03 (self):

        current_language = cfgl.configLoader()[14]        

        print "---"

        FixResult = []

        if len(self.ObjWithPivotError) > 0:
            
            print "Fix Pivot list:"
            
            for i in range(len(self.ObjWithPivotError)):

                if cmds.objExists(self.ObjWithPivotError[i]) == True:   
                                                         
                    try:
                        cmds.xform(self.ObjWithPivotError[i], ws=True, pivots=(0, 0, 0) )
                        cmds.makeIdentity(self.ObjWithPivotError[i], apply=True, t=1)
                        cmds.delete(self.ObjWithPivotError[i], ch=True )
                        print self.ObjWithPivotError[i], "- Pivot Point position fixed."
                    except:
                        print "ERROR:",self.ObjWithPivotError[i], "- not fixed. Object possibly deleted or renamed."
                        FixResult.append(self.ObjWithPivotError[i])
                else:
                    cmds.warning("PolygonTools. Object " + str(self.ObjWithPivotError[i]) + " not exists!")
                    FixResult.append(self.ObjWithPivotError[i])
            
            #one or many objects
            if len(self.ObjWithPivotError) == 1 and len(FixResult) == 0:
                self.lblInfo.setText("Pivot point position fixed for " + str(gen_func.shortNamerTransform(self.ObjWithPivotError[0])) + " transform.")                
            elif len(self.ObjWithPivotError) > 1 and len(FixResult) == 0:
                self.lblInfo.setText("Pivot point position fixed for " + str(len(self.ObjWithPivotError)) + " transforms.")

            print ""

            #problem with fix
            if len(FixResult) == 0:
                checkMarks[2].setText( green )
                checkLabels[2].setText('3. Pivot point position fixed. Now it\'s [0,0,0]')
                fixButtons[2].setEnabled(False)
                print self.lblInfo.text(), "Now it\'s [0,0,0]"
                conclusion_text = conclusion.fixConclusion(current_language, "3", True)
                self.txtbrowCheckerConclusion.setHtml(conclusion_text) 
                print "---"
                self.pivotInsideBBox04(self.ObjWithPivotError) #run 4
            else:
                checkMarks[2].setText( red )
                checkLabels[2].setText("3. Can't Fix Pivot point position for " + str(len(FixResult)) + "objects")
                fixButtons[2].setEnabled(False)
                self.lblInfo.setText("Fix Error. Object(s) possibly deleted or renamed. See log.")
                self.lblInfo.setStyleSheet("background-color:#ed1c24;")
                print "PolygonTools:", self.lblInfo.text()
                print "---"
                conclusion_text = conclusion.fixConclusion(current_language, "3", False)
                self.txtbrowCheckerConclusion.setHtml(conclusion_text) 

    #4 
    def pivotInsideBBox04 (self, SelectedShapes):

        self.ObjWithBBoxError = []

        Errors = []
        
        for i in range(len(SelectedShapes)):          
            if cmds.objExists(SelectedShapes[i]) == True:
                #get all array
                ParentsArray = cmds.ls(SelectedShapes[i], long=True)[0].split('|')[1:-1]
                #get split names
                TransformNameArray = ['|'.join(ParentsArray[:i]) for i in xrange(1, 1 + len(ParentsArray))]
                                 
                for k in range(len(TransformNameArray)):
                    #get bbox size
                    bbox = cmds.exactWorldBoundingBox(TransformNameArray[k])
                
                    #get pivot position
                    pivot_point_pos = cmds.xform(TransformNameArray[k], q=True, ws=True, pivots=True)
                                    
                    #if pivot ccords in range of min-max bbox                    
                    if (bbox[1] <= pivot_point_pos[1] <= bbox[4]) and \
                    (bbox[0] <= pivot_point_pos[0] <= bbox[3]) and \
                    (bbox[2] <= pivot_point_pos[2] <= bbox[5]):
                        pass
                    else:
                        #print TransformName, "- Pivot Point outside of objects bounding box."
                        self.ObjWithBBoxError.append(TransformNameArray[k])
            else:
                Errors.append(SelectedShapes[i])

        self.CheckErrorCount.append(len(Errors))
                
        if len(Errors) > 0:
            print ""
            print "ATTENTION! These objects have not been checked because they do not exist or contain serious errors (", len(Errors), "):"
            print ('\n'.join(Errors)) 
        
        print ""
        

        if len(self.ObjWithBBoxError) == 0:
            checkMarks[3].setText( green )
            checkLabels[3].setText('4. Pivot inside of objects Bounding Box')
            fixButtons[3].setEnabled(False)
            return True
        else:
            checkMarks[3].setText( yellow )
            checkLabels[3].setText('4. Check Pivot. It\'s outside of objects Bounding Box (' + str(len(self.ObjWithBBoxError))+")")
            fixButtons[3].setEnabled(True)    
            print "Objects with Pivot Point outside of BoundigBox:"
            print ('\n'.join(self.ObjWithBBoxError)) 
            print ""
            print len(self.ObjWithBBoxError), "objects found with problems."
            print ""
            return False

    #4 FIX
    def pivotInsideBBoxFix04 (self):

        current_language = cfgl.configLoader()[14] 

        print "---"

        FixResult = []
        
        if len(self.ObjWithBBoxError) > 0:

            print "Fix Pivot Point position relative to BBox:"
            

            for i in range(len(self.ObjWithBBoxError)):    
                if cmds.objExists(self.ObjWithBBoxError[i]) == True:        
                    try:
                        #set pivot to center
                        cmds.xform(self.ObjWithBBoxError[i], centerPivots=True)
                        
                        #freezw transform
                        cmds.makeIdentity(self.ObjWithBBoxError[i], apply=True, t=1)

                        #del history
                        cmds.delete(self.ObjWithBBoxError[i], ch=True )

                        print self.ObjWithBBoxError[i], "- pivot point position fixed."
                    except:
                        print "ERROR:", self.ObjWithBBoxError[i], "- not fixed. Object possibly deleted or renamed."
                        FixResult.append(self.ObjWithBBoxError[i])
                else:
                    cmds.warning("PolygonTools. Object " + str(self.ObjWithBBoxError[i]) + " not exists!")
                    FixResult.append(self.ObjWithBBoxError[i])

            print ""

            if len(self.ObjWithBBoxError) == 1 and len(FixResult) == 0:
                self.lblInfo.setText("Pivot inside of " + str(gen_func.shortNamerTransform(self.ObjWithBBoxError[0])) + " transform BBox.")
            elif len(self.ObjWithBBoxError) > 1 and len(FixResult) == 0:
                self.lblInfo.setText("Pivot inside of " + str(len(self.ObjWithBBoxError)) + " transforms BBoxes.")

            if len(FixResult) == 0:
                checkMarks[3].setText( green )
                checkLabels[3].setText('4. Fixed. Pivot inside of objects bounding box')
                fixButtons[3].setEnabled(False)
                conclusion_text = conclusion.fixConclusion(current_language, "4", True)
                self.txtbrowCheckerConclusion.setHtml(conclusion_text) 
                print self.lblInfo.text()
                self.pivotPointPos03(self.ObjWithBBoxError) #run 3
            else:
                checkMarks[3].setText( red )
                checkLabels[3].setText("4. Can't Fix pivot for " + str(len(self.ObjWithBBoxError)) + " objects")
                fixButtons[3].setEnabled(False)
                self.lblInfo.setText("Fix Error. Object(s) possibly deleted or renamed. See log.")
                self.lblInfo.setStyleSheet("background-color:#ed1c24;")
                print "PolygonTools:", self.lblInfo.text()            
                conclusion_text = conclusion.fixConclusion(current_language, "4", False)
                self.txtbrowCheckerConclusion.setHtml(conclusion_text) 

            print "---"            
    
    #5    
    def hiddenfrozenObjects05(self):

        Errors = []

        try:
            #get all hidden objects
            hiddenNodes=[]
            hiddenNodes = cmds.ls(invisible=True, type="transform")
            
            #standard names
            std_names = ['front','persp','side','top', 'transform']

            #only objects
            self.hiddenObjects = []
            self.hiddenObjects = [s for s in hiddenNodes if not any(xs in s for xs in std_names)]
            
            cmds.isolateSelect( 'modelPanel1', state=0 )
            cmds.isolateSelect( 'modelPanel2', state=0 )
            cmds.isolateSelect( 'modelPanel3', state=0 )
            cmds.isolateSelect( 'modelPanel4', state=0 )
            
            #unhide layers and make it normal
            layers = cmds.ls( type='displayLayer')
            
            #layer format
            layerFormat = []
            
            #layer visibility
            layerVis = []
            
            #get layer info
            for x in layers[1:]:
                #get layer Format - Normal is correct
                layerFormat.append(cmds.getAttr("{}.displayType".format(x)))
                
                #get layer visibility - True is correct
                visVal = cmds.getAttr( '%s.visibility' % x)
                
                if visVal==False:
                    layerVis.append(visVal)
                    print x, "- layer is hidden."
        except:
            Errors.append(1)

        self.CheckErrorCount.append(len(Errors))
        
        if len(self.hiddenObjects) > 0:
            print ""
            print "Hidden objects:", self.hiddenObjects
            print ""

        #we check hidden objects, hidden layers 
        if (len(self.hiddenObjects)==0) and (sum(layerFormat)==0) and (len(layerVis)==0):
            checkMarks[4].setText( green )
            checkLabels[4].setText('5. No hidden objects and layers on scene')
            fixButtons[4].setEnabled(False)
            return True
        else:
            checkMarks[4].setText( red )
            checkLabels[4].setText('5. Check hidden objects or layers on scene')
            fixButtons[4].setEnabled(True)
            return False
     
    #5 FIX
    def hiddenfrozenObjectsFix05(self):

        current_language = cfgl.configLoader()[14] 

        print "---"
        print "Fix result:"
        
        FixResult = []

        #unhide
        for i in range(len(self.hiddenObjects)):
            if cmds.objExists(self.hiddenObjects[i]) == True:
                cmds.showHidden( self.hiddenObjects[i] )
                print self.hiddenObjects[i], "unhidden."
            else:
                cmds.warning("PolygonTools. Object " + str(self.hiddenObjects[i]) + " not exists!")
                FixResult.append(self.hiddenObjects[i])
        
        layers = cmds.ls( type='displayLayer')
       
        #set correct values
        for x in layers[1:]:
            cmds.setAttr( '%s.visibility' % x, 1)
            cmds.setAttr("{}.displayType".format(x), 0)

        if len(FixResult) == 0:
            checkMarks[4].setText( green )
            checkLabels[4].setText('5. Fixed. All objects and layers unhidden')
            fixButtons[4].setEnabled(False)
            self.lblInfo.setText("Fixed. All objects and layers unhidden.")
            
            conclusion_text = conclusion.fixConclusion(current_language, "5", True)
            self.txtbrowCheckerConclusion.setHtml(conclusion_text) 

            print "PolygonTools:", self.lblInfo.text()
        else:
            checkMarks[4].setText( red )
            checkLabels[4].setText("5. Can't Fix all hidden objects and layers")
            fixButtons[4].setEnabled(False)
            self.lblInfo.setText("Can't Fix all hidden objects and layers")
            self.lblInfo.setStyleSheet("background-color:#ed1c24;")

            conclusion_text = conclusion.fixConclusion(current_language, "5", False)
            self.txtbrowCheckerConclusion.setHtml(conclusion_text) 

            print "PolygonTools:", self.lblInfo.text()


    #6
    def backFaceCulling06(self, SelectedShapes):

        Errors = []

        self.ObjWithBackCull = []
        
        #get backface
        for i in range(len(SelectedShapes)):
            if cmds.objExists(SelectedShapes[i]) == True:
                try:
                    bfc = cmds.displayCull(SelectedShapes[i], q=True)
                except:
                    pass
                
                if bfc == False:
                    if len(self.ObjWithBackCull) == 0:
                        print "Backface Culling disabled for:" 
                    print gen_func.shortNamer(SelectedShapes[i])
                    self.ObjWithBackCull.append(SelectedShapes[i])
            else:
                Errors.append(SelectedShapes[i])

        self.CheckErrorCount.append(len(Errors))

        if len(Errors) > 0:
            print ""
            print "ATTENTION! These objects have not been checked because they do not exist or contain serious errors (", len(Errors), "):"
            print ('\n'.join(Errors)) 
        
        print ""

        #one or many objects
        if len(self.ObjWithBackCull) == 0:
            checkMarks[5].setText( green )
            checkLabels[5].setText("6. Backface Culling enabled")
            fixButtons[5].setEnabled(False)
            return True
        else:
            checkMarks[5].setText( yellow )
            checkLabels[5].setText("6. Backface Culling disabled (" + str(len(self.ObjWithBackCull)) + ")")
            fixButtons[5].setEnabled(True)
            return False
            
    #6 FIX
    def backFaceCullingFix06(self):

        current_language = cfgl.configLoader()[14] 

        FixResult = []

        print "---"
        print "Fix result:"
        
        for i in range(len(self.ObjWithBackCull)):
            if cmds.objExists(self.ObjWithBackCull[i]) == True:
                try:
                    cmds.displayCull(self.ObjWithBackCull[i],  bfc=True )
                    print gen_func.shortNamer(self.ObjWithBackCull[i]), "Backface Culling enabled." 
                except:
                    print "ERROR:", gen_func.shortNamer(self.ObjWithBackCull[i]), "can't turn ON Backface Culling. Object possibly deleted or renamed." 
                    FixResult.append(self.ObjWithBackCull[i])
            else:
                FixResult.append(self.ObjWithBackCull[i])
                cmds.warning("PolygonTools. Object " + str(self.ObjWithBackCull[i]) + " not exists!")

        print ""
        
        #one or many objects
        if len(self.ObjWithBackCull) == 1 and len(FixResult) == 0:
            self.lblInfo.setText("Backface Culling enabled for " + str(self.ObjWithBackCull[0]))
        if len(self.ObjWithBackCull) > 1 and len(FixResult) == 0:
            self.lblInfo.setText("Backface Culling enabled for " + str(len(self.ObjWithBackCull)) + " objects.")

        if len(FixResult) == 0:            
            checkMarks[5].setText( green )
            checkLabels[5].setText("6. Fixed. Backface Culling enabled")
            fixButtons[5].setEnabled(False)

            conclusion_text = conclusion.fixConclusion(current_language, "6", True)
            self.txtbrowCheckerConclusion.setHtml(conclusion_text) 

            print "PolygonTools:", self.lblInfo.text()
        else:
            checkMarks[5].setText( red )
            checkLabels[5].setText("6. Can't fix Backface Culling for " + str(len(FixResult)) + "object(s)")
            fixButtons[5].setEnabled(False)
            self.lblInfo.setText("Fix Error. Object possibly deleted or renamed. See log.")
            self.lblInfo.setStyleSheet("background-color:#ed1c24;")

            conclusion_text = conclusion.fixConclusion(current_language, "6", False)
            self.txtbrowCheckerConclusion.setHtml(conclusion_text) 

            print "PolygonTools:", self.lblInfo.text()
        
        print "---"

    #7
    def transformationCheck07(self, SelectedShapes):

        Errors = []

        self.ObjWithTransform = []
        
        for i in range(len(SelectedShapes)):            
            if cmds.objExists(SelectedShapes[i]) == True:
                #get all array
                ParentsArray = cmds.ls(SelectedShapes[i], long=True)[0].split('|')[1:-1]
                #get split names
                TransformNameArray = ['|'.join(ParentsArray[:i]) for i in xrange(1, 1 + len(ParentsArray))]
                
                #get all transform matrix
                for k in range(len(TransformNameArray)):
                    
                    transform_matrix=[]
                    transform_matrix = cmds.xform(TransformNameArray[k] , q=True, m=True)
                
                    if sum(transform_matrix) != 4:
                        if len(self.ObjWithTransform) == 0:
                            print "Objects with transformations:" 
                        if TransformNameArray[k] not in self.ObjWithTransform: #add unique only 
                            self.ObjWithTransform.append( TransformNameArray[k] )
                            print len(self.ObjWithTransform), TransformNameArray[k]
                        
            else:
                Errors.append( SelectedShapes[i] )
                
        self.CheckErrorCount.append(len(Errors))

        if len(Errors) > 0:
            print ""
            print "ATTENTION! These objects have not been checked because they do not exist or contain serious errors (", len(Errors), "):"
            print ('\n'.join(Errors))         

        print ""        

        #if 4 - then no transform
        if len(self.ObjWithTransform) == 0:
            checkMarks[6].setText( green )
            checkLabels[6].setText("7. The object(s) hasn\'t transformation")
            fixButtons[6].setEnabled(False)
            return True
        else:
            checkMarks[6].setText( red )
            checkLabels[6].setText("7. The object(s) has transformation (" + str(len(self.ObjWithTransform)) + ")")
            fixButtons[6].setEnabled(True)
            return False

    #7 FIX       
    def transformationFix07(self):

        current_language = cfgl.configLoader()[14] 

        print "---"
        FixResult = []
        print "Fix result:"
        
        if len(self.ObjWithTransform) > 0:
            
            print self.ObjWithTransform
            
            print "Transform freezed for:"
            
            for i in range(len(self.ObjWithTransform)):   
                if cmds.objExists(self.ObjWithTransform[i]) == True:
                    try:
                        #freeze transform
                        cmds.makeIdentity(self.ObjWithTransform[i], apply=True, t=1, r=1, s=1 )
                
                        #del history
                        cmds.delete(self.ObjWithTransform[i], ch=True )

                        print self.ObjWithTransform[i]
                    except:
                        cmds.warning("Cant freeze transform for: " + self.ObjWithTransform[i] + " Try to check incoming connection.")
                        FixResult.append(self.ObjWithTransform[i])
                else:
                    FixResult.append(self.ObjWithTransform[i])
                    cmds.warning("PolygonTools. Object " + str(self.ObjWithTransform[i]) + " not exists!")
                
            print ""

            if len(self.ObjWithTransform) == 1:  
                self.lblInfo.setText("Transformation Freezed for " + str(self.ObjWithTransform[0]))
            elif len(self.ObjWithTransform) > 1:
                self.lblInfo.setText("Transformation Freezed for " + str(len(self.ObjWithTransform)) + " objects.")


            if len(FixResult) == 0:
                checkMarks[6].setText( green )
                checkLabels[6].setText("7. Fixed. Transformation Freezed")
                fixButtons[6].setEnabled(False)

                conclusion_text = conclusion.fixConclusion(current_language, "7", True)
                self.txtbrowCheckerConclusion.setHtml(conclusion_text) 

                print "PolygonTools:", self.lblInfo.text()
            else:
                checkMarks[6].setText( red )
                checkLabels[6].setText("7. Cant Fix Transformation for " + str(len(FixResult)) + " object(s)")
                fixButtons[6].setEnabled(False)
                self.lblInfo.setText("Fix Error. Object possibly deleted or renamed. See log.")
                self.lblInfo.setStyleSheet("background-color:#ed1c24;")

                conclusion_text = conclusion.fixConclusion(current_language, "7", False)
                self.txtbrowCheckerConclusion.setHtml(conclusion_text) 

                print "PolygonTools:", self.lblInfo.text()

            print "---"


    #8
    def correctPolygonsCheck08(self, SelectedShapes):

        self.ObjWithPolyErrors = []
        
        Errors = []
    
        #list of errors
        errors_list = []
        
        for i in range(len(SelectedShapes)):
            
            if cmds.objExists(SelectedShapes[i]) == True:
    
                cmds.select(SelectedShapes[i])
                            
                #ngons
                ngons_list = []
                try:
                    ngons_list = maya.mel.eval('polyCleanupArgList ObjectName { "0","2","1","0","1","0","0","0","0","1e-05","0","1e-05","0","1e-05","0","-1","0","0" };')
                except:
                    pass
                
                if len(ngons_list) != 0:
                    ErrorType = "n-gons"
                    if ErrorType not in errors_list:
                        errors_list.append(ErrorType)
                    if SelectedShapes[i] not in self.ObjWithPolyErrors:
                        self.ObjWithPolyErrors.append(SelectedShapes[i])
                    print gen_func.shortNamer(SelectedShapes[i]), "has N-gon faces."
    
                #re-select    
                cmds.select(SelectedShapes[i])
                
                #concave            
                concave_list = []
                try:
                    concave_list = maya.mel.eval('polyCleanupArgList ObjectName { "0","2","1","0","0","1","0","0","0","1e-05","0","1e-05","0","1e-05","0","-1","0","0" };')
                except:
                    pass
                
                if len(concave_list) != 0:
                    ErrorType = "concave"
                    if ErrorType not in errors_list:
                        errors_list.append(ErrorType)
                    if SelectedShapes[i] not in self.ObjWithPolyErrors:
                        self.ObjWithPolyErrors.append(SelectedShapes[i])
                    print gen_func.shortNamer(SelectedShapes[i]), "has concave faces."
                
                #re-select
                cmds.select(SelectedShapes[i])
                
                #non-planar
                nonplanar_list = []
                try:
                    nonplanar_list = maya.mel.eval('polyCleanupArgList ObjectName { "0","2","1","0","0","0","0","1","0","1e-05","0","1e-05","0","1e-05","0","-1","0","0" };')
                except:
                    pass
    
                if len(nonplanar_list) != 0:
                    ErrorType = "non-planar"
                    if ErrorType not in errors_list:
                        errors_list.append(ErrorType)
                    if SelectedShapes[i] not in self.ObjWithPolyErrors:
                        self.ObjWithPolyErrors.append(SelectedShapes[i])
                    print gen_func.shortNamer(SelectedShapes[i]), "has non-planar faces."
                
                print ""
                    
                #re-select
                cmds.select(SelectedShapes[i])
                
            else:
                Errors.append(SelectedShapes[i])

        self.CheckErrorCount.append(len(Errors))        
        
        if len(Errors) > 0:
            print ""
            print "ATTENTION! These objects have not been checked because they do not exist or contain serious errors (", len(Errors), "):"
            print ('\n'.join(Errors))         
        

        if len(self.ObjWithPolyErrors) == 0:
            checkMarks[7].setText( green )
            checkLabels[7].setText("8. All polygons are correct")
            fixButtons[7].setEnabled(False)
            return True
        else:
            checkMarks[7].setText( red )
            checkLabels[7].setText("8. Check for errors: " + (', '.join(errors_list)) + " | (" + str(len(self.ObjWithPolyErrors)) + ")")
            fixButtons[7].setEnabled(True)
            return False

    #8 Fix    
    def correctPolygonsFix08(self):

        current_language = cfgl.configLoader()[14] 

        print "---"
        FixResult = []
        print "Fix result:"
                
        if len(self.ObjWithPolyErrors) > 0:
            
            for i in range(len(self.ObjWithPolyErrors)):
                if cmds.objExists(self.ObjWithPolyErrors[i]) == True:
                    try:
                        cmds.select(self.ObjWithPolyErrors[i])

                        ObjectName = self.ObjWithPolyErrors[i]

                        #fix
                        maya.mel.eval('polyCleanupArgList ObjectName { "0","1","1","0","1","1","1","1","0","1e-05","0","1e-05","0","1e-05","0","-1","0","0" };')
                        
                        #delhist
                        cmds.delete(ObjectName, constructionHistory=True )

                        print gen_func.shortNamer(self.ObjWithPolyErrors[i]), "fixed."
                    except:
                        print "ERROR:", gen_func.shortNamer(self.ObjWithPolyErrors[i]), "can't fixed."
                        FixResult.append(self.ObjWithPolyErrors[i])
                else:
                    FixResult.append(self.ObjWithPolyErrors[i])
                    cmds.warning("PolygonTools. Object " + str(self.ObjWithPolyErrors[i]) + " not exists!")


        if len(self.ObjWithPolyErrors) == 1 and len(FixResult) == 0:  
            self.lblInfo.setText("Cleanup complete for " + str(self.ObjWithPolyErrors[0]))
        elif len(self.ObjWithPolyErrors) > 1 and len(FixResult) == 0:
            self.lblInfo.setText("Cleanup complete for " + str(len(self.ObjWithPolyErrors)) + " objects.")

        print ""    
        
        if len(FixResult) == 0:
            #return select
            cmds.select (self.ObjWithPolyErrors)
            checkMarks[7].setText( green )
            checkLabels[7].setText("8. Fixed. All polygons are correct")
            fixButtons[7].setEnabled(False)

            conclusion_text = conclusion.fixConclusion(current_language, "8", True)
            self.txtbrowCheckerConclusion.setHtml(conclusion_text) 

            print self.lblInfo.text()
        else:
            #return select
            checkMarks[7].setText( red )
            checkLabels[7].setText("8. Can't fix " + str(len(FixResult)) + " objects")
            fixButtons[7].setEnabled(False)
            self.lblInfo.setText("Fix Error. Object possibly deleted or renamed. See log.")
            self.lblInfo.setStyleSheet("background-color:#ed1c24;")

            conclusion_text = conclusion.fixConclusion(current_language, "8", False)
            self.txtbrowCheckerConclusion.setHtml(conclusion_text) 

            print "PolygonTools:", self.lblInfo.text()
        
        print "---"


    #9
    def materialCheck09(self, SelectedShapes):

        self.ObjWithMatProblems = []       
        
        Errors = []

        print "Assigned material list:" 
        
        lambert = ""
        nomat = ""

        for i in range(len(SelectedShapes)):
            
            if cmds.objExists(SelectedShapes[i]) == True:
                #get material
                cmds.select(SelectedShapes[i])
                MaterialList = cmds.ls( mat=1 )
                InConnections = cmds.listConnections ( SelectedShapes[i], type = "shadingEngine" )
                
                if InConnections != None:
                    AssignedMat = cmds.ls ( cmds.listConnections (InConnections), mat=1 )
                else:
                    AssignedMat = []
    
                if (len(AssignedMat) == 0):
                    self.ObjWithMatProblems.append(SelectedShapes[i])
                    print gen_func.shortNamer(SelectedShapes[i]), "-> without material"
                    nomat = " -no material"
                elif (AssignedMat[0] == "lambert1"):
                     self.ObjWithMatProblems.append(SelectedShapes[i])
                     print gen_func.shortNamer(SelectedShapes[i]), "->", AssignedMat[0] 
                     lambert = " - lambert1"
                else:
                    print gen_func.shortNamer(SelectedShapes[i]), "->", AssignedMat[0]
            else:
                Errors.append(SelectedShapes[i])
                 
        self.CheckErrorCount.append(len(Errors))
        
        if len(Errors) > 0:
            print ""
            print "ATTENTION! These objects have not been checked because they do not exist or contain serious errors (", len(Errors), "):"
            print ('\n'.join(Errors))         
        
        print ""

        if len(self.ObjWithMatProblems) == 0:
            checkMarks[8].setText( green )
            checkLabels[8].setText("9. No problem with materials")
            fixButtons[8].setEnabled(False)
            return True
        else:      #no material or Lambert1
            checkMarks[8].setText( red )
            checkLabels[8].setText("9. Material problems:" + nomat + lambert + " (" + str(len(self.ObjWithMatProblems)) + ")")
            fixButtons[8].setEnabled(True)
            return False
    
    #9 FIX
    def materialFix09(self):

        current_language = cfgl.configLoader()[14] 

        print "---"
        FixResult = []
        print "Fix result:"

        if len(self.ObjWithMatProblems) > 0:
            
            if cmds.objExists('pt_temporary_shader') == False:
                pt_temporary_mat = cmds.shadingNode('blinn', asShader=True, name="pt_temporary_shader")
                cmds.setAttr('pt_temporary_shader'+'.specularColor', 1, 1, 1, type="double3")
                cmds.sets(name='pt_shading_group_temporary', renderable=True, empty=True)
                cmds.defaultNavigation(connectToExisting=True, source='pt_temporary_shader', destination='pt_shading_group_temporary')
                    
            if cmds.objExists('pt_temporary_shader') == True:
                for i in range (len(self.ObjWithMatProblems)):
                    if cmds.objExists(self.ObjWithMatProblems[i]) == True:
                        cmds.sets(self.ObjWithMatProblems[i], e=True, forceElement='pt_shading_group_temporary')
                    else:
                        FixResult.append(self.ObjWithMatProblems[i])
                        cmds.warning("PolygonTools. Object " + str(self.ObjWithMatProblems[i]) + " not exists!")

            if len(self.ObjWithMatProblems) == 1:
                self.lblInfo.setText("Temporary material has been assigned to " + str(gen_func.shortNamer(self.ObjWithMatProblems[0])))
            elif len(self.ObjWithMatProblems) > 1:
                self.lblInfo.setText("Temporary material has been assigned to " + str(len(self.ObjWithMatProblems)) + " objects.")

            if len(FixResult) == 0:
                checkMarks[8].setText( green )
                checkLabels[8].setText("9. Temporary material has been assigned")
                fixButtons[8].setEnabled(False)

                conclusion_text = conclusion.fixConclusion(current_language, "9", True)
                self.txtbrowCheckerConclusion.setHtml(conclusion_text) 

                print self.lblInfo.text()
            else:
                checkMarks[8].setText( red )
                checkLabels[8].setText("9. Can't fix " + str(len(FixResult)) + " objects")
                fixButtons[8].setEnabled(False)
                self.lblInfo.setText("Fix Error. Object possibly deleted or renamed. See log.")
                self.lblInfo.setStyleSheet("background-color:#ed1c24;")

                conclusion_text = conclusion.fixConclusion(current_language, "9", False)
                self.txtbrowCheckerConclusion.setHtml(conclusion_text) 

                print "PolygonTools:", self.lblInfo.text()
        
        print "---"
                                                    

    #10
    def uvBorderCheck10(self, SelectedShapes):
        
        uvoutside = []
        
        Errors = []

        print "Objects with UV shells outside [0,1] area:"

        for k in range(len(SelectedShapes)):
            
            if cmds.objExists(SelectedShapes[k]) == True:
                #get bounding box 2d
                BBox2D = cmds.polyEvaluate(SelectedShapes[k], b2=True )
                    
                for i in range(len(BBox2D)):
                    for j in range(len(BBox2D[i])):
                            if (BBox2D[i][j] < 0.0) or (BBox2D[i][j] > 1.0): 
                                if SelectedShapes[k] not in uvoutside:
                                    uvoutside.append (SelectedShapes[k])
                                    print gen_func.shortNamer(SelectedShapes[k])
            else:
                Errors.append(SelectedShapes[i])

        self.CheckErrorCount.append(len(Errors))
        
        if len(Errors) > 0:
            print ""
            print "ATTENTION! These objects have not been checked because they do not exist or contain serious errors (", len(Errors), "):"
            print ('\n'.join(Errors))                 

        print ""

        if  len(uvoutside) > 0:
            checkMarks[9].setText( yellow )
            checkLabels[9].setText("10. Some UV shells outside [0,1] area (" + str(len(uvoutside)) + ")")
            return True
        else:
            checkMarks[9].setText( green )
            checkLabels[9].setText("10. All UV shells inside [0,1] area")
            return False

    #11   
    def uvSetsCountCheck11(self, SelectedShapes):

        self.ObjWithManyUVSets = []
        
        Errors = []

        print "Objects with many UV Sets:"

        #get uvsets number
        for i in range(len(SelectedShapes)):
            
            if cmds.objExists(SelectedShapes[i]) == True:
            
                totaluvsets = cmds.polyUVSet(SelectedShapes[i], query=True, auv=True )
                
                if len(totaluvsets) > 1:
                    self.ObjWithManyUVSets.append(len(totaluvsets))
                    print gen_func.shortNamer(SelectedShapes[i]), "has", len(totaluvsets)
            else:
                Errors.append(SelectedShapes[i])

        self.CheckErrorCount.append(len(Errors))
        
        if len(Errors) > 0:
            print ""
            print "ATTENTION! These objects have not been checked because they do not exist or contain serious errors (", len(Errors), "):"
            print ('\n'.join(Errors))                 

        print ""

        if len(self.ObjWithManyUVSets) == 0:
            checkMarks[10].setText( green )
            checkLabels[10].setText("11. Quantity of UV Sets: 1")
            fixButtons[10].setEnabled(False)
            return True
        else:
            checkMarks[10].setText( yellow )
            checkLabels[10].setText("11. Check qty. of UV Sets. Some has " + str(max(self.ObjWithManyUVSets)) + " (" + str(len(self.ObjWithManyUVSets)) + ")")
            fixButtons[10].setEnabled(False)
            return False
            
    #12
    def uvUtilCheck12(self, SelectedShapes):

        PTProgressWindow = cmds.window ( title="PolygonTools Progress Bar", minimizeButton=False, maximizeButton=False )
        cmds.columnLayout(PTProgressWindow )

        Shapes = len(SelectedShapes)
        progressControl = cmds.progressBar(maxValue=Shapes, width=300)
        cmds.showWindow( PTProgressWindow )
    
        self.AllUVAreas = []
        
        Errors = []

        print "Objects UV utilization list:"
        
        ObjectsWithUV = []
        
        #get UV
        for i in range(len(SelectedShapes)):

            cmds.progressBar(progressControl, edit=True, step=1)

            if cmds.objExists(SelectedShapes[i]) == True:
                UVArea  = gen_func.uvUtilStat(SelectedShapes[i])[0]
                print gen_func.shortNamer(SelectedShapes[i]), "-", UVArea, "%"
                if UVArea > 0:                    
                    self.AllUVAreas.append(UVArea)
                    ObjectsWithUV.append(SelectedShapes[i])
            else:
                print "ERROR: Object is not exists", str(SelectedShapes[i])
                Errors.append(SelectedShapes[i])

        cmds.deleteUI( PTProgressWindow , window=True ) 

        self.CheckErrorCount.append(len(Errors))

        print ""

        try:
            UVAareaAvg = sum(self.AllUVAreas)/len(self.AllUVAreas) 
            print "Average UV-Utilization (%):", UVAareaAvg            
        except:
            print "UV Area Array values:", sum(self.AllUVAreas), "/", len(self.AllUVAreas) 
            cmds.warning("Cant calculate average UV-Utilization. Maybe problems with UV layout.")
            self.CheckErrorCount.append(1)
        
        print ""

        FinalUV = gen_func.uvUtilStat(ObjectsWithUV)[0]
                
        #UV ranges
        dangerous_uv_range = range(95,101)
        ideal_uv_range = range(67,96)
        medium_uv_range = range(50,68)
        low_uv_range = range(1,51)
        
        checkLabels[11].setStyleSheet("")

        #ideal_uv_range 
        if FinalUV in ideal_uv_range:
            checkMarks[11].setText( green )
            checkLabels[11].setText("12. Current UV utilization: " + str(FinalUV) + "% | Good")
            return True

        #medium_uv_range                
        if FinalUV in medium_uv_range:
            checkMarks[11].setText( yellow )
            checkLabels[11].setText("12. Current UV utilization: " + str(FinalUV) + "% | Normal")
            print "Try to do UV layout more efficiently!"
            return False

        #low_uv_range 
        if FinalUV in low_uv_range:
            checkMarks[11].setText( red )
            checkLabels[11].setText("12. Current UV utilization: " + str(FinalUV) + "% | Low")
            print "UV Utilization is Low!"
            return False

        #dangerous_uv_range                            
        if FinalUV in dangerous_uv_range:
            checkMarks[11].setText( red )
            checkLabels[11].setText("12. Current UV utilization: " + str(FinalUV) + "% | Suspicious")
            print "Check padding, overlap and range on UV layout!"
            return False
                    
        if  FinalUV == 0:
            checkMarks[11].setText( red )
            checkLabels[11].setStyleSheet("color:#ed1c24;")
            checkLabels[11].setText("12. Check UV mapping! UV utilization: 0% | No UV-layout")
            return False
        

def namesChecker (SelectedShapes):
    #array for errors
    NameErrors = []
    
    #names in scene for matching
    UsedNames = []
    
    NamingProblems = []
    
    #get scene name
    CurrentSceneName = cmds.file( query=True, sn=True, shn=1) 
    
    if len(CurrentSceneName) == 0:
        NameErrors.append("scene name")
        cmds.warning ("PolygonTools. Scene not saved. Please save the scene!")
    else:
        print "PolygonTools. Current scene name is:", CurrentSceneName
        UsedNames.append(CurrentSceneName)    
    
    for i in range(len(SelectedShapes)):
        print ""
        print i, "-", gen_func.shortNamer(SelectedShapes[i])

        #get object name
        UsedNames.append(SelectedShapes[i])
        
        #get material
        try:
            MaterialList = cmds.ls(mat=1)
            InConnections = cmds.listConnections (SelectedShapes[i], type = "shadingEngine")
            AssignedMat = cmds.ls( cmds.listConnections (InConnections), mat=1)
        except:
            pass
    
        if len(AssignedMat) == 0:
            ErrorName = "mat. availability"
            if ErrorName not in NameErrors: #add once
                NameErrors.append("mat. availability")
            cmds.warning ("No material assigned to object. Please assign a material!")
        else:
            print "Assigned material:", AssignedMat[0]   
            UsedNames.append(AssignedMat[0])     
        
        if (len(AssignedMat)>0) and (AssignedMat[0] == "lambert1"):
            ErrorName = "material type"
            if ErrorName not in NameErrors:
                NameErrors.append("material type") #add once
            print "Default material is assigned! It\'s correct?"
    
    #add layer names    
    layers = cmds.ls( type='displayLayer')
    for l in layers[1:]:
        UsedNames.append(l)        
    
    #standard names is not good 'Shape'
    bad_names = ['Sphere','Cube', 'Cylinder', 'Cone', 'Torus', 'Plane', 'Disc', 'lambert1', 'lambert', 'blinn', 'phong', ':', 'untitled', 'layer', 'pasted']
    
    #create naming problems array
    NamingProblems = [s for s in UsedNames if any(xs in s for xs in bad_names)]
    
    UniqueNamingProblems = []
    
    for i in range(len(NamingProblems)):
        if NamingProblems[i] not in UniqueNamingProblems:
            UniqueNamingProblems.append(NamingProblems[i])

    print ""

    if len(NamingProblems) > 0:
        print "Naming problems (", len(UniqueNamingProblems), "):"
        print ('\n'.join(UniqueNamingProblems))
        NameErrors.append("naming rules (" + str(len(UniqueNamingProblems)) + ")")
        print ""
        print len(UniqueNamingProblems), "naming problems found."
        print ""
        
    return NameErrors
