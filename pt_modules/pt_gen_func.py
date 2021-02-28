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
import threading
import random
import maya.cmds as cmds
import maya.mel
import maya.OpenMaya as OpenMaya
import sys

import pt_conclusion as conclusion
reload(conclusion)

sys.path.append('..')
import pt_config_loader as cfgl
reload(cfgl)

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtUiTools import *

#General Tab
class PT_Gen_Tab (QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent=parent)

        self.tabGen_v_layout = QVBoxLayout(self)
        self.tabGen_v_layout.setAlignment(Qt.AlignTop)
        self.tabGen_v_layout.setContentsMargins(0,10,0,10)
        self.tabGen_v_layout.setSpacing(5)
        
        #Top Labels
        self.lbInfo01 = QLabel()
        self.lbInfo01.setText('Welcome to Polygon Tools!')
        self.lbInfo01.setMargin(2)
        self.lbInfo02 = QLabel()
        self.lbInfo02.setMargin(2)
        
        #Progress Bar
        self.pbChekProgress = QProgressBar()
        self.pbChekProgress.setRange(0, 100)
        
        #Elements
        
        #icons
        currentDir = os.path.dirname(__file__)
        try:
            iconMesh  = QPixmap(currentDir +"/icons/mesh_icon.png")
            iconScene  = QPixmap(currentDir +"/icons/scene_icon.png")
            iconViewport  = QPixmap(currentDir +"/icons/viewport_icon.png")
            iconStat  = QPixmap(currentDir +"/icons/stat_icon.png")
            self.iconDim  = QPixmap(currentDir +"/icons/dim_icon.png")
            self.iconDimXForm  = QPixmap(currentDir +"/icons/dim_transform_icon.png")
            iconZeroA  = QPixmap(currentDir +"/icons/zero_area_icon.png")
        except:
            cmds.warning( "PolygonTools: Can't load icons for General Tab! Check icon files in pt_modules/icons directory.")
        
        
        #groupbox Prepare
        self.gboxPrepare = QGroupBox("Prepare for Feedback")
        self.gboxPrepare.setMaximumWidth(340)
        self.gboxPrepare_v_layout = QVBoxLayout()     
                
        #Prepare buttons        
        self.btnPrepScene = QPushButton("Scene")
        self.btnPrepScene.setMinimumWidth(75)
        self.btnPrepScene.setMinimumHeight(35)
        self.btnPrepScene.setStyleSheet("background-color:#0061B0;")
        self.btnPrepScene.setIcon(iconScene)
        
        self.btnPrepView = QPushButton("Viewports")
        self.btnPrepView.setMinimumWidth(75)
        self.btnPrepView.setMinimumHeight(35)
        self.btnPrepView.setStyleSheet("background-color:#25567D;")
        self.btnPrepView.setIcon(iconViewport)
                
        self.btnPrepMesh = QPushButton("Mesh")
        self.btnPrepMesh.setMinimumWidth(75)
        self.btnPrepMesh.setMinimumHeight(35)
        self.btnPrepMesh.setStyleSheet("background-color:#3579B0;")
        self.btnPrepMesh.setIcon(iconMesh)

        #groupbox Statistics
        self.gboxStatistics = QGroupBox("Statistics")
        self.gboxStatistics.setMaximumWidth(340)
        self.gboxStatistics_v_layout = QVBoxLayout()     
        
        #Statistics labels      
        self.lblShapes = QLabel("Mesh Shapes: ")
        self.lblpolycount = QLabel("Polygons: ")
        self.lbltriscount = QLabel("Triangles: ")
        self.lblvertcount = QLabel("Vertices: ")
        self.lblJointsCount = QLabel("Joints: ")
        self.lblUVVert = QLabel("UV-vertices: ")
        self.lblMatIDQ = QLabel("Materials: ")
        
        self.lblUVUt = QLabel("Total UV-Utilization: ")
        self.lblUVUtAvg = QLabel("Average UV-Utilization: ")
        self.lblUVO = QLabel("Overlaps: ")
        self.lblUVarea = QLabel("UV in [0,1]: ")
        self.lblMapChanQ = QLabel("UV Sets: ")
        self.lblUVShellsCount = QLabel("UV Shells: ")
        
        #forUVutil
        self.lblUVUtilPic = QLabel()
        self.lblUVUtilPic.setFixedSize(120, 100)
        
        self.pixmap = QPixmap(QSize(100,100))
        self.colorBlack = QColor()

        self.colorBlack.setRgb(0,0,0,255)
        self.pixmap.fill(self.colorBlack)
        
        self.lblUVUtilPic.setPixmap(self.pixmap)
        
        self.gboxGenConclusion = QGroupBox("Conclusion")
        self.gboxGenConclusion.setMaximumWidth(340)
        self.gboxGenConclusion.setMinimumHeight(170)
        self.gboxGenConclusion_v_layout = QVBoxLayout()
        
        #conclusion text here
        self.txtbrowGenConclusion = QTextBrowser()
        self.txtbrowGenConclusion.setHtml("")
            
        self.gboxGenConclusion_v_layout.addWidget(self.txtbrowGenConclusion) 
        
        #Add labels to groupbox
        self.gboxStatistics_v_layout.addWidget(self.lblShapes)
        self.gboxStatistics_v_layout.addWidget(self.lblpolycount)
        self.gboxStatistics_v_layout.addWidget(self.lbltriscount)
        self.gboxStatistics_v_layout.addWidget(self.lblvertcount)
        self.gboxStatistics_v_layout.addWidget(self.lblJointsCount)
        self.gboxStatistics_v_layout.addWidget(self.lblUVVert)
        self.gboxStatistics_v_layout.addWidget(self.lblMatIDQ)
        self.gboxStatistics_v_layout.addWidget(self.lblUVO)
        self.gboxStatistics_v_layout.addWidget(self.lblUVarea)
        self.gboxStatistics_v_layout.addWidget(self.lblMapChanQ)
        self.gboxStatistics_v_layout.addWidget(self.lblUVShellsCount)
        self.gboxStatistics_v_layout.addWidget(self.lblUVUt)
        self.gboxStatistics_v_layout.addWidget(self.lblUVUtAvg)
        self.gboxStatistics_v_layout.addWidget(self.lblUVUtilPic)
        
        # Horizontal layout 2 for buttons
        self.tabGen_h_layout_02 = QHBoxLayout()
        self.tabGen_h_layout_02.setAlignment(Qt.AlignLeft)
        
        self.gboxStatistics_v_layout.addLayout(self.tabGen_h_layout_02)
        
        #self.tabGen_v_layout.addLayout(self.tabGen_h_layout_02)
        self.btnGetStat = QPushButton("Get Statistics")
        self.btnGetStat.setToolTip("Statistics")
        self.btnGetStat.setStyleSheet("background-color:#003663;")
        self.btnGetStat.setMinimumWidth(110)
        self.btnGetStat.setIcon(iconStat)
        
        self.btnGetDim = QToolButton()
        self.btnGetDim.setText("Show Dimension")
        self.btnGetDim.setToolTip("Show Dimension")
        self.btnGetDim.setMaximumWidth(150)
        self.btnGetDim.setIcon(self.iconDim) 
        self.btnGetDim.setCheckable(True)

        self.btnZeroPolySelector = QPushButton()
        self.btnZeroPolySelector.setMinimumWidth(18)
        self.btnZeroPolySelector.setToolTip("Select Zero-Faces")
        self.btnZeroPolySelector.setDisabled(True)
        self.btnZeroPolySelector.setIcon(iconZeroA)

        #2 buttons
        self.tabGen_h_layout_02.addWidget(self.btnGetStat)
        self.tabGen_h_layout_02.addWidget(self.btnGetDim)
        self.tabGen_h_layout_02.addWidget(self.btnZeroPolySelector)

        #add gbox stat to layout
        self.gboxStatistics.setLayout(self.gboxStatistics_v_layout)
        
        #conclusion
        self.gboxGenConclusion.setLayout(self.gboxGenConclusion_v_layout)
        
        #Add to Layout
        
        #labels
        self.tabGen_v_layout.addWidget(self.lbInfo01)
        self.tabGen_v_layout.addWidget(self.lbInfo02)
        
        #set progress bar to layout
        self.tabGen_v_layout.addWidget(self.pbChekProgress)
        self.pbChekProgress.setValue(0)
        self.pbChekProgress.setMaximumWidth(340)
        
        self.prep_h_layout_01 = QHBoxLayout()
        
        #Add horizontal elements - buttons prepare    
        self.prep_h_layout_01.addWidget(self.btnPrepMesh)
        self.prep_h_layout_01.addWidget(self.btnPrepScene)
        self.prep_h_layout_01.addWidget(self.btnPrepView)
        
        self.gboxPrepare_v_layout.addLayout(self.prep_h_layout_01)
        
        self.gboxPrepare.setLayout(self.gboxPrepare_v_layout)
        
        #add Group Box
        self.tabGen_v_layout.addWidget(self.gboxPrepare)
    
        #Statistics area
        self.tabGen_v_layout.addWidget(self.gboxStatistics)
        
        #conclusion area
        self.tabGen_v_layout.addWidget(self.gboxGenConclusion)
                
        #Scene Prepare
        self.btnPrepScene.clicked.connect(self.btnPrepSceneClicked)

        #Viewport Prepare
        self.btnPrepView.clicked.connect(self.btnPrepViewClicked)

        #Mesh Prepare
        self.btnPrepMesh.clicked.connect(self.btnPrepMeshClicked)
                
        #Get Statistics
        self.btnGetStat.clicked.connect(self.getStatistics)
        
        #GetDimension
        self.btnGetDim.pressed.connect(self.btnGetDimPressed)

        self.btnZeroPolySelector.clicked.connect(self.selectZeroFaces)

        #lang selector
        current_languge = cfgl.configLoader()[14]
        self.txtbrowGenConclusion.setHtml( conclusion.genTabIntroConclusion(current_languge) )

        self.ObjectWithZeroFaces = []
        #"------------------- FUNCTIONS --------------------------"
        
    
    #prepare scene
    def btnPrepSceneClicked(self):
    
        print "-------------------------------------------"
        print "     PolygonTools. SCENE PREPARE BATCH"
        print "-------------------------------------------"
        
        self.SimpleActionResponce('1', 'Scene preparation is running!', '', '')
        
        #prepare scene batch
        conclusion_data = prepareScene()

        #get all info about scene name
        scene_name_data = sceneName()

        #add scene name info
        conclusion_data.append(scene_name_data[3])
        
        #get current language
        current_languge = cfgl.configLoader()[14]
        
        #set conclusion text
        conclusion_text = conclusion.prepSceneConclusion(current_languge, conclusion_data)
        
        #conclusion output
        self.txtbrowGenConclusion.setHtml(conclusion_text)
    
        #sceneName
        self.SimpleActionResponce('2', '', scene_name_data[1], '') 
        self.lbInfo02.setStyleSheet(scene_name_data[2])
            
        self.SimpleActionResponce('1', 'Scene was successfully prepared!', '', '')
        self.lbInfo01.setStyleSheet("background-color:#3D523D;")
    
        print "-------------------------------------------"


    #Responce
    def SimpleActionResponce(self, config, label_01, label_02, label_03):
        
        if config == '1':
            self.lbInfo01.setText(label_01)
            print ('PolygonTools: ' + label_01)
        
        if config == '2':
            self.lbInfo02.setText(label_02)
            print ('PolygonTools: ' + label_02)
            
        if config == '12':
            self.lbInfo01.setText(label_01)
            if label_01 != '':
                print ('PolygonTools: ' + label_01)
        
            self.lbInfo02.setText(label_02)
            if label_02 != '':
                print ('PolygonTools: ' + label_02)        

    #clean values
    def valueCleaner(self, what_clear):
    
        #1 clear stat
        if what_clear == '1':
            self.SimpleActionResponce('123', '', '', '')
            self.pbChekProgress.setValue(0)
            self.lblShapes.setText('Mesh Shapes: ')
            self.lblpolycount.setText('Polygons: ')
            self.lbltriscount.setText('Triangles: ')
            self.lblvertcount.setText('Vertices: ')
            self.lblJointsCount.setText('Joints: ')
            self.lblUVVert.setText('UV-vertices: ')
            self.lblMatIDQ.setText("Materials: ")
            self.lblUVO.setText("Overlaps: ")
            self.lblMapChanQ.setText("UV Sets: ")
            self.lblUVUt.setText ("Total UV-Utilization: ")
            self.lblUVUtAvg.setText ("Average UV-Utilization: ")
            self.lblUVarea.setText ("UV in [0,1]: ")
            self.lblUVShellsCount.setText ("UV Shells: ")
            self.pixmap.fill(self.colorBlack)
            self.lblUVUtilPic.setPixmap(self.pixmap)
            self.btnZeroPolySelector.setDisabled(True)
            
            #style to default
            self.lblShapes.setStyleSheet("")
            self.lblMatIDQ.setStyleSheet("")
            self.lblUVarea.setStyleSheet("")
            self.lblUVUt.setStyleSheet("")
            self.lblMapChanQ.setStyleSheet("")
            self.lbltriscount.setStyleSheet("")
            self.lblUVO.setStyleSheet("")
            
            #clear conclusion
            self.txtbrowGenConclusion.setHtml("")
            
        if what_clear == '2':
            self.lbInfo01.setStyleSheet("")
            self.lbInfo02.setStyleSheet("")
                

    #Prepare viewport
    def btnPrepViewClicked(self):
    
        self.pbChekProgress.setValue(0)
    
        print "-----------------------------------------"
        print "     PolygonTools VIEW PREPARE BATCH"
        print "-----------------------------------------"
        
        self.SimpleActionResponce('1', 'Viewports preparation is running!', '', '')
        self.valueCleaner("2")
        
        #prepare batch
        conclusion_data = prepareViewport()
                
        #get current language
        current_languge = cfgl.configLoader()[14]
        
        #set conclusion text
        conclusion_text = conclusion.prepViewportConclusion(current_languge, conclusion_data)
        
        #conclusion output
        self.txtbrowGenConclusion.setHtml(conclusion_text)        
        
        self.pbChekProgress.setValue(100)

        self.SimpleActionResponce('1', 'Viewports was successfully prepared!', '', '')
        self.lbInfo01.setStyleSheet("background-color:#3D523D;")
    
        print "-----------------------------------------"
        
        
    
    #Prepare Mesh
    def btnPrepMeshClicked(self):
                        
        self.pbChekProgress.setValue(0)
        
        self.lbInfo01.setText("Prepare Mesh in progress...")
        self.lbInfo02.setText("")
        
         #get current language
        current_languge = cfgl.configLoader()[14]
                
        # check selection if nothing selected show message
        try:
            shapes_transforms_array = checkSelection()
            
            #shapes array
            selected_shapes = shapes_transforms_array[0]
            
            #transform array
            selected_transforms = shapes_transforms_array[1]
            
        except:
            self.SimpleActionResponce('1', "Please select something. Mesh object for example...", '', '')

        if len(selected_shapes) > 0:
                        
            self.pbChekProgress.setValue(50)                        
            
            #prepare mesh batch
            conclusion_data = prepareMesh(selected_shapes, selected_transforms)
            
            #get all info about scene name
            scene_name_data = sceneName()

            #add scene name info
            conclusion_data.append(scene_name_data[3])

            #set conclusion text
            conclusion_text = conclusion.prepMeshConclusion(current_languge, conclusion_data)
            
            #conclusion output
            self.txtbrowGenConclusion.setHtml(conclusion_text)        
                                                
            print ""

            #STEP 9
            #sceneName
            self.SimpleActionResponce('2', '', scene_name_data[1], '') 
            self.lbInfo02.setStyleSheet(scene_name_data[2])

            self.pbChekProgress.setValue(100)
                        
            #final text
            if len(selected_shapes) == 1:
                
                self.SimpleActionResponce('1', (shortNamer(selected_shapes[0]) + " was prepared!"), '', '')
                self.lbInfo01.setStyleSheet("background-color:#3D523D;")
            else:
                self.SimpleActionResponce('1', (str(len(selected_shapes)) + " shapes was prepared!"), '', '')
                self.lbInfo01.setStyleSheet("background-color:#3D523D;")
            
            print "-----------------------------------------"
            
        else:
            self.SimpleActionResponce('12', "Please select something. Mesh object for example...", '', '')
            conclusion_text = conclusion.noSelection(current_languge, "prepare_mesh")
            self.txtbrowGenConclusion.setHtml(conclusion_text)
            self.valueCleaner("2")
                            

    #get dimension of object
    def btnGetDimPressed(self):
        
        self.pbChekProgress.setValue(0)

        #get current language
        current_languge = cfgl.configLoader()[14]
        
        # check selection if nothing selected show message
        try:
            shapes_transforms_array = checkSelection()
            
            #shapes array
            selected_shapes = shapes_transforms_array[0]
            
        except:
            self.SimpleActionResponce('1', "Please select something. Mesh object for example...", '', '')

        ObjectHasTransform = False

        if len(selected_shapes) > 0:
            if self.btnGetDim.isChecked():
                cmds.setXformManip(suppress=True)
                self.btnGetDim.setText("Show Dimension")
                self.SimpleActionResponce('12', 'Show Dimension is OFF', '', '')
                self.txtbrowGenConclusion.setHtml( conclusion.genTabIntroConclusion(current_languge) )
                self.btnGetDim.setIcon(self.iconDim)                
            else:
                for i in range(len(selected_shapes)):

                    #get all array
                    ParentsArray = cmds.ls(selected_shapes[i], long=True)[0].split('|')[1:-1]
                    #get split names
                    TransformNameArray = ['|'.join(ParentsArray[:i]) for i in xrange(1, 1 + len(ParentsArray))]

                    for k in range(len(TransformNameArray)):                    
                        transform_matrix = []
                        transform_matrix = cmds.xform(TransformNameArray[k], q=True, scale=True, relative=True)
                        if sum(transform_matrix) != 3:
                            print TransformNameArray[k], "has Scale transform. Its value is:", transform_matrix
                            ObjectHasTransform = True

                print ""    
                if ObjectHasTransform == True:
                    self.btnGetDim.setIcon(self.iconDimXForm)                
                
                cmds.setXformManip(suppress=False, showUnits=True)
                self.btnGetDim.setText("Hide Dimension")
                self.SimpleActionResponce('12', "Show Dimension is ON", '', '')
                
                #set conclusion text
                conclusion_text = conclusion.dimensionConclusion(current_languge, ObjectHasTransform)
                #conclusion output
                self.txtbrowGenConclusion.setHtml(conclusion_text)        

        else:
            self.btnGetDim.setChecked(True)
            self.SimpleActionResponce('12', "Please select something. Mesh object for example...", '', '')
            conclusion_text = conclusion.noSelection(current_languge, "dimension")
            self.txtbrowGenConclusion.setHtml(conclusion_text)
    
        
        
    #get statistics
    def getStatistics(self):
        
        #clear values
        self.valueCleaner("1")
        self.valueCleaner("2")

        uv_shells_total = 0
        
        #get current language
        current_languge = cfgl.configLoader()[14]
        
        stat_conclusion_data = []
                
        # check selection if nothing selected show message
        try:
            shapes_transforms_array = checkSelection()
            
            #shapes array
            selected_shapes = shapes_transforms_array[0]
            
            #transform array
            selected_transforms = shapes_transforms_array[1]
            
            selected_joints = len(shapes_transforms_array[3])

        except:
            self.SimpleActionResponce('12', "Please select something. Mesh object for example...", '', '')
            shapes_transforms_array = checkSelection()            
        
        #if something selected
        if len(selected_shapes) > 0:
            
            print "-------------------- Polygon Tools Statistics --------------------"

            # 0 - unsupported_shapes_count, 1 - all_shapes_polycount, 2 - totalpoly, 3 - totaltris, 4 - totalvert, 5 - totaluvvert
            #run geo stat function
            geo_stat_data = geoStat(shapes_transforms_array, selected_shapes, selected_transforms)
            
            if geo_stat_data[0] > 0:
                self.lblShapes.setStyleSheet("color:#f26522;")
                self.lblShapes.setText("Mesh Shapes: " + str(len(geo_stat_data[1])) + " | Not mesh shapes: "+ str(geo_stat_data[0]))
                stat_conclusion_data.append(str(geo_stat_data[0]))
            else:
                self.lblShapes.setStyleSheet("")
                self.lblShapes.setText("Mesh Shapes: " + str(len(geo_stat_data[1])))
                stat_conclusion_data.append(True)
            
            print self.lblShapes.text()                        
                        
            self.lblpolycount.setText('Polygons: ' + str(geo_stat_data[2]))
            print self.lblpolycount.text()
            self.pbChekProgress.setValue(10)
        
            self.lbltriscount.setText('Triangles: ' + str(geo_stat_data[3]))
            print self.lbltriscount.text()
            self.pbChekProgress.setValue(20)
            
            self.lblvertcount.setText('Vertices: ' + str(geo_stat_data[4]))
            print self.lblvertcount.text()
            self.pbChekProgress.setValue(30)
            
            self.lblJointsCount.setText('Joints: ' + str(selected_joints))
            
            self.lblUVVert.setText('UV-vertices: ' + str(geo_stat_data[5]))
            print self.lblUVVert.text()
            self.pbChekProgress.setValue(40)
            
            print ""
            
            # 0 - shape_geo_area, 1 - shape_uv_area, 2 - shape_geo_area, 3 -shapes_with_uv_overlaps, 4 - full_UVOverlap, 5 - ObjectsWithZeroArea
            #run UV stat function
            overlap_stat_data = overlapStat(selected_shapes, geo_stat_data[1])

            print ""
                                                        
            if len(overlap_stat_data[3]) == 0:
                self.lblUVO.setText("Overlaps: 0")
                print self.lblUVO.text()
                stat_conclusion_data.append(True)
            else:
                self.lblUVO.setText("Overlaps: present in " + str(len(overlap_stat_data[3])) + " shape(s)")
                print self.lblUVO.text()
                print ""
                stat_conclusion_data.append(False)

                        
            for i in range(len(overlap_stat_data[4])):
                print str(i+1), "-", shortNamer(overlap_stat_data[4][i]), "has 100% overlap."
                    
            if len(overlap_stat_data[4]) > 0:
                print ""
                self.lblUVO.setStyleSheet("color:#f26522;") 
                self.lblUVO.setText(self.lblUVO.text() + " | "+ str(len(overlap_stat_data[4])) + " - has 100%.")
                print ("ATTENTION! " + str(len(overlap_stat_data[4])) + " shape(s) has 100% overlap.")
                stat_conclusion_data.append(str(len(overlap_stat_data[4])))
            else:
                stat_conclusion_data.append(True)
            
            self.pbChekProgress.setValue(45)        
            

            print ""
            #search very small tris

            if len(overlap_stat_data[5]) > 0:
                stat_conclusion_data.append(False) #for conclusion
                
                self.ObjectWithZeroFaces = overlap_stat_data[5]
                if len(self.ObjectWithZeroFaces) == 1:
                    self.btnZeroPolySelector.setDisabled(False)
                
                self.lbltriscount.setStyleSheet("color:#f26522;")
                self.lbltriscount.setText(self.lbltriscount.text() + ' | Very small or Zero-area was detected!')
                print "Objects with very small area (less than 0.0001m) or area = 0 (Zero-area):"
                for i in range(len(overlap_stat_data[5])):
                    print shortNamer(overlap_stat_data[5][i])
                print "Please pay more attention for this objects!"
            else:
                stat_conclusion_data.append(True)

            self.pbChekProgress.setValue(50)  
            
            #return selection
            if len(selected_shapes) == 1:
                cmds.select(selected_shapes[0])
                
            print ""
            
            # 0 - one_uv_set, 1 - many_uv_sets
            #run UV-set stat function
            uvset_stat_data = uvSetStat(selected_shapes)
            
                
            if len(uvset_stat_data[1]) == 0 and len(selected_shapes) > 1:
                self.lblMapChanQ.setText("UV Sets: " + str(len(uvset_stat_data[0])) + " shape(s) has one.")
                print self.lblMapChanQ.text()
                stat_conclusion_data.append(True)
            elif len(uvset_stat_data[1]) == 0 and len(selected_shapes) == 1:
                self.lblMapChanQ.setText("UV Sets: 1")
                stat_conclusion_data.append(True)
            else:
                self.lblMapChanQ.setStyleSheet("color:#f26522;")
                self.lblMapChanQ.setText("UV Sets: " + str(len(uvset_stat_data[0])) + " shape(s) has one | " + str(len(uvset_stat_data[1])) + " shape(s) > then one.")
                print self.lblMapChanQ.text()
                stat_conclusion_data.append(False)
                
            print ""
            
            self.pbChekProgress.setValue(60)
            
            # 0-one_mat, 1-many_mat, 2-unique_mat
            #run materials stat
            mat_stat_data = matStat(selected_shapes)
  
            print ""
            
            if len(mat_stat_data[0]) == len(selected_shapes) and len(selected_shapes)==1:
                self.lblMatIDQ.setText("Materials: " + str(len(mat_stat_data[0])))            
                print self.lblMatIDQ.text() 
                stat_conclusion_data.append(True)
            elif len(mat_stat_data[0]) == len(selected_shapes) and len(selected_shapes)>1:
                self.lblMatIDQ.setText("Materials: " + str(len(mat_stat_data[0])) + " shapes has 1.")
                print self.lblMatIDQ.text()
                stat_conclusion_data.append(True)
            elif len(mat_stat_data[0]) == 0 and len(selected_shapes)==1:
                self.lblMatIDQ.setStyleSheet("color:#f26522;")
                self.lblMatIDQ.setText("Materials: " + str(len(mat_stat_data[2])) + " | See log for details.")
                stat_conclusion_data.append(False)
            else:
                self.lblMatIDQ.setStyleSheet("color:#f26522;")
                self.lblMatIDQ.setText("Materials: " + str(len(mat_stat_data[0])) + " shapes has 1 | " + str(len(mat_stat_data[1])) + " - many. See log.")
                print self.lblMatIDQ.text()
                stat_conclusion_data.append(False)
                
            print ""
                            
            self.pbChekProgress.setValue(70)
            
            # 0-uv_outside, 1-unique_shape_outside
            #run UV 1-0 range stat
            uvrange_stat_data = uvRangeStat(selected_shapes)
                        
            if len(uvrange_stat_data[1])==0 and len(selected_shapes)>1:
                self.lblUVarea.setText ("UV in [0,1]: True for " + str(len(selected_shapes)) + " shape(s)")
                print self.lblUVarea.text()
                stat_conclusion_data.append(True)
            elif len(uvrange_stat_data[1])==0 and len(selected_shapes)==1:
                self.lblUVarea.setText ("UV in [0,1]: True")
                print self.lblUVarea.text()                
                stat_conclusion_data.append(True)
            elif len(uvrange_stat_data[1])>0:
                self.lblUVarea.setStyleSheet("color:#f26522;")
                self.lblUVarea.setText ("UV in [0,1]: False for " + str(len(uvrange_stat_data[1])) + " shape(s) from " + str(len(selected_shapes)))
                print self.lblUVarea.text()
                stat_conclusion_data.append(False)
                        
            print ""                            
            
            self.pbChekProgress.setValue(80)

            #win for progress bar            
            PTProgressWindow = cmds.window ( title="PolygonTools Progress Bar", minimizeButton=False, maximizeButton=False )
            cmds.columnLayout(PTProgressWindow )

            Shapes = len(selected_shapes)
            progressControl = cmds.progressBar(maxValue=Shapes, width=300)
            cmds.showWindow( PTProgressWindow )

            # 0-precentage, 1-pixmap
            #uv utilization run
            uvutil_stat_data = uvUtilStat(selected_shapes)            
            
            print "UV-Utilisation per shape:" 
            all_uv_areas =[]
            #UVarea - check LOW UV-utilization
            for i in range(len(selected_shapes)):
                #prog bar
                cmds.progressBar(progressControl, edit=True, step=1)
                
                UVAreaSum = uvUtilStat(selected_shapes[i])[0]
                print i+1, "-", shortNamer(selected_shapes[i]), "-", UVAreaSum, "%"                
                if UVAreaSum > 0:                    
                    all_uv_areas.append(UVAreaSum)

            cmds.deleteUI( PTProgressWindow , window=True ) 

            self.lblUVUtilPic.setPixmap(uvutil_stat_data[1])                 
                
            uvarea_sum = sum(all_uv_areas)
            final_uv_area = uvutil_stat_data[0]
            
            try:
                uvarea_avg = sum(all_uv_areas)/len(all_uv_areas)        
                self.lblUVUtAvg.setText ("Average UV-Utilization: " + str(uvarea_avg) + "%")  
            except:
                print "UV Area Array values:", sum(all_uv_areas), "/", len(all_uv_areas) 
                cmds.warning("Cant calculate average UV-Utilization. Maybe problems with UV layout.")
                self.lblUVUtAvg.setText ("Average UV-Utilization: not available. See log")  

            
            #UV ranges
            dangerous_uv_range = range(95,101)
            ideal_uv_range = range(67,95)
            medium_uv_range = range(50,66)
            low_uv_range = range(1,49)
        
            #if 1 obj        
            if (len(selected_shapes) == 1):
                self.lblUVUtAvg.setEnabled(False)
            else:
                self.lblUVUtAvg.setEnabled(True)
                
            print ""                

                                        
            if (final_uv_area in ideal_uv_range):
                self.lblUVUt.setStyleSheet("")
                self.lblUVUt.setText ("Total UV-Utilization: " + str(final_uv_area) + "%")     
                stat_conclusion_data.append(True)
                   
            if final_uv_area in medium_uv_range:
                self.lblUVUt.setStyleSheet("")
                self.lblUVUt.setText ("Total UV-Utilization: " + str(final_uv_area) + "% | Try to do more efficiently!")
                stat_conclusion_data.append(True)                

            if (final_uv_area in low_uv_range):
                self.lblUVUt.setStyleSheet("color:#f26522;")
                self.lblUVUt.setText ("Total UV-Utilization: " + str(final_uv_area) + "% | Low!")
                stat_conclusion_data.append(False)
                                
            if (final_uv_area in dangerous_uv_range):
                self.lblUVUt.setStyleSheet("color:#f26522;")
                self.lblUVUt.setText ("Total UV-Utilization: >" + str(final_uv_area) + "% | Check padding, overlap, range!")
                stat_conclusion_data.append(False)

            if final_uv_area == 0:
                self.lblUVUt.setStyleSheet("color:#f26522;")
                self.lblUVUt.setText ("Total UV-Utilization: not available. Problems with UV layout!")
                stat_conclusion_data.append(False)


            print self.lblUVUt.text()
            print self.lblUVUtAvg.text()
                                                                
            self.pbChekProgress.setValue(90)
            
            print ""
            
            # 0-uv_shells_all, 1-uv_shells_total
            #UV shells number
            uvshells_stat_data = uvShellsStat(selected_shapes)
            
            self.lblUVShellsCount.setText ("UV Shells: " + str(uvshells_stat_data[1]) + " for " + str(len(selected_shapes)) + " shape(s)")
            print self.lblUVShellsCount.text()
            
            print "" 
            
            self.pbChekProgress.setValue(100)
            
            print ""
            
            cmds.select( selected_shapes )
            
            #set conclusion text
            conclusion_text = conclusion.statConclusion(current_languge, stat_conclusion_data)
            #conclusion output
            self.txtbrowGenConclusion.setHtml(conclusion_text)                    
        
            if len(selected_shapes) == 1:
                #short_name = str(cmds.listRelatives( SelectedObjectName, p=True )[0])
                self.SimpleActionResponce('12', "Statistics was successfully obtained for 1 object", 'Processed object: ' + shortNamer(selected_shapes[0]), '')
                self.lbInfo01.setStyleSheet("background-color:#3D523D;")
            else:
                self.SimpleActionResponce('12', ("Statistics was successfully obtained for " + str(len(selected_shapes)) + ' mesh shapes.'), '', '')
                self.lbInfo01.setStyleSheet("background-color:#3D523D;")
            
            print "--------------------"
            
        else:
            self.SimpleActionResponce('12', "Please select something. Mesh object for example...", '', '')   
            conclusion_text = conclusion.noSelection(current_languge, "statisctics")
            self.txtbrowGenConclusion.setHtml(conclusion_text)

            
        
        #return totalpoly, totaltris, totalvert, totaluvvert, totaluvsets, UVoverlap    


    def selectZeroFaces(self):
        
        ZeroFaceArray = []

        current_languge = cfgl.configLoader()[14]

        if len(self.ObjectWithZeroFaces) == 1 and cmds.objExists(self.ObjectWithZeroFaces[0])==True:
            
            CurrentObjectPolycount = cmds.polyEvaluate(self.ObjectWithZeroFaces[0], face=True )
        
            for l in range(0, CurrentObjectPolycount):
                cmds.select(self.ObjectWithZeroFaces[0] + '.f['+ str(l) +']')
                SelectedFaceName = (self.ObjectWithZeroFaces[0] + '.f['+ str(l) +']')
                GeoAreaRaw = cmds.polyEvaluate( fa=True )
                GeoArea = (GeoAreaRaw[0]/10000)              
                
                if GeoArea == 0:
                    ZeroFaceArray.append(SelectedFaceName)
            
            cmds.select(ZeroFaceArray)
            cmds.modelEditor( modelPanel='modelPanel4', da="wireframe", grid=False, displayLights="default", cameras=False, activeView=True)
            self.SimpleActionResponce('12', str(len(ZeroFaceArray)) + " Zero-faces was selected.", 'Processed object: ' + shortNamer(self.ObjectWithZeroFaces[0]), '')

            if current_languge == "rus":
                self.txtbrowGenConclusion.setHtml("Полигоны с нулевой площадью выделены. Постарайтесь их исправить!")
            else:
                self.txtbrowGenConclusion.setHtml("Zero-faces was selected. Try to fix it!")

        else:
            self.btnZeroPolySelector.setDisabled(True)
            print "PolygonTools. Can't select Zero-Faces. Object is not Exists or other problems."

#---------------------------------------- FUNC --------------------    

#Check Scene Name
def sceneName():
    
    current_scene_name = cmds.file( query=True, sn=True, shn=1)

    scene_name_conclusion_data = False
    
    message = ''

    if current_scene_name == '':
        message = "Please save current scene!"
        label_color = "background-color:#916666;"
        scene_name_conclusion_data = False
    else:
        message = "Current file name is: " + current_scene_name
        label_color = "background-color:#3D523D;"
        scene_name_conclusion_data = True

    return current_scene_name, message, label_color, scene_name_conclusion_data


#procedure check selection object type and objects count    
def checkSelection():
    
    all_sel_shapes = []
    mesh_sel_shapes = []
    all_sel_transforms = []
    all_sel_joints = [] 
    
    try:
        print "----------------------"
        print "Selection information:"
        
        #get selection
        SelectionLongName = cmds.ls( selection=True, long=True  )
        
        #transform to full name 
        if (".f[" in SelectionLongName[0]) or (".e[" in SelectionLongName[0]) or (".vtx[" in SelectionLongName[0])  or (".map[" in SelectionLongName[0]): #if face selected
            SelName = SelectionLongName[0] 
            head, sep, tail = SelName.partition('.') #find transform name - head 
            SelectionLongName = []
            SelectionLongName.append(head)
            cmds.select(SelectionLongName[0])        
        
        #shapes array                        
        all_sel_shapes = cmds.ls( selection=True, long=True, dagObjects=True, shapes=True)
        print "1. Shapes:", len(all_sel_shapes)
        
        for i in range(len(all_sel_shapes)):
            if cmds.objExists(all_sel_shapes[i]) == True:
                obj_type = cmds.objectType( all_sel_shapes[i] )                
                #processed mesh
                if obj_type == "mesh":
                    mesh_sel_shapes.append(all_sel_shapes[i])
                
        print "2. Mesh shapes:", len(mesh_sel_shapes)
        
        #transform array                                
        all_sel_transforms = cmds.ls ( selection=True, long=True, dagObjects=True, transforms=True)
        
        print "3. Transforms: ", len(all_sel_transforms)
        
        #joints array                               
        all_sel_joints = cmds.ls( selection=True, long=True, dagObjects=True, type='joint')
        
        print "4. Joints: ", len(all_sel_joints)        

        print ""
                              
    except:
        cmds.warning ("PolygonTools. Please select something. Mesh object for example.")

        if len(all_sel_transforms) == 0:
            cmds.warning("PolygonTools. Maybe you have problems with naming in scene.")
        
    return mesh_sel_shapes, all_sel_transforms, all_sel_shapes, all_sel_joints


#get short name
def shortNamer(long_name_data):
    full_name = str(long_name_data)                
    name_parts = full_name.split("|")
    #last element of array
    short_name = str(name_parts[-1])
    
    return short_name

#get short name
def shortNamerTransform (long_name_data):
    full_name = str(long_name_data)                
    name_parts = full_name.split("|")
    #last element of array
    short_name = str(name_parts[1])
    
    return short_name

#prepare scene Batch
def prepareScene():
    
    prep_scene_conclusion_data = []
    
    #STEP 1
    #get all hidden objects
    try:
        hiddenNodes=[]
        hiddenNodes = cmds.ls(invisible=True, type="transform")

        #standard names
        std_names = ['front','persp','side','top', 'transform']
    
        #only objects
        hiddenObjects =[]
        hiddenObjects = [s for s in hiddenNodes if not any(xs in s for xs in std_names)]
    
        cmds.showHidden( hiddenObjects )
        print "PolygonTools: All objects are Unhidden......OK"
        
        prep_scene_conclusion_data.append(True)
    except:
        prep_scene_conclusion_data.append(False)
        
    #STEP 2
    #Unhide layers and make in Normal
    try:
        layers = cmds.ls( type='displayLayer')  
        
        #for x in layers[0:]:
        for i in range(len(layers)):                      
            try:
                if layers[i] != 'defaultLayer':
                    cmds.setAttr('%s.visibility' % layers[i], 1)
                    cmds.setAttr("{}.displayType".format(layers[i]), 0)
            except:
                pass
    
        print "PolygonTools: All layers are Unhidden......OK"
        
        prep_scene_conclusion_data.append(True)
    except:
        prep_scene_conclusion_data.append(False)
                    
    #STEP 3
    #refresh scene
    try:
        cmds.refresh()
        print "PolygonTools: Viewport Refresh..............OK"
        
        prep_scene_conclusion_data.append(True)
    except:
        prep_scene_conclusion_data.append(False)
        
    #STEP 4
    #delete unused nodes
    try:
        maya.mel.eval('hyperShadePanelMenuCommand("hyperShadePanel1", "deleteUnusedNodes");')
        print "PolygonTools: Delete Unused Nodes in Hypershade..............OK"
        
        prep_scene_conclusion_data.append(True)
    except:
        prep_scene_conclusion_data.append(False)
        
    #STEP 5 - optimize
    try:
        maya.mel.eval("OptimizeScene;")
        print "PolygonTools: Optimize Scene..............OK"
        
        prep_scene_conclusion_data.append(True)
    except:
        prep_scene_conclusion_data.append(False)

    #STEP 6 - clenup
    try:
        maya.mel.eval("cleanUpScene 3;")
        print "PolygonTools: CleanUp Scene..............OK"
        
        prep_scene_conclusion_data.append(True)
    except:
        prep_scene_conclusion_data.append(False)
    
    return prep_scene_conclusion_data


#prepare viewport batch    
def prepareViewport():    

    prep_viewport_conclusion_data = []

    #STEP 1
    #clear selection
    try:
        cmds.select( clear=True )    
        prep_viewport_conclusion_data.append(True)
    except:
        prep_viewport_conclusion_data.append(False)


    #STEP 2
    #set 4 vievports
    try:
        maya.mel.eval('setNamedPanelLayout("Four View")')
        print "PolygonTools: Standart Layout........................OK"
        prep_viewport_conclusion_data.append(True)
    except:
        prep_viewport_conclusion_data.append(False)
                
    #STEP 3
    #Cam planes setup
    try:
        cmds.viewClipPlane('topShape', ncp=0.05, fcp=10000)
        cmds.viewClipPlane('frontShape', ncp=0.05, fcp=10000)
        cmds.viewClipPlane('sideShape', ncp=0.05, fcp=10000)
        cmds.viewClipPlane('perspShape', ncp=0.05, fcp=10000)
        print "PolygonTools: Cameras Far and Near Clip Setup........OK"
        prep_viewport_conclusion_data.append(True)
    except:
        prep_viewport_conclusion_data.append(False)
    
    #STEP 4
    #turn on Hedup display with stat in Prersp viewport Only
    try:
        maya.mel.eval('TogglePolyCount')
        maya.mel.eval('setPolyCountVisibility( on )')
        prep_viewport_conclusion_data.append(True)
    except:
        prep_viewport_conclusion_data.append(False)        
    
    #set inside viewport
    
    #STEP 5
    #top
    try:
        cmds.modelEditor( modelPanel='modelPanel1', da="smoothShaded", grid=False, displayLights="default", wireframeOnShaded=True, cameras=False, activeView=True)
        maya.mel.eval('modelEditor -e -hud false modelPanel1')    
        cmds.viewFit()
        prep_viewport_conclusion_data.append(True)
    except:
        prep_viewport_conclusion_data.append(False)        
    
    #STEP 6
    #side
    try:
        cmds.modelEditor( modelPanel='modelPanel2', da="smoothShaded", grid=False, displayLights="default", wireframeOnShaded=True, cameras=False, activeView=True)
        maya.mel.eval('modelEditor -e -hud false modelPanel2')
        cmds.viewFit()
        prep_viewport_conclusion_data.append(True)
    except:
        prep_viewport_conclusion_data.append(False)        

    #STEP 7
    #front
    try:
        cmds.modelEditor( modelPanel='modelPanel3', da="smoothShaded", grid=False, displayLights="default", wireframeOnShaded=True, cameras=False, activeView=True)
        maya.mel.eval('modelEditor -e -hud false modelPanel3')
        cmds.viewFit()
        prep_viewport_conclusion_data.append(True)
    except:
        prep_viewport_conclusion_data.append(False)                
        
    #STEP 8
    #persp
    try:
        cmds.modelEditor( modelPanel='modelPanel4', da="smoothShaded", grid=True, displayLights="default", cameras=False, activeView=True)
        prep_viewport_conclusion_data.append(True)
    except:
        prep_viewport_conclusion_data.append(False)        
    #STEP 9
    #turn off isolate
    try:
        cmds.isolateSelect( 'modelPanel1', state=False )
        cmds.isolateSelect( 'modelPanel2', state=False )
        cmds.isolateSelect( 'modelPanel3', state=False )
        cmds.isolateSelect( 'modelPanel4', state=False )
        prep_viewport_conclusion_data.append(True)
    except:
        prep_viewport_conclusion_data.append(False)        

    #STEP 10
    #camera setup default view
    try:
        cmds.xform('persp', t=(24,18,24), ro=(-27.938, 45.000, 0.000))
        cmds.tumble('perspShape', pivotPoint=(0,0,0))
        cmds.viewFit()    
        prep_viewport_conclusion_data.append(True)
    except:
        prep_viewport_conclusion_data.append(False)        

    print "PolygonTools: Standart Layout Panels Setup...........OK"
    
    #STEP 11
    #refresh scene
    try:
        cmds.refresh()
        print "PolygonTools: Viewport Refresh.......................OK"
        prep_viewport_conclusion_data.append(True)
    except:
        prep_viewport_conclusion_data.append(False)        

    return prep_viewport_conclusion_data

#prepare mesh batch    
def prepareMesh(selected_shapes, selected_transforms):
               
     prep_mesh_conclusion_data = []
      
     if len(selected_shapes) > 0:
         print "-----------------------------------------"
         print "     PolygonTools MESH PREPARE BATCH"
         print "-----------------------------------------"
        
        #STEP 1
         try:
            cmds.showHidden( all=True )
            print "PolygonTools: All objects are Unhidden............OK"
            prep_mesh_conclusion_data.append(True)
         except:
             prep_mesh_conclusion_data.append(False)
                                              
         print ""                        
        
        #STEP 2
         try:
            cmds.makeIdentity( apply=True, translate=1, rotate=1, scale=1 )
            print "PolygonTools: Freeze Transformation............OK"
            prep_mesh_conclusion_data.append(True)
         except:
            cmds.warning ("Can't Freeze Transformation... One of reason - model has incoming connection.") 
            prep_mesh_conclusion_data.append(False)           
        
         print "" 
        
        #STEP 3
        #Set Important Attributes 
         try:
             for i in range(len(selected_shapes)):
                
                obj_type = cmds.objectType( selected_shapes[i] )
                
                #processed mesh
                if obj_type == "mesh":                
                    print "#", i
                                  
                    cmds.setAttr((selected_shapes[i]+'.doubleSided'), 0)
                    print "PolygonTools: Double-sided is OFF for " + shortNamer(selected_shapes[i]) + ".......OK"
                    
                    cmds.setAttr((selected_shapes[i]+'.backfaceCulling'), 3)
                    print "PolygonTools: Backface Cull (Full) in ON for " + shortNamer(selected_shapes[i]) + ".......OK"
                    
                    print ""
                    
                    cmds.setAttr((selected_shapes[i]+'.displayBorders'), 1)
                    cmds.setAttr((selected_shapes[i]+'.vertexNormalMethod'), 3)
                    cmds.setAttr((selected_shapes[i]+'.displayCenter'), 0)
                    cmds.setAttr((selected_shapes[i]+'.displayNormal'), 0)
              
                else:
                    print "PolygonTools: Operation is not supported for this type of object:", shortNamer(selected_shapes[i]), "-", obj_type 
             
             prep_mesh_conclusion_data.append(True) 
         except:
             prep_mesh_conclusion_data.append(False)    
        
        #STEP 4        
         try:
             for i in range(len(selected_transforms)):   
                             
                cmds.setAttr((selected_transforms[i]+'.displayHandle'), 0)
                cmds.setAttr((selected_transforms[i]+'.displayRotatePivot'), 0)
                cmds.setAttr((selected_transforms[i]+'.displayScalePivot'), 0)
            
             prep_mesh_conclusion_data.append(True)
         except:
             prep_mesh_conclusion_data.append(False)
         
         print ""   
        
        #STEP 5
        #Delete color
         try:
            cmds.polyColorSet( delete=True )
            print "PolygonTools: Color Set Deleted.....................OK"
            prep_mesh_conclusion_data.append(True)
         except:
            print "PolygonTools: Color Set.....................OK"
            prep_mesh_conclusion_data.append(False)  
        
         print "" 
        
         #STEP 5
         #turn off isolate
         try:
             cmds.isolateSelect( 'modelPanel1', state=False )
             cmds.isolateSelect( 'modelPanel2', state=False )
             cmds.isolateSelect( 'modelPanel3', state=False )
             cmds.isolateSelect( 'modelPanel4', state=False )
             prep_mesh_conclusion_data.append(True)
         except:
             prep_mesh_conclusion_data.append(False)  
        
         print "" 
                    
        #STEP 6
        #cleanup
         print "Cleanup"
         try:
             for i in range(len(selected_shapes)):
              
                selected_shape = selected_shapes[i]
                
                maya.mel.eval('polyCleanupArgList selected_shape { "0","1","1","0","1","1","1","1","0","1e-05","0","1e-05","0","1e-05","0","-1","0","0" };')
                print "#", i, "PolygonTools: Cleanup Complete for", shortNamer(selected_shapes[i]), "...OK"
             prep_mesh_conclusion_data.append(True)
         except:
             prep_mesh_conclusion_data.append(False)            

         print ""              
        #STEP 7        
        #refresh scene
         try:
            cmds.refresh()
            print "PolygonTools: Viewport Refresh.....................OK"
            prep_mesh_conclusion_data.append(True)
         except:
            prep_mesh_conclusion_data.append(False)
                 
        #STEP 8
        #Delete history all
         try:
             for i in range(len(selected_transforms)): 
                cmds.delete(selected_transforms[i], constructionHistory=True )
                print "#", i, "PolygonTools: Delete History for", shortNamer(selected_transforms[i]) , "...OK"
             prep_mesh_conclusion_data.append(True)
         except:
             prep_mesh_conclusion_data.append(False)
                  
         print ""
        
         cmds.selectMode( object=True )
         cmds.select(clear=True)
         
         return prep_mesh_conclusion_data
      
#geometry statistics
def geoStat(shapes_transforms_array, selected_shapes, selected_transforms):

    #stat var
    unsupported_shapes_count = 0
    all_shapes_polycount =[]
    totalpoly = 0    
    totaltris = 0
    totalvert = 0
    totaluvvert = 0    
    
    unsupported_shapes_count = len(shapes_transforms_array[2]) - len(selected_shapes)
    
    for i in range(len(selected_shapes)):
        #polygons
        current_shape_poly = cmds.polyEvaluate(selected_shapes[i], f=True )      
        all_shapes_polycount.append(current_shape_poly)          
        totalpoly = totalpoly + current_shape_poly
        
        #tris
        current_shape_tris = cmds.polyEvaluate(selected_shapes[i], t=True )
        totaltris = totaltris + current_shape_tris
        
        #vertices
        current_shape_vert = cmds.polyEvaluate(selected_shapes[i], v=True )
        totalvert = totalvert + current_shape_vert
        
        #uv vertices
        current_uv_vert = cmds.polyEvaluate(selected_shapes[i], uv=True )
        totaluvvert = totaluvvert + current_uv_vert 
        
    return unsupported_shapes_count, all_shapes_polycount, totalpoly, totaltris, totalvert, totaluvvert

#overlap statistics
def overlapStat(selected_shapes, all_shapes_polycount):
    #overlap var
    UVoverlap = 0
    shapes_with_uv_overlaps = []
    full_UVOverlap = []
    shape_uv_area = []
    shape_geo_area = []
    ObjectsWithZeroArea = []
        
    for i in range(len(selected_shapes)):
        SelectedFacesTemp = [ selected_shapes[i] + '.f[:]']
        cmds.select(SelectedFacesTemp)
        
        UVoverlap = cmds.polyUVOverlap( overlappingComponents=True )        
                        
        if UVoverlap != None:
            shapes_with_uv_overlaps.append(UVoverlap)
            
            #if 100% overlap
            if len(UVoverlap)==all_shapes_polycount[i]:
                full_UVOverlap.append(selected_shapes[i])
        
        #get geo area of all faces
        FaceAreas = cmds.polyEvaluate( fa=True )
        shape_geo_area.append (FaceAreas) 
        
        #print zero area shapes
        if 0 in FaceAreas:
            ObjectsWithZeroArea.append(selected_shapes[i])
        
        #get are of all selected UVs
        shape_uv_area.append(cmds.polyEvaluate( ufa=True ))
    
    return shape_geo_area, shape_uv_area, shape_geo_area, shapes_with_uv_overlaps, full_UVOverlap, ObjectsWithZeroArea

#uvsets statistics
def uvSetStat(selected_shapes):
    #uvsets var
    total_uv_sets = 0
    one_uv_set =[]
    many_uv_sets = []    
    
    for i in range(len(selected_shapes)):
        
        total_uv_sets = cmds.polyUVSet(selected_shapes[i], query=True, auv=True )                
        
        if len(total_uv_sets) == 1:
            one_uv_set.append(selected_shapes[i])
        else:
            many_uv_sets.append(selected_shapes[i])
            
    return one_uv_set, many_uv_sets

#material statistics
def matStat(selected_shapes):
    #mat var
    one_mat=[]
    many_mat=[]

    for i in range(len(selected_shapes)):
        #all mats in scene
        MaterialList = cmds.ls(selected_shapes[i], mat=1)
          
        #Input Connections
        InConnections = cmds.listConnections (selected_shapes[i], type = "shadingEngine")
          
        #all Assigned Materials
        AssignedMat = cmds.ls( cmds.listConnections (InConnections), mat=1)
          
        #all Assigned Materials Number
        TotalAssignedMaterialsNumber = len(AssignedMat) 
          
        #Get only Unique Materials  
        unique_mat=[]
                        
        for ix in AssignedMat:
            if ix not in unique_mat:
                unique_mat.append(ix)  
          
        if len(unique_mat) > 0:
            print "Assigned Material(s) Name(s) for", shortNamer(selected_shapes[i]), ":"                        
          
        for iz in range(0, len(unique_mat)):
            print iz+1, '-', unique_mat[iz]                
    
        if len(unique_mat) == 1:
            one_mat.append(selected_shapes[i])
        else:
            many_mat.append(selected_shapes[i])
    
    return one_mat, many_mat, unique_mat

#uv range statistics
def uvRangeStat(selected_shapes):
    #mat var
    uv_outside=[]
    
    #UV-vertex outside the 1-0
    for i in range(len(selected_shapes)):
        BBox2D = cmds.polyEvaluate(selected_shapes[i], b2=True )                
        for ix in range(len(BBox2D)):
            for j in range(len(BBox2D[ix])):
                if (BBox2D[ix][j] < 0.0) or (BBox2D[ix][j] > 1.0):
                    uv_outside.append (selected_shapes[i])
    
    #unique shapes with UV outside
    unique_shape_outside=[]
    
    for iz in uv_outside:
        if iz not in unique_shape_outside:
            unique_shape_outside.append(iz)
            
    for i in range(len(unique_shape_outside)):
        print str(i+1), "-", shortNamer(unique_shape_outside[i]), "- UV not in [0,1] range" 

    return uv_outside, unique_shape_outside

def uvShellsStat(selected_shapes):
    #uvshell var
    uv_shells_all = []
    uv_shells_total = 0
    
    for i in range(len(selected_shapes)):
        uv_shells = cmds.polyEvaluate(selected_shapes[i], us=True )
        uv_shells_all.append(uv_shells)    
        print "UV-Shells:", shortNamer(selected_shapes[i]), "-", uv_shells
    
    uv_shells_total = sum(uv_shells_all)
    
    return uv_shells_all, uv_shells_total

#UV utilization
def uvUtilStat(shape_name):
    
    pixmap = QPixmap(QSize(100,100))
    painter = QPainter()
    colorWhite = QColor()
    colorBlack = QColor()

    colorWhite.setRgb(255,255,255,255)
    colorBlack.setRgb(0,0,0,255)
    pixmap.fill(colorBlack)
    
    TempExistShapeArray = []
    ShapeErrors = []
    
    #check shape exist    
    # 12 = Polygon
    try:
        obj = cmds.filterExpand(shape_name, selectionMask=12)
    except:
        obj = None
        pass
            
    if obj != None:
        for o in obj:
            #start processing object
            # 1 - get current uv set
            currentUVSet = cmds.polyUVSet(o, q=1, currentUVSet=1)
            
            #check if the object has some uvs
            numUVs = cmds.polyEvaluate(o, uvcoord=1)

            if numUVs > 0:
                # 2 - drawing uv shells

                selectionList = OpenMaya.MSelectionList()

                selectionList.add(o)
                
                dagPath = OpenMaya.MDagPath() 
                mObject = OpenMaya.MObject()

                selectionList.getDagPath(0, dagPath, mObject)

                iter = OpenMaya.MItMeshPolygon(dagPath)
                
                while not iter.isDone():
                    uCoord = OpenMaya.MFloatArray()
                    vCoord = OpenMaya.MFloatArray()
                    iter.getUVs(uCoord, vCoord, currentUVSet[0])
                    uvCount = uCoord.length()
                    #print "face: ", uCoord, vCoord

                    QArray = QPolygonF()
                    
                    for i in range(len(uCoord)):
                        curU = int(uCoord[i] * 100)
                        curV = 100 - int(vCoord[i] * 100)
                        point = QPointF(curU, curV)
                            # print point
                        QArray.append(point)
                        # print "formated: ", QArray #QArray wrong

                    painter.begin(pixmap)
                    painter.setBrush(QBrush(colorWhite))
                    painter.setPen(colorWhite)
                    painter.drawConvexPolygon(QArray)
                    painter.end()                    
                    iter.next()


                #3 - get black pixels and get area = 10000 - len(blackPixels)
                blackPixelCount = 0
                
                img = pixmap.toImage()
                
                for i in range(0,100):
                    for j in range(0,100):
                        color = QColor()
                        color = QColor.fromRgb(img.pixel(i,j))
                        if color == Qt.black:
                            blackPixelCount += 1
                
                precentage = 100 - blackPixelCount / 100 #by 1 %                
            else:
                precentage = 0
    else:
        precentage = 0
    return precentage, pixmap
