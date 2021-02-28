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
import maya._OpenMayaUI as omui


from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtUiTools import * 
from shiboken2 import wrapInstance

from polygon_tools import *
from pt_modules.pt_gui import *
from pt_modules.pt_gen_func import *
from pt_modules.pt_set_func import *

global loading_counter
loading_counter = 0


def MySysInfo():
    import platform;
    print ("PolygonTools. SYS INFO: " + (platform.sys.version));
    
def ConfigWriter(Section, Variable, Value, path, config):
    
    pt_configfile_path = path
    
    ptconfig = config
     
    try:
        ptconfig.set(Section, Variable, Value + '\n\r')
    except:
        cmds.error("error_message_01" + " ConfigWriter.Set")
        MySysInfo()
            
    try:
        with open(pt_configfile_path, 'w') as cfg:
            ptconfig.write(cfg)
            print ("PolygonTools. " + "[" + Section + "] " + Variable +" = "+ Value + " write to config file.")
    except:
        cmds.error("error_message_01" + " ConfigWriter.Open")
        MySysInfo()
        
    
#read config file and send data to pt_gen_func
def readValuesFromConfig(ptconfig, pt_configfile_path):

    #call function count    
    global loading_counter
    loading_counter = loading_counter + 1
        
    #global read_cfg_error_count
    read_cfg_error_count = 0
    config_values=[]
    
    #0    
    try:
        map_resolution = ptconfig.get('Texel', 'map_resolution')
        config_values.append(map_resolution)
    except:
        print "PolygonTools. ERROR: Can't read Map resolution value from config file."
        read_cfg_error_count = read_cfg_error_count + 1
        ptconfig.add_section("Texel")
        ptconfig.set('Texel', 'map_resolution', '3\n\r')

    #1
    try:
        TexelValue = ptconfig.get('In-Range', 'Texel')
        config_values.append(TexelValue)
    except:
        print "PolygonTools. ERROR: Can't read Texel value from config file."
        read_cfg_error_count = read_cfg_error_count + 1
        ptconfig.add_section("In-Range")
        ptconfig.set('In-Range', 'Texel', '256\n\r')
    
    #2    
    try:
        DiffValue = ptconfig.get('In-Range', 'Difference')
        config_values.append(DiffValue)
    except:
        print "PolygonTools. ERROR: Can't read Difference value from config file."
        read_cfg_error_count = read_cfg_error_count + 1
        ptconfig.set('In-Range', 'Difference', '20\n\r')
    
    #3    
    try:
        TinyItValue = ptconfig.get('In-Range', 'Tiny_it')
        config_values.append(TinyItValue)
    except:
        print "PolygonTools. ERROR: Can't read Tiny_it value from config file."
        read_cfg_error_count = read_cfg_error_count + 1
        ptconfig.set('In-Range', 'Tiny_it', '0.0001\n\r')
    
    #4    
    try:
        TinyUvValue = ptconfig.get('In-Range', 'Tiny UV')
        config_values.append(TinyUvValue)
    except:
        print "PolygonTools. ERROR: Can't read Tiny UV value from config file."
        read_cfg_error_count = read_cfg_error_count + 1
        ptconfig.set('In-Range', 'Tiny UV', '1\n\r')
    
    #5    
    try:
        lod1value = ptconfig.get('LOD_distance', 'lod1') 
        config_values.append(lod1value)
    except:
        print "PolygonTools. ERROR: Can't read lod1 value from config file."
        read_cfg_error_count = read_cfg_error_count + 1
        ptconfig.add_section("LOD_distance")
        ptconfig.set('LOD_distance', 'lod1', '10\n\r')
    
    #6    
    try:
        lod2value = ptconfig.get('LOD_distance', 'lod2')
        config_values.append(lod2value)
    except:
        print "PolygonTools. ERROR: Can't read lod2 value from config file."
        read_cfg_error_count = read_cfg_error_count + 1
        ptconfig.set('LOD_distance', 'lod2', '20\n\r')
    
    #7    
    try:
        lod3value = ptconfig.get('LOD_distance', 'lod3')
        config_values.append(lod3value)
    except:
        print "PolygonTools. ERROR: Can't read lod3 value from config file."
        read_cfg_error_count = read_cfg_error_count + 1
        ptconfig.set('LOD_distance', 'lod3', '40\n\r')
        
    #8
    try:
        lod4value = ptconfig.get('LOD_distance', 'lod4')
        config_values.append(lod4value)
    except:
        print "PolygonTools. ERROR: Can't read lod4 value from config file."
        read_cfg_error_count = read_cfg_error_count + 1
        ptconfig.set('LOD_distance', 'lod4', '60\n\r')
    
    #9
    try:
        CustomSysUnits = ptconfig.get('Units', 'Custom_System_type_units')
        config_values.append(CustomSysUnits)
    except:
        print "PolygonTools. ERROR: Can't read Custom_System_type_units value from config file."
        read_cfg_error_count = read_cfg_error_count + 1
        ptconfig.add_section("Units")
        ptconfig.set('Units', 'Custom_System_type_units', 'm\n\r')

    #10
    try:
        CustomDispUnits = ptconfig.get('Units', 'Custom_Display_units')
        config_values.append(CustomDispUnits)
    except:
        print "PolygonTools. ERROR: Can't read Custom_Display_units value from config file."
        read_cfg_error_count = read_cfg_error_count + 1
        ptconfig.set('Units', 'Custom_Display_units', 'Generic\n\r')
    
    #11    
    try:
        desired_texel = ptconfig.get('Texel', 'desired_texel')
        config_values.append(desired_texel)
    except:
        print "PolygonTools. ERROR: Can't read desired texel value from config file."
        read_cfg_error_count = read_cfg_error_count + 1
        ptconfig.set('Texel', 'desired_texel', '400\n\r')
    
    #12    
    try:
        intersection_depth = ptconfig.get('Tools', 'intersection_depth')
        config_values.append(intersection_depth)
    except:
        print "PolygonTools. ERROR: Can't read intersection depth value from config file."
        read_cfg_error_count = read_cfg_error_count + 1
        ptconfig.add_section("Tools")
        ptconfig.set('Tools', 'intersection_depth', '10\n\r')
        
    #13    
    try:
        target_face_count = ptconfig.get('Tools', 'target_face_count')
        config_values.append(target_face_count)
    except:
        print "PolygonTools. ERROR: Can't read target face count value from config file."
        read_cfg_error_count = read_cfg_error_count + 1
        ptconfig.set('Tools', 'target_face_count', '100\n\r')

    #14    
    try:
        current_languge = ptconfig.get('Languge', 'current_languge')
        config_values.append(current_languge)
    except:
        print "PolygonTools. ERROR: Can't read current languge value from config file."
        read_cfg_error_count = read_cfg_error_count + 1
        ptconfig.add_section("Languge")
        ptconfig.set('Languge', 'current_languge', 'eng')

        
    #add empty for future
    for i in range(0, 83):
        config_values.append("Empty")
    
    #98    
    config_values.append(read_cfg_error_count) 
        
    #Fix wrong values
    if read_cfg_error_count > 0:
        try:
            with open(pt_configfile_path, 'w') as cfg:
                ptconfig.write(cfg)
                ptconfig.close()
                print "PolygonTools. Some values not read (see log above). Default values was write to file."
        except:
            cmds.error("error_message_01" + " ReadValuesFromConfig.Open") 
            MySysInfo()
    else:
        if loading_counter == 1:
            print "PolygonTools. Data from config file was loaded."

    
    return config_values


def ValueSender():
    return CustomSysUnits

#write config file with default values
def CreateDefaultConfig (ptconfig, pt_configfile_path):        
    
    print "----"
    print "Restore sections and values:"
    print "" 
    
    try:
        import configparser as cfgp
    except:
        import ConfigParser as cfgp

    #Add all default values to file
    try:
        ptconfig.add_section("Texel")
        print "Texel section restored!"
        ptconfig.set('Texel', 'Map_resolution', '3\n\r')
        ptconfig.set('Texel', 'desired_texel', '400\n\r')
    except cfgp.DuplicateSectionError:
        ptconfig.set('Texel', 'Map_resolution', '3\n\r')
        ptconfig.set('Texel', 'desired_texel', '400\n\r')
    finally:
        print "Texel values restored!"
    
    try:    
        ptconfig.add_section("In-Range")
        print "In-Range section restored!"
        ptconfig.set('In-Range', 'Texel', '256\n\r')
        ptconfig.set('In-Range', 'Difference', '10\n\r')
        ptconfig.set('In-Range', 'Tiny_it', '0.0001\n\r')
        ptconfig.set('In-Range', 'Tiny UV', '1\n\r')
    except cfgp.DuplicateSectionError:
        ptconfig.set('In-Range', 'Texel', '256\n\r')
        ptconfig.set('In-Range', 'Difference', '10\n\r')
        ptconfig.set('In-Range', 'Tiny_it', '0.0001\n\r')
        ptconfig.set('In-Range', 'Tiny UV', '1\n\r')
    finally:
        print "In-Range values restored!"
    
    try:    
        ptconfig.add_section("LOD_distance")
        print "LOD_distance section restored!"
        ptconfig.set('LOD_distance', 'lod1', '10\n\r')
        ptconfig.set('LOD_distance', 'lod2', '20\n\r')
        ptconfig.set('LOD_distance', 'lod3', '40\n\r')
        ptconfig.set('LOD_distance', 'lod4', '60\n\r')
    except cfgp.DuplicateSectionError:
        ptconfig.set('LOD_distance', 'lod1', '10\n\r')
        ptconfig.set('LOD_distance', 'lod2', '20\n\r')
        ptconfig.set('LOD_distance', 'lod3', '40\n\r')
        ptconfig.set('LOD_distance', 'lod4', '60\n\r')
    finally:
        print "LOD_distance values restored!"
        

    try:        
        ptconfig.add_section("Units")
        print "Units section restored!"
        ptconfig.set('Units', 'Custom_System_type_units', 'm\n\r')
        ptconfig.set('Units', 'Custom_Display_units', 'Generic\n\r')
    except cfgp.DuplicateSectionError:
        ptconfig.set('Units', 'Custom_System_type_units', 'm\n\r')
        ptconfig.set('Units', 'Custom_Display_units', 'Generic\n\r')
    finally:
        print "Units value restored!"
    
    try:    
        ptconfig.add_section("Tools")
        print "Tools section restored!"
        ptconfig.set('Tools', 'intersection_depth', '10\n\r')
        ptconfig.set('Tools', 'target_face_count', '100\n\r')
    except cfgp.DuplicateSectionError:
        ptconfig.set('Tools', 'intersection_depth', '10\n\r')
        ptconfig.set('Tools', 'target_face_count', '100\n\r')
    finally:
        print "Tools values restored!"


    try:
        ptconfig.add_section("Languge")
        print "Languge section restored!"
        ptconfig.set('Languge', 'current_languge', 'eng')
    except cfgp.DuplicateSectionError:
        ptconfig.set('Languge', 'current_languge', 'eng')
    finally:
        print "Languge values restored!"
        
    print ""
        
    #Try to save data to the config file
    try:
        with open(pt_configfile_path, 'w') as cfg:
            ptconfig.write(cfg)
            print "PolygonTools. Config file with default values was successfully created! Please reload PolygonTools."
    except:
        cmds.error("error_message_01" + " CreateDefaultConfig.Open") 
        MySysInfo()


def getConfigFilePath():
    #get current dir
    currentDir = os.path.dirname(__file__)
    
    #config file
    ptconfigfile = 'polygontoolspack_settings.ini'
    
    #path to config file
    pt_configfile_path = currentDir + "/" + ptconfigfile

    return pt_configfile_path


def getPTConfig():

    try:
        from configparser import ConfigParser
    except ImportError:
        from ConfigParser import ConfigParser  # ver. < 3.0
    
    #config data
    ptconfig = ConfigParser()
    
    return ptconfig

    
#Data loader
def configLoader():
    
    global loading_counter
    
    pt_configfile_path = getConfigFilePath() 
    
    #config data
    ptconfig = getPTConfig()
                
    try:
        if os.path.getsize(pt_configfile_path) > 0:
            ptconfig.read(pt_configfile_path)
            
            read_data = readValuesFromConfig(ptconfig, pt_configfile_path)
            
            #add new data
            read_data.append(pt_configfile_path)
            read_data.append(ptconfig)
            
            #13 - number of read problems            
            if (read_data[98] == 0):
                if loading_counter == 1:                
                    print "PolygonTools: Config file was successfully read!"
                    print "PolygonTools: Path to config:", read_data[99]
                    print "---------------------" 
            else:
                print "------------------------------------------------"
                print ("PolygonTools: ATTENTION! Config file was read with " + str(read_cfg_error_count) + " errors! Default values was loaded.")
                        
        else:
            CreateDefaultConfig(ptconfig, pt_configfile_path)
    
    except OSError as e:
        try: 
            print "PolygonTools: PT_CONFIG_LOADER. ATTENTION! Config File does not exists or is non accessible!"
            MySysInfo()
            ptconfig = open(pt_configfile_path,'w')
            print ("PolygonTools: PT_CONFIG_LOADER. Empty Config file was successfully created " + pt_configfile_path)
            ptconfig.close()
        except:
            cmds.error("error_message_01" + " ConfigLoader.OSError") 
     
    return read_data          