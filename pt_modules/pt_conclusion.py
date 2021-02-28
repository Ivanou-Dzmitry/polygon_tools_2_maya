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

#current languages eng, rus

import os
import maya.cmds as cmds


#intro text for gen tab
def genTabIntroConclusion(language):
    if language == "rus":
        full_conclusion_text = "<span style=\"color:#8dc63f\">Здравствуйте!</span><br>После выполнения каких-либо действий в PolygonTools в этом окошке можно будет прочитать, \
            что произошло. Иногда, тут будут полезные советы или краткое описание проблемы.<br> \
                Сейчас вы находитесь на вкладке, где можно подготовить геометрию, сцену и вьюпорт к проверке, а также получить статистику и узнать размеры объектов. \
                    <br><span style=\"color:#00bff3\">Успехов в работе! Ваш PolygonTools</span> :-)"
    elif language=="eng":
        full_conclusion_text = "<span style=\"color:#8dc63f\">Hello!</span><br>After performing any actions in PolygonTools in this window you can read \
            what happened. Sometimes there will be useful tips or a brief description of the problem.<br> \
                Now you are on the tab where you can prepare the geometry, scene and viewport for feedback. As well as get statistics and find out the sizes of objects. \
                    <br><span style=\"color:#00bff3\">Good luck in job! Your PolygonTools</span> :-)"
    
    return full_conclusion_text

#intro text for Texel tab
def texTabIntroConclusion(language):
    if language == "rus":
        full_conclusion_text = "Сейчас вы находитесь на вкладке, где можно узнать тексель на выбранном полигоне, задать тексель для всей модели или проверить его равномерность. <br>\
            Как правило, тексель измеряется на одном выбранном полигоне. Если вы не выберете конкретный полигон вручную — будет выбран случайный (автоматически). \
                Измерять тексель на модели без финальной UV-развертки в большинстве случаев бессмысленно. \
                    <br><span style=\"color:#00bff3\">Успехов в работе! Ваш PolygonTools</span> :-)"
    elif language=="eng":
        full_conclusion_text = "Now you are on the tab where you can get texel on the selected polygon, set the texel for the entire model or check its uniformity. \
        Typically texel is measured at one selected polygon. If you do not select a specific polygon manually a random one will be selected (automatically). \
        Measuring texel on a model without a final UV-layout in most cases is pointless. \
            <br><span style=\"color:#00bff3\">Good luck in job! Your PolygonTools</span> :-)"
    
    return full_conclusion_text

#intro text for UV tab
def uvTabIntroConclusion (language):
    if language == "rus":
        full_conclusion_text = "Сейчас вы находитесь на вкладке, где можно назначить на модель различные виды чекеров, а также совершить некоторые простые операции над UV-разверткой. <br>\
            Чекер — вспомогательная текстура, которая применяется до создания финальной текстуры. Чекер помогает увидеть искажения и отражения на UV-развертке и другие проблемы. \
                Чекера бывают разного типа, для разных нужд. В PolygonTools представлены лишь некоторые, самые полезные, по мнению авторов. В любом случае, выбор чекера остается за вами. \
                    <br><span style=\"color:#00bff3\">Успехов в работе!</span>"
    elif language=="eng":
        full_conclusion_text = "Now you are on the tab where you can assign various types of checkers to the model. As well as perform some simple UV-layout operations. \
        Checker is an auxiliary texture that is applied before the final texture is created. The checker helps to see distortions and miroring on the UV-layout and other problems. \
        Checkers come in different types for different needs. In PolygonTools only some of the most useful are presented (according to the authors). In any case the choice of checker is yours. \
            <br><span style=\"color:#00bff3\">Good luck in job!</span>"
    
    return full_conclusion_text

#intro text for Tool tab
def toolTabIntroConclusion (language):
    if language == "rus":
        full_conclusion_text = "Сейчас вы находитесь на вкладке с полезными инструментами. <br>\
            Здесь можно назначить на объект проверочные шейдеры или полностью удалить материалы. Проверить ЛОДы и пересечение элементов. Сделать простейшую ретопологию и отрендерить превью \
                    <br><span style=\"color:#00bff3\">Успехов в работе!</span>"
    elif language=="eng":
        full_conclusion_text = "Now you are on the tab with useful tools.<br>\
            Here you can assign test shaders to the object or completely delete materials. Check LODs and intersection of elements. Make simple retopology and render preview. \
                <br><span style=\"color:#00bff3\">Good luck in job!</span>"
    
    return full_conclusion_text

#intro text for Tool tab
def checkerTabIntroConclusion (language):
    if language == "rus":
        full_conclusion_text = "Сейчас вы находитесь на вкладке с Polygon-чекером. <br>\
            С помощью чекера можно проверить модель по определенным объективным критериям и понять, готова ли она к фидбэку или финальной приемке. \
                Выберитер один или несколько объектов типа mesh и запустите проверку. Часть информации будет выведена на экран напротив пунктов. Дополнительная информация, особенно если \
                    проверялось несколько объектов, будет в логе Script Editor. Зеленый маркер - все в порядке, желтый - возможно стоит обратить внимание, красный - скорее всего есть проблема. \
                        Если напротив пункта активна кнопка Fix - проблему можно решить. Как правило, это будет простое или временное решение. Финальные правки за вами. \
                    <br><span style=\"color:#00bff3\">Успехов в работе!</span>"
    elif language=="eng":
        full_conclusion_text = "Now you are on the tab with the Polygon checker. <br>\
            Using the checker you can check the model against certain objective criteria and see if it is ready for feedback or final acceptance. \
                Select one or more mesh objects and run the Check. Part of the information will be displayed opposite the items. Additional information especially\
                    if several objects were checked will be in the Script Editor log. The green marker - everything is in OK. Yellow - perhaps it is worth paying attention. Red - most likely there is a problem. \
                        If the Fix button is active opposite the item the problem can be solved. Usually this is a simple or temporary solution. Final edits are yours.\
                        <br><span style=\"color:#00bff3\">Good luck in job!</span>"
    
    return full_conclusion_text


#intro text for gen tab
def noSelection(language, action_type):

    currentDir = os.path.dirname(__file__)
    try:
        iconEmpty = currentDir +"/icons/empty_icon.png"

        iconMesh = currentDir +"/icons/mesh_icon.png"
        iconScene = (currentDir +"/icons/scene_icon.png")
        iconViewport = (currentDir +"/icons/viewport_icon.png")
        iconStat = (currentDir +"/icons/stat_icon.png")
        iconDim = currentDir +"/icons/dim_icon.png"

        #Texel Tab
        iconGetTex  = currentDir + "/icons/gettexel_icon.png"
        iconSetTex  = currentDir + "/icons/settexel_icon.png"
        iconSetTex  = currentDir + "/icons/settexel_icon.png"
        iconCheckTex  = currentDir +"/icons/checktexel_icon.png"
        iconCleanCheck  = currentDir +"/icons/cleancheck_icon.png"

        #UV tab
        iconScaleUV2  = (currentDir +"/icons/scale_uv2_icon.png")
        iconScaleUV05  = (currentDir +"/icons/scale_uv05_icon.png")
        iconMoveVUp  = (currentDir +"/icons/move_v_up_icon.png")
        iconMoveVDown  = (currentDir +"/icons/move_v_down_icon.png")
        iconMoveURight  = (currentDir +"/icons/move_u_right_icon.png")
        iconMoveULeft  = (currentDir +"/icons/move_u_left_icon.png")
        iconShowUV  = (currentDir +"/icons/show_uv_icon.png")
        iconRemoveChecker  = (currentDir +"/icons/remove_checker_icon.png")

        #Tool tab
        iconFBXExport  = (currentDir +"/icons/fbxexport_icon.png")
        iconDelMat  = (currentDir +"/icons/delete_mat_icon.png")
        iconMateMat  = (currentDir +"/icons/mate_mat_icon.png")
        iconGlossMat  = (currentDir +"/icons/gloss_mat_icon.png")
        iconIntersect  = (currentDir +"/icons/intersection_icon.png")
        iconRetop  = (currentDir +"/icons/retop_icon.png")
        iconLod  = (currentDir +"/icons/lod_check_icon.png")
        iconRendPrev  = (currentDir +"/icons/render_prev_icon.png")            

        #Check tab
        iconChecker  = (currentDir +"/icons/checker_icon.png")

    except:
        cmds.warning( "PolygonTools: Can't load icons for General Tab! Check icon files in pt_modules/icons directory.")
        
    if action_type == "prepare_mesh":
        unique_action_text_rus = "подготовить геометрию"
        unique_action_text_eng = "prepare mesh"
        button_name = " Mesh "
        icon = iconMesh

    if action_type == "dimension":
        unique_action_text_rus = "узнать размер объекта"
        unique_action_text_eng = "get dimension"
        button_name = " Get dimension "
        icon = iconDim 

    if action_type == "statisctics":
        unique_action_text_rus = "узнать статистику"
        unique_action_text_eng = "get statistics"
        button_name = " Get Statistics "
        icon = iconStat 

    if action_type == "check_texel":
        unique_action_text_rus = "узнать значение текселя"
        unique_action_text_eng = "get texel"
        button_name = " Get Texel "
        icon = iconGetTex

    if action_type == "set_texel":
        unique_action_text_rus = "задать значение текселя"
        unique_action_text_eng = "set texel"
        button_name = " Set Texel "
        icon = iconSetTex

    if action_type == "check_texel":
        unique_action_text_rus = "проверить значение текселя"
        unique_action_text_eng = "check texel"
        button_name = " Check Texel "
        icon = iconCheckTex
        
    if action_type == "clean_check":
        unique_action_text_rus = "очистить результаты проверки текселя"
        unique_action_text_eng = "clean check result"
        button_name = " Clean Check "
        icon = iconCleanCheck

#UV
    if action_type == "scale_uv_up":
        unique_action_text_rus = "увеличить масштаб UV-развертки"
        unique_action_text_eng = "increase UV-layout scale"
        button_name = " x2 "
        icon = iconScaleUV2

    if action_type == "scale_uv_down":
        unique_action_text_rus = "уменьшить масштаб UV-развертки"
        unique_action_text_eng = "decrease UV-layout scale"
        button_name = " x0.5 "
        icon = iconScaleUV05               

    if action_type == "move_uv_left":
        unique_action_text_rus = "сдвинуть UV-расзвертку влево"
        unique_action_text_eng = "move UV-layout left"
        button_name = " -1U "
        icon = iconMoveULeft               

    if action_type == "move_uv_right":
        unique_action_text_rus = "сдвинуть UV-расзвертку вправо"
        unique_action_text_eng = "move UV-layout right"
        button_name = " +1U "
        icon = iconMoveURight               

    if action_type == "move_uv_up":
        unique_action_text_rus = "сдвинуть UV-расзвертку вверх"
        unique_action_text_eng = "move UV-layout up"
        button_name = " +1V "
        icon = iconMoveVUp              

    if action_type == "move_uv_down":
        unique_action_text_rus = "сдвинуть UV-расзвертку вниз"
        unique_action_text_eng = "move UV-layout down"
        button_name = " -1V "
        icon = iconMoveVDown

    if action_type == "assign_std_checker":
        unique_action_text_rus = "хотите назначить стандартный чекер"
        unique_action_text_eng = "assign standard checker"
        button_name = " Standard "
        icon = iconEmpty             

    if action_type == "assign_dig_checker":
        unique_action_text_rus = "хотите назначить цифровой чекер"
        unique_action_text_eng = "assign digital checker"
        button_name = " Digital "
        icon = iconEmpty             

    if action_type == "assign_diag_checker":
        unique_action_text_rus = "хотите назначить диагональный чекер"
        unique_action_text_eng = "assign diagonal checker"
        button_name = " Diagonal "
        icon = iconEmpty              

    if action_type == "assign_grad_checker":
        unique_action_text_rus = "хотите назначить градиентный чекер"
        unique_action_text_eng = "assign gradient checker"
        button_name = " Gadient "
        icon = iconEmpty              

    if action_type == "show_uv":
        unique_action_text_rus = "хотите увидеть UV-развертку в виде текстуры на объекте"
        unique_action_text_eng = "want to see a UV-layout as a texture on the objects"
        button_name = " Show UV "
        icon = iconShowUV            
    
    #tool del_mat

    if action_type == "del_mat":
        unique_action_text_rus = "хотите удалить материалы"
        unique_action_text_eng = "want to delete materials"
        button_name = " Delete "
        icon = iconDelMat            

    if action_type == "gloss_mat":
        unique_action_text_rus = "хотите назначить глянцевый материал"
        unique_action_text_eng = "want to assign gloss material"
        button_name = " Gloss "
        icon = iconGlossMat            

    if action_type == "mate_mat":
        unique_action_text_rus = "хотите назначить матовый материал"
        unique_action_text_eng = "want to assign mate material"
        button_name = " Mate "
        icon = iconMateMat                      

    if action_type == "fbx_exp":
        unique_action_text_rus = "хотите что-то экспортировать в FBX"
        unique_action_text_eng = "want to export somethcing to FBX"
        button_name = " To FBX "
        icon = iconFBXExport                      

    if action_type == "check_intersect":
        unique_action_text_rus = "хотите проверить пересечение объектов"
        unique_action_text_eng = "want to check object intersection"
        button_name = " Check "
        icon = iconIntersect

    if action_type == "retop":
        unique_action_text_rus = "хотите сделать ретопологию"
        unique_action_text_eng = "want to retop"
        button_name = " Set "
        icon = iconRetop

    if action_type == "checker":
        unique_action_text_rus = "хотите запустить проверку"
        unique_action_text_eng = "want to check"
        button_name = " Check "
        icon = iconChecker

    if language == "rus":
        full_conclusion_text = "Вы хотите " + unique_action_text_rus + ", <span style=\"color:#ffc000\">но видимо ничего не выбрано или объект не типа mesh...</span> \
            Многие функции в PolygonTools работают <b>только</b> с выделенным в режиме Object Mode объектом типа mesh. Можно выбрать и трансформ, а уж дальше он сам найдет подходящий объект (если он есть). \
                <br><span style=\"color:#00bff3\">Что делать?</span> Все просто! Выберите то, что вам необходимо во вьюпорте или Outliner (Object Mode) и попробуйте нажать кнопку <img src=\""+ icon + "\">"+ button_name +" еще раз. <br> \
                    P.S. Кстати, с помощью некоторых функций можно обработать не один, а несколько объектов за раз и получить сводную информацию."
    elif language == "eng":
        full_conclusion_text = "You want to " + unique_action_text_eng + ", <span style=\"color:#ffc000\">but apparently nothing is selected or not mesh object selected...</span> \
            Many functions in PolygonTools work only with a selected in Object Mode mesh-type object. You can choose a transform and Tools will find a suitable object (if they present). \
                <br><span style=\"color:#00bff3\">What to do?</span> It's simple! Select what you need in the viewport or Outliner (Object Mode) and try to click the <img src=\""+ icon + "\">"+ button_name +" button again. <br> \
                    P.S. By the way you can process several objects at a time and get summary information (actual for some functions)."
    
    return full_conclusion_text



def prepMeshConclusion(language, conclusion_data):

    conclusion_text = []
    
    result_true_rus = []
    result_false_rus = []

    result_true_eng = []
    result_false_eng = []
    
    #0
    result_true_rus.append("<span>Все объекты на сцене были сделаны видимыми. </span>")
    result_true_eng.append("<span>All objects on the scene were made visible. </span>")
    
    result_false_rus.append("<span style=\"color:#ed1c24\">Хмм... Не смог сделать видимыми все объекты на сцене. </span>")
    result_false_eng.append("<span style=\"color:#ed1c24\">Hmm ... I could not make all the objects on the scene visible. </span>")

    #1
    result_true_rus.append("<span>Сделал Freeze Transformation. </span>")
    result_true_eng.append("<span>Freeze Transformation complete. </span>")
    
    result_false_rus.append("<span style=\"color:#ed1c24\">Проблемы с Freeze Transformation. Возможная причина — модель имеет входящее соединения. </span>")
    result_false_eng.append("<span style=\"color:#ed1c24\">Can't Freeze Transformation. One of reason — model has incoming connection. </span>")

    #2
    result_true_rus.append("<span>Включил нужные атрибуты и выключил ненужные. </span>")
    result_true_eng.append("<span>Turned on the necessary attributes and turned off unnecessary ones. </span>")
    
    result_false_rus.append("<span style=\"color:#ed1c24\">Не смог вкл-выкл некоторые атрибуты. </span>")
    result_false_eng.append("<span style=\"color:#ed1c24\">Could not turn on-off some attributes.. </span>")

    #3
    result_true_rus.append("<span>Продолжил с атрибутами и выключил еще несколько. </span>")
    result_true_eng.append("<span>Continued with attributes and turned off a few more. </span>")
    
    result_false_rus.append("<span style=\"color:#ed1c24\">Несколько атрибутов не выключаются. </span>")
    result_false_eng.append("<span style=\"color:#ed1c24\">Some attributes do not turn off. </span>")

    #4
    result_true_rus.append("<span>Удалил Color Set'ы. </span>")
    result_true_eng.append("<span>Color Set Deleted. </span>")
    
    result_false_rus.append("<span >Color Set'ов не было в сцене. </span>")
    result_false_eng.append("<span >No Color Sets on scene. </span>")

    #5
    result_true_rus.append("<span>Отключил Isolate-режим для всех вьюпортов. </span>")
    result_true_eng.append("<span>Disable Isolate mode for all viewports. </span>")
    
    result_false_rus.append("<span style=\"color:#ed1c24\">Isolate-режим для вьюпортов не отключается. </span>")
    result_false_eng.append("<span style=\"color:#ed1c24\">Can't disable Isolate mode for viewports. </span>")

    #6
    result_true_rus.append("<span>Сделал Cleanup. </span>")
    result_true_eng.append("<span>Cleanup complete. </span>")
    
    result_false_rus.append("<span style=\"color:#ffc000\">С Cleanup возникли проблемы! </span>")
    result_false_eng.append("<span style=\"color:#ffc000\">There are problems with Cleanup! </span>")

    #7
    result_true_rus.append("<span>Обновил вьюпорт. </span>")
    result_true_eng.append("<span>Viewport refreshed. </span>")
    
    result_false_rus.append("<span style=\"color:#ffc000\">Вьюпорт не обновился! </span>")
    result_false_eng.append("<span style=\"color:#ffc000\">Viewport has not been updated! </span>")

    #8
    result_true_rus.append("<span>Вся история была удалена. </span>")
    result_true_eng.append("<span>All construction history was deleted. </span>")
    
    result_false_rus.append("<span style=\"color:#ffc000\">Проблемы с удалением истории! </span>")
    result_false_eng.append("<span style=\"color:#ffc000\">Problems deleting construction history! </span>")
    
    #9
    result_true_rus.append("")
    result_true_eng.append("")
    
    result_false_rus.append("<span style=\"color:#ffc000\">Кстати, рекомендую сохраниться (Ctr+S)! </span>")
    result_false_eng.append("<span style=\"color:#ffc000\">By the way I recommend save the scene (Ctr+S)! </span>")


    #Intro
    if language == "rus":
        conclusion_text.append("<span style=\"color:#8dc63f\">Я подготовил модель для проверки. </span>")
    else:
        conclusion_text.append("<span style=\"color:#8dc63f\">So I prepared the mesh for feedback. </span>")
    
    #Create feedback
    for i in range(len(conclusion_data)):
        
        if language == "rus":
            
            if conclusion_data[i]==True:
                conclusion_text.append(result_true_rus[i])
            else:
                conclusion_text.append(result_false_rus[i])
        
        if language == "eng":
            
            if conclusion_data[i]==True:            
                conclusion_text.append(result_true_eng[i])
            else:
                conclusion_text.append(result_false_eng[i])

    #Outro
    if language == "rus":
        conclusion_text.append("<span>Модель подготовлена. Если что пропустил — сделайте пожалуйста сами. Успехов в работе!</span>") 
    else:
        conclusion_text.append("<span>Mesh prepared. If I forgot something — please do it yourself. Good luck in job!</span>")   

    full_conclusion_text = ''.join(conclusion_text)    
    
    return full_conclusion_text


def prepSceneConclusion(language, conclusion_data):
     
    conclusion_text = []
    
    result_true_rus = []
    result_false_rus = []

    result_true_eng = []
    result_false_eng = []
    
    #0
    result_true_rus.append("<span>Все объекты на сцене были сделаны видимыми. </span>")
    result_true_eng.append("<span>All objects on the scene were made visible. </span>")
    
    result_false_rus.append("<span style=\"color:#ed1c24\">Хмм... Не смог сделать видимыми все объекты на сцене. </span>")
    result_false_eng.append("<span style=\"color:#ed1c24\">Hmm ... I could not make all the objects on the scene visible. </span>")

    #1
    result_true_rus.append("<span>Также, включил видимость всех слоев. </span>")
    result_true_eng.append("<span>Also turn ON the visibility of all layers. </span>")
    
    result_false_rus.append("<span style=\"color:#ed1c24\">Странно, но слои не получилось сделать видимыми. </span>")
    result_false_eng.append("<span style=\"color:#ed1c24\">Strange... but the layers could not be made visible. </span>")

    #2
    result_true_rus.append("<span>На всякий случай обновил вьюпорт. </span>")
    result_true_eng.append("<span>Just in case I updated the viewport. </span>")
    
    result_false_rus.append("<span style=\"color:#ed1c24\">Не обновил вьюпорт. Мелочь, а неприятно... </span>")
    result_false_eng.append("<span style=\"color:#ed1c24\">Did not update the viewport. A trifle but unpleasant... </span>")

    #3
    result_true_rus.append("<span>Удалил все неиспользуемые на сцене материалы. </span>")
    result_true_eng.append("<span>Removed all unused materials on scene. </span>")
    
    result_false_rus.append("<span style=\"color:#ed1c24\">Вам придется удалить все неиспользуемые на сцене материалы самостоятельно... </span>")
    result_false_eng.append("<span style=\"color:#ed1c24\">You will have to delete all unused materials on the stage yourself... </span>")

    #4
    result_true_rus.append("<span>Запускал оптимизацию. </span>")
    result_true_eng.append("<span>Started optimization. </span>")
    
    result_false_rus.append("<span style=\"color:#ed1c24\">Не смог запустить оптимизацию. </span>")
    result_false_eng.append("<span style=\"color:#ed1c24\">Could not start optimization. </span>")

    #5
    result_true_rus.append("<span>В конце — очистил сцену (Cleanup). </span>")
    result_true_eng.append("<span>At the end cleared the scene (Cleanup). </span>")
    
    result_false_rus.append("<span style=\"color:#ed1c24\">Хотел очистить сцену, но что-то пошло не так! </span>")
    result_false_eng.append("<span style=\"color:#ed1c24\">I wanted to clear the scene but something went wrong! </span>")

    #6
    result_true_rus.append("")
    result_true_eng.append("")
    
    result_false_rus.append("<span style=\"color:#ffc000\">Кстати, рекомендую сохраниться (Ctr+S)! </span>")
    result_false_eng.append("<span style=\"color:#ffc000\">By the way I recommend save the scene (Ctr+S)! </span>")

    #Intro
    if language == "rus":
        conclusion_text.append("<span style=\"color:#8dc63f\">Я подготовил эту сцену для проверки. </span>")
    else:
        conclusion_text.append("<span style=\"color:#8dc63f\">So I prepared the scene for feedback. </span>")
    
    #Create feedback
    for i in range(len(conclusion_data)):
        
        if language == "rus":
            
            if conclusion_data[i]==True:
                conclusion_text.append(result_true_rus[i])
            else:
                conclusion_text.append(result_false_rus[i])
        
        if language == "eng":
            
            if conclusion_data[i]==True:            
                conclusion_text.append(result_true_eng[i])
            else:
                conclusion_text.append(result_false_eng[i])

    #Outro
    if language == "rus":
        conclusion_text.append("<span>Вроде все... Если что упустил — сделайте пожалуйста самостоятельно. Успехов в работе!</span>") 
    else:
        conclusion_text.append("<span>Like everything... If I missed something — please do it yourself. Good luck in job!</span>")   
    
    #Union all texts
    full_conclusion_text = ''.join(conclusion_text)    
    
    return full_conclusion_text

def prepViewportConclusion (language, conclusion_data):

    conclusion_text = []
    
    result_true_rus = []
    result_false_rus = []

    result_true_eng = []
    result_false_eng = []
    
    #0
    result_true_rus.append("<span>Снял текущее выделение. </span>")
    result_true_eng.append("<span>Removed the current selection. </span>")
    
    result_false_rus.append("<span style=\"color:#ed1c24\">Проблема со снятием выделения. </span>")
    result_false_eng.append("<span style=\"color:#ed1c24\">Problem with deselecting. </span>")

    #1
    result_true_rus.append("<span>Переключился в стандартный вид (4 панели). </span>")
    result_true_eng.append("<span>Switch to standard view (4 panels). </span>")
    
    result_false_rus.append("<span style=\"color:#ed1c24\">Не получается переключиться на 4 панели. </span>")
    result_false_eng.append("<span style=\"color:#ed1c24\">Сan’t switch to 4 panels. </span>")

    #2
    result_true_rus.append("<span>Настроил клиппинг у камер. </span>")
    result_true_eng.append("<span>Set up cameras clipping. </span>")
    
    result_false_rus.append("<span style=\"color:#ed1c24\">Клиппинг не удалось настроить. </span>")
    result_false_eng.append("<span style=\"color:#ed1c24\">Failed to configure clipping. </span>")

    #3
    result_true_rus.append("<span>Включил отображение статистики во вьюпорте (перспектива). </span>")
    result_true_eng.append("<span>Turn on statistics in the viewport (perspective). </span>")
    
    result_false_rus.append("<span style=\"color:#ed1c24\">Что-то не смог включить статистику в перспективе. </span>")
    result_false_eng.append("<span style=\"color:#ed1c24\">Could not turn on statistics in perspective. </span>")

    #4
    result_true_rus.append("<span>Настроил отображение в панели 1 (шейдинг, освещение, сетку). </span>")
    result_true_eng.append("<span>Set up the display properties in panel 1 (shading, lighting, grid). </span>")
    
    result_false_rus.append("<span style=\"color:#ed1c24\">Ошибка при настройке панели 1. </span>")
    result_false_eng.append("<span style=\"color:#ed1c24\">Error setting panel 1. </span>")

    #5
    result_true_rus.append("<span>Панель 2 — настроена. </span>")
    result_true_eng.append("<span>Panel 2 - configured. </span>")
    
    result_false_rus.append("<span style=\"color:#ed1c24\">Панель 2 не настроена. </span>")
    result_false_eng.append("<span style=\"color:#ed1c24\">Panel 2 is not configured. </span>")

    #6
    result_true_rus.append("<span>Панель 3 - ОК. </span>")
    result_true_eng.append("<span>Panel 3 - OK. </span>")
    
    result_false_rus.append("<span style=\"color:#ffc000\">Панель 3 не настроена. </span>")
    result_false_eng.append("<span style=\"color:#ffc000\">Panel 3 is not configured. </span>")

    #7
    result_true_rus.append("<span>Панель 4 - ОК. </span>")
    result_true_eng.append("<span>Panel 4 - OK. </span>")
    
    result_false_rus.append("<span style=\"color:#ffc000\">Панель 4 не настроена. </span>")
    result_false_eng.append("<span style=\"color:#ffc000\">Panel 4 is not configured. </span>")

    #8
    result_true_rus.append("<span>Отключил режим Isolate для всех вьюпортов. </span>")
    result_true_eng.append("<span>Disable Isolate mode for all viewports. </span>")
    
    result_false_rus.append("<span style=\"color:#ffc000\">Проблемы с отключением режима Isolate. </span>")
    result_false_eng.append("<span style=\"color:#ffc000\">Problems disabling Isolate mode. </span>")

    #9
    result_true_rus.append("<span>Настроил камеру в панели перспектива. </span>")
    result_true_eng.append("<span>I set up the camera in the perspective panel. </span>")
    
    result_false_rus.append("<span style=\"color:#ffc000\">Камера в окне перспективы не настроена. </span>")
    result_false_eng.append("<span style=\"color:#ffc000\">The camera in the perspective window is not configured. </span>")

    #10
    result_true_rus.append("<span>Обновил вьюпорт. </span>")
    result_true_eng.append("<span>Viewport updated. </span>")
    
    result_false_rus.append("<span style=\"color:#ffc000\">Не смог обновить вьюпорт. </span>")
    result_false_eng.append("<span style=\"color:#ffc000\">Could not update viewport. </span>")


    #Intro
    if language == "rus":
        conclusion_text.append("<span style=\"color:#8dc63f\">Я подготовил вьюпорт для проверки. </span>")
    else:
        conclusion_text.append("<span style=\"color:#8dc63f\">So I prepared the viewport for feedback. </span>")
    
    #Create feedback
    for i in range(len(conclusion_data)):
        
        if language == "rus":
            
            if conclusion_data[i]==True:
                conclusion_text.append(result_true_rus[i])
            else:
                conclusion_text.append(result_false_rus[i])
        
        if language == "eng":
            
            if conclusion_data[i]==True:            
                conclusion_text.append(result_true_eng[i])
            else:
                conclusion_text.append(result_false_eng[i])

    #Outro
    if language == "rus":
        conclusion_text.append("<span>На этом — все. Если что забыл — сделайте пожалуйста сами. Успехов в работе!</span>") 
    else:
        conclusion_text.append("<span>It's all... If I forgot something — please do it yourself. Good luck in job!</span>")   
                  

    full_conclusion_text = ''.join(conclusion_text)    
    
    return full_conclusion_text

def statConclusion(language, conclusion_data):
    conclusion_text = []
    
    result_true_rus = []
    result_false_rus = []

    result_true_eng = []
    result_false_eng = []

    #0
    result_true_rus.append("<span>Были выделены только Mesh Shapes. </span>")
    result_true_eng.append("<span>Only Mesh Shapes were selected. </span>")

    result_false_rus.append("<span style=\"color:#ffc000\">В выделении были не только Mesh-shapes и они не были учтены при подсчете. </span>")
    result_false_eng.append("<span style=\"color:#ffc000\">In selection there were not only Mesh Shapes and they were ignored. </span>")    

    #1
    result_true_rus.append("<span></span>")
    result_true_eng.append("<span></span>")

    result_false_rus.append("<span style=\"color:#ec008c\">На UV-развертке есть оверлап. </span>")
    result_false_eng.append("<span style=\"color:#ec008c\">Overlap is present on the UV-layout. </span>")    

    #2 100% overlap
    result_true_rus.append("<span></span>")
    result_true_eng.append("<span></span>")

    result_false_rus.append("<span style=\"color:#ed1c24\">На " + str(conclusion_data[2]) + " oбнаружен 100% оверлап (все элементы uv-развертки лежат друг на друге). Так было задумано? </span>")
    result_false_eng.append("<span style=\"color:#ed1c24\">On " + str(conclusion_data[2]) + " - 100% overlap is present (all UV Shells are on top of each other). It's OK? </span>")

    #3
    result_true_rus.append("<span></span>")
    result_true_eng.append("<span></span>")

    result_false_rus.append("<span style=\"color:#ed1c24\">Обнаружены полигоны с очень маленькой площадью! </span>")
    result_false_eng.append("<span style=\"color:#ed1c24\">Polygons with a very small area was detected! </span>")


    #4 UV Sets
    result_true_rus.append("<span></span>")
    result_true_eng.append("<span></span>")

    result_false_rus.append("<span style=\"color:#ff8fd1\">На некоторых объектах обнаружен больше чем один UV Set! Для простых моделей (без мультитекстурирования) достаточно одного. </span>")
    result_false_eng.append("<span style=\"color:#ff8fd1\">More than one UV Set detected on some objects! For simple models (without multitexturing) one is enough. </span>")


    #5 Mats
    result_true_rus.append("<span></span>")
    result_true_eng.append("<span></span>")

    result_false_rus.append("<span style=\"color:#ed1c24\">На некоторых объектах назначено несколько материалов. Как правило, на игровых моделях на 1 меш назначен 1 материал. </span>")
    result_false_eng.append("<span style=\"color:#ed1c24\">Some objects have several materials assigned. Usually in game models 1 material is assigned to 1 mesh. </span>")


    #6 1-0 UV
    result_true_rus.append("<span></span>")
    result_true_eng.append("<span></span>")

    result_false_rus.append("<span style=\"color:#d68d00\">Отдельные элементы UV-развертки выходят за пределы области [1,0]. Если ваша текстура тайлится, то это ОК. </span>")
    result_false_eng.append("<span style=\"color:#d68d00\">Some UV Shells outside [1, 0] area. If your texture is tiled then this is OK. </span>")


    #7 Util
    result_true_rus.append("<span></span>")
    result_true_eng.append("<span></span>")

    result_false_rus.append("<span style=\"color:#f26522\">Проблемы с UV-разверткой. Если так и было задумано, то ОК. Если нет, то рекомендую ее оптимизировать. Уменьшить процент пустого пространства, проверить паддинг и оверлап. </span>")
    result_false_eng.append("<span style=\"color:#f26522\">Problems with UV-layout. If this was intended then OK. If not I recommend optimizing it! Reducing the percentage of empty space, check padding and overlap! </span>")


    #Intro
    if language == "rus":
        conclusion_text.append("<span style=\"color:#8dc63f\">Комментарии к статистике. </span>")
    else:
        conclusion_text.append("<span style=\"color:#8dc63f\">Comments for statistics. </span>")
    
    #model raiting    
    good_bad_model=[]

    #Create feedback
    for i in range(len(conclusion_data)):
        
        if language == "rus":
            
            if conclusion_data[i]==True:
                conclusion_text.append(result_true_rus[i])
                good_bad_model.append(1)
            else:
                conclusion_text.append(result_false_rus[i])
                good_bad_model.append(0)
        
        if language == "eng":
            
            if conclusion_data[i]==True:            
                conclusion_text.append(result_true_eng[i])
                good_bad_model.append(1)
            else:
                conclusion_text.append(result_false_eng[i])
                good_bad_model.append(0)
                
    
    #model raiting
    if sum(good_bad_model) >= 6:
        if language == "rus":
            conclusion_text.append("<span>Вроде неплохая моделька получилась! </span>") 
        else:
            conclusion_text.append("<span>It seems like a good model! </span>")
    elif sum(good_bad_model) <= 5:                  
        if language == "rus":
            conclusion_text.append("<span>Неплохая модель, но с проблемами. Видимо стоит ее доработать. </span>") 
        else:
            conclusion_text.append("<span>Model with problems. Apparently it is worth fix it. </span>")               

    #Outro
    if language == "rus":
        conclusion_text.append("<span>Более подробную информацию можно обнаружить изучив лог Script Editor. Успехов в работе!</span>") 
    else:
        conclusion_text.append("<span>More information can be found by examining the Script Editor log. Good luck in job!</span>")                  
    
    full_conclusion_text = ''.join(conclusion_text)    
    
    return full_conclusion_text

def dimensionConclusion(language, ObjectHasTransform):
    
    conclusion_text =""
    #Outro
    if language == "rus":
        TransformText = ""

        if ObjectHasTransform == True:
            TransformText = "<br><span style=\"color:#ff0007\">Объекты имеют трансформацию масштабирования отличную от 1! Желательно сделать операцию Freeze Transformations.</span>"

        conclusion_text = ("<span style=\"color:#8dc63f\">Вы включили режим просмотра размеров габаритного контейнера объектов во вьюпорте.</span>" + TransformText  +
        "<br>Посмотрите на длину, ширину и высоту объекта. Все ли в порядке? \
        Например, вы смоделировали автомобиль и видите, что его длина 1 метр, то скорее всего с размерами что-то не так, только если автомобиль не на радиоуправлении... \
        Если размеры не корректные — отмасштабируйте объект. Сделайте Freeze Transformations и снова проверьте размер. Успехов!") 
    else:
        TransformText = ""
        if ObjectHasTransform == True:
            TransformText = "<br><span style=\"color:#ff0007\">Objects have a Scale Transform other than 1! Better to do Freeze Transforms operation.</span>"
        
        conclusion_text = ("<span style=\"color:#8dc63f\">You have turned on the mode for viewing the dimensions of the bounding box of objects in the viewport.</span>" + TransformText  + 
        "<br>Look at the length, width and height of the object. Is everything alright? \
        For example you modeled a car and you see that its length is 1 meter. Then most likely something is wrong with the dimensions only if the car is not radio-controlled ... \
        If the sizes are not correct — scale the object. Make Freeze Transformations and check the size again. Good luck!") 
    
    return conclusion_text

#lang, texel value and seletion type (random or not)
def calcTexelConclusion(language, texelValue, selOrRandom):
    
    conclusion_text = ""
    
    if (language == "rus"):
        
        if selOrRandom == True:
            selectType = "Тексель измерен для выбранного вручную полигона. "
        else:
            selectType = "Тексель измерен для случайно выбранного полигона. "    
        
        if texelValue <= 49:
            conclusion_text = selectType + "<span style=\"color:#ffc000\">Значение текселя ОЧЕНЬ низкое (меньше 1пикс на 1см).</span> \
            Это может значить, что текстура без деталей (заливка сплошным цветом) или объект находиться очень далеко от игровой камеры (почти не видим игроком). <br>\
            Помните, что тексель зависит от размера текстуры и площади UV-развертки!"
        if texelValue in range(49, 201):
            conclusion_text = selectType + "<span style=\"color:#00bff3\">Значение текселя достаточно низкое (1-2пикс на 1см).</span> Возможно:\
            вы делаете текстуру для мобильной игры, это какой-то второстепенный объект на заднем плане или малозаметная для игрока часть модели.<br>\
            Помните, что тексель зависит от размера текстуры и площади UV-развертки!"
        elif texelValue in range(200, 351):
            conclusion_text = selectType + "<span style=\"color:#8dc63f\">Значение текселя — среднее.</span> Текстура будет предназначена или для мобильной игры или для ПК, но\
             будет находиться на некотором отдалении от игровой камеры. Возможно, это малозаметная деталь для современной ПК-игры. <br>\
             Помните, что тексель зависит от размера текстуры и площади UV-развертки!"
        elif texelValue in range(350, 601):
            conclusion_text = selectType + "<span style=\"color:#8dc63f\">Значение текселя — высокое.</span> Скорее всего вы делаете высококачественную игру\
             для ПК или эта деталь близко к игровой камере. <br>Помните, что тексель зависит от размера текстуры и площади UV-развертки!"
        elif texelValue in range(600, 8192):
            conclusion_text = selectType + "<span style=\"color:#8dc63f\">Значение текселя — ОЧЕНЬ высокое.</span> Это будет текстура для NextGen-игры для 4К-мониторов или модель\
             будет находиться очень близко к игровой камере. <br>Помните, что тексель зависит от размера текстуры и площади UV-развертки!"
        elif texelValue > 8192:
            conclusion_text = selectType + "<span style=\"color:#8dc63f\">Значение текселя не реально высокое.</span> Так не бывает! Это модель для компьютерной игры?"

    
    if language == "eng":

        if selOrRandom == True:
            selectType = "The texel is measured for a manually selected polygon. "
        else:
            selectType = "The texel is measured for a randomly selected polygon. "    
        
        if texelValue <= 49:
            conclusion_text = selectType + "<span style=\"color:#ffc000\"> The texel value is VERY low (less than 1px per 1cm).</span> \
            It could mean: this is a texture without details (solid fill) or located very far from the game camera (almost invisible to the player).\
            Remember that texel depends on the size of the texture and the area of the UV-layout!"
        if texelValue in range(49, 201):
            conclusion_text = selectType + "<span style=\"color:#00bff3\"> The texel value is quite low (1-2pix per 1cm).</span> Maybe: \
            you are making a texture for a mobile game, is it some secondary object in the background or a part of the model that is invisible to the player.\
            Remember that texel depends on the size of the texture and the area of the UV-layout!"
        elif texelValue in range(200, 351):
            conclusion_text = selectType + "<span style=\"color:#8dc63f\"> The texel value is medium.</span> A model for either a mobile game or a PC but \
             will be located at some distance from the game camera. Perhaps this is an inconspicuous detail for a modern PC game.\
             Remember that texel depends on the size of the texture and the area of the UV-layout!"
        elif texelValue in range(350, 601):
            conclusion_text = selectType + "<span style=\"color:#8dc63f\"> The texel value is high.</span> Most likely you are making a high-quality PC game \
            or this part is close to the game camera. Remember that texel depends on the size of the texture and the area of the UV-layout!"
        elif texelValue in range(601, 8192):
            conclusion_text = selectType + "<span style=\"color:#8dc63f\"> The texel value is VERY high.</span> Is this a NextGen game for 4K monitors or the model\
             will be very close to the game camera. Remember that texel depends on the size of the texture and the area of the UV-layout!"
        elif texelValue > 8192:
            conclusion_text = selectType + "<span style=\"color:#8dc63f\">The texel value is unrealistically high.</span> It's impossible'! Is this a model for PC game?"

    return conclusion_text


#lang, texel value and seletion type (random or not)
def setTexelConclusion(language, texelValue, shapesOutside, ObjectsNumber):
    
    conclusion_text = ""
    
    if (language == "rus"):
        
        if shapesOutside == True:
            outsideData = "<span style=\"color:#8dc63f\">На текущий момент все элементы UV-развертки в пределах площади [0, 1].</span> "
        else:
            outsideData = "<span style=\"color:#ffc000\">На текущий момент некоторые элементы UV-развертки выходят за пределы площади [0, 1]. Смотрите лог.</span> "    

        ObjectsNumberText = "Обработано объектов: " + str(ObjectsNumber)
                
        if texelValue <= 49:
            conclusion_text =  ObjectsNumberText + "<span style=\"color:#ffc000\"> Было задано ОЧЕНЬ низкое значение текселя (меньше 1пикс на 1см).</span> \
            Это будет текстура без деталей (заливка сплошным цветом) или объект, на котором она будет назначена, находиться очень далеко от игровой камеры (почти не видим игроком).\
            Помните, что увеличение текселя происходит за счет увеличения площади UV-развертки. Если текстура не предполагает тайл, то после операции увеличения убедитесь, \
            что UV-развертка не вышла за пределы площади [1,0]. " + outsideData
        if texelValue in range(50, 201):
            conclusion_text = ObjectsNumberText + "<span style=\"color:#00bff3\"> Было установлено достаточно низкое значение текселя (1-2пикс на 1см).</span> Возможно:\
            вы делаете текстуру для мобильной игры, это какой-то второстепенный объект на заднем плане или малозаметная для игрока часть модели.\
            Помните, что увеличение текселя происходит за счет увеличения площади UV-развертки. Если текстура не предполагает тайл, то после операции увеличения убедитесь, \
            что UV-развертка не вышла за пределы площади [1,0]. " + outsideData
        elif texelValue in range(201, 351):
            conclusion_text = ObjectsNumberText + "<span style=\"color:#8dc63f\"> Заданное значение текселя — среднее.</span> Текстура и модель или для мобильной игры, или для ПК, но\
             будет находиться на некотором отдалении от игровой камеры. Возможно, это малозаметная деталь для современной ПК-игры.\
             Помните, что увеличение текселя происходит за счет увеличения площади UV-развертки. Если текстура не предполагает тайл, то после операции увеличения убедитесь, \
            что UV-развертка не вышла за пределы площади [1,0]. " + outsideData
        elif texelValue in range(351, 601):
            conclusion_text = ObjectsNumberText + "<span style=\"color:#8dc63f\"> Установленное значение текселя — высокое.</span> Скорее всего вы делаете высококачественную игру\
             для ПК или эта деталь модели близко к игровой камере. Помните, что увеличение текселя происходит за счет увеличения площади UV-развертки.\
             Если текстура не предполагает тайл, то после операции увеличения убедитесь, что UV-развертка не вышла за пределы площади [1,0]. " + outsideData
        elif texelValue in range(601, 10000):
            conclusion_text = ObjectsNumberText + "<span style=\"color:#8dc63f\"> Было задано ОЧЕНЬ высокое значение текселя.</span> Это NextGen-игра для 4К-мониторов или модель\
             будет находиться очень близко к игровой камере. Помните, что увеличение текселя происходит за счет увеличения площади UV-развертки.\
             Если текстура не предполагает тайл, то после операции увеличения убедитесь, что UV-развертка не вышла за пределы площади [1,0]. " + outsideData
    
    if language == "eng":
        
        if shapesOutside == True:
            outsideData = "<span style=\"color:#8dc63f\">Currently all the elements of UV Shells within the area [0, 1].</span> "
        else:
            outsideData = "<span style=\"color:#ffc000\">Currently some UV Shells elements are outside the area [0, 1]. See the log.</span> "    

        ObjectsNumberText = "Objects processed: " + str(ObjectsNumber)
                
        if texelValue <= 49:
            conclusion_text =  ObjectsNumberText + "<span style=\"color:#ffc000\"> A VERY low texel value was set (less than 1px per 1cm).</span> \
            This will be a texture without details (solid color fill) or the object on which it will be assigned to be very far from the game camera (almost not visible to the player).\
            Remember that an increase in texel occurs due to an increase in the UV-layout area. If the texture does not imply a tile then after the enlargement operation make sure \
            that the UV layout did not extend beyond the area [1,0]. " + outsideData
        if texelValue in range(50, 201):
            conclusion_text = ObjectsNumberText + "<span style=\"color:#00bff3\"> A fairly low texel value was set (1-2px per 1cm).</span> Maybe:\
            you make a texture for a mobile game, or it is secondary object in the background or a part of the model that is invisible to the player. \
            Remember that an increase in texel occurs due to an increase in the UV-layout area. If the texture does not imply a tile then after the enlargement operation make sure \
            that the UV layout did not extend beyond the area [1,0]. " + outsideData
        elif texelValue in range(201, 351):
            conclusion_text = ObjectsNumberText + "<span style=\"color:#8dc63f\"> The texel value is average.</span> The texture and model are either for a mobile game or for a PC but \
            will be located at some distance from the game camera. Perhaps this is an inconspicuous detail for a modern PC game. \
            Remember that an increase in texel occurs due to an increase in the UV-layout area. If the texture does not imply a tile then after the enlargement operation make sure \
            that the UV layout did not extend beyond the area [1,0]. " + outsideData
        elif texelValue in range(351, 601):
            conclusion_text = ObjectsNumberText + "<span style=\"color:#8dc63f\"> The texel value is high.</span> Most likely you are making a high-quality PC game \
             or this part is close to the game camera. Remember that an increase in texel occurs due to an increase in the UV-layout area. If the texture does not imply a tile then after the enlargement operation make sure \
            that the UV layout did not extend beyond the area [1,0]. " + outsideData
        elif texelValue in range(601, 10000):
            conclusion_text = ObjectsNumberText + "<span style=\"color:#8dc63f\"> The texel value is VERY high.</span> Is this a NextGen game for 4K monitors or the model \
            will be very close to the game camera. Remember that an increase in texel occurs due to an increase in the UV-layout area. If the texture does not imply a tile then after the enlargement operation make sure \
            that the UV layout did not extend beyond the area [1,0]. " + outsideData
    

    return conclusion_text


def checkTexelConclusion (language, DifferenceMargin, correct, streched, compressed, TinyUV, TinyFace):
    

    if (language == "rus"):
        
        if TinyUV == True:
            TinyUVConclusion = " На UV-развертке присутствуют UV Shells с очень маленькой площадью. "
        else:
            TinyUVConclusion = ""

        if TinyFace == True:
            TinyFaceConclusion = " В модели есть полигоны с очень маленькой площадью. "
        else:
            TinyFaceConclusion = ""

        
        if sum(correct) > 0:
            CorrectConclusion = " <span style=\"color:#80ff80\">Количество полигонов в заданном диапазоне: " + str(sum(correct)) + " шт. </span>"
        else:
            CorrectConclusion = "<span style=\"color:#80ff80\"> Полигонов с заданным текселем не обнаружено.</span> "

        if sum(streched) > 0:
            StrechedtConclusion = " <span style=\"color:#ffc0c0\">Есть полигоны с повышенным текселем " + str(sum(streched)) + " шт. Это значит, что тексель у них выше заданного более чем на 10%. \
            Если так и планировалось, то хорошо, а иначе необходимо отмасштабировать их UV-развертку в меньшую сторону. </span>"
        else:
            StrechedtConclusion = "<span style=\"color:#ffc0c0\"> Полигонов с повышенным текселем не обнаружено.</span> "

        if sum(compressed) > 0:
            CompressedConclusion = " <span style=\"color:#80c0ff\">Еще были найдены полигоны с пониженным текселем — " + str(sum(compressed)) + " шт. Их тексель ниже заданного диапазона, если это не было запланировано, \
            то необходимо увеличить площадь UV-развертки этих полигонов. </span>"
        else:
            CompressedConclusion = "<span style=\"color:#80c0ff\"> Полигонов с пониженным текселем не обнаружено.</span> "

        conclusion_text = "Была произведена проверка и сравнение полигонов всех выделенных объектов с заданным текселем в диапазоне +/-" + str(DifferenceMargin) + "%" + \
        CorrectConclusion + StrechedtConclusion + CompressedConclusion + TinyUVConclusion + TinyFaceConclusion + " После правок не забывайте проверить тексель. Успехов!" 
    
    if language == "eng":
        
        if TinyUV == True:
            TinyUVConclusion = " The UV layout has UV shells with a very small area. "
        else:
            TinyUVConclusion = ""

        if TinyFace == True:
            TinyFaceConclusion = " The model has polygons with a very small area. "
        else:
            TinyFaceConclusion = ""        

        if sum(correct) > 0:
            CorrectConclusion = " <span style=\"color:#80ff80\">The number of polygons in a given range: " + str(sum(correct)) + " pcs. </span>"
        else:
            CorrectConclusion = "<span style=\"color:#80ff80\">Ppolygons with a specified texel no found.</span> "

        if sum(streched) > 0:
            StrechedtConclusion = " <span style=\"color:#ffc0c0\">There are polygons with elevated texel " + str(sum(streched)) + " pcs. This means that their texel is above the target by more than 10%. \
            If this was planned — then it is good! Otherwise it is necessary to scale down their UV-layout. </span>"
        else:
            StrechedtConclusion = "<span style=\"color:#ffc0c0\">No polygons with elevated texel were found.</span> "

        if sum(compressed) > 0:
            CompressedConclusion = " <span style=\"color:#80c0ff\">Low texel polygons were found — " + str(sum(compressed)) + " pcs. Their texel is below the specified range, \
            If this was not planned — then it is necessary to increase the UV-layout area of these polygons. </span>"
        else:
            CompressedConclusion = "<span style=\"color:#80c0ff\">No low texel polygons were found.</span> "

        conclusion_text = "The polygons of all selected objects (with the specified texel) in the range +/-" + str(DifferenceMargin) + "% were checked and compared. " + \
        CorrectConclusion + StrechedtConclusion + CompressedConclusion + TinyUVConclusion + TinyFaceConclusion + " After fixing do not forget to check the texel. Good luck!" 

    
    return conclusion_text    

def CleanCheckClicked (language, CleanOrNot):
    
    if (language == "rus"):
        
        if CleanOrNot == True:
            conclusion_text = "Окраска полигонов после проверки текселя была очищена. Успехов в работе!"
        else:
            conclusion_text = "Нечего очищать! Очистку можно произвести только после проверки текселя, когда полигоны будут окрашены."
        
    if language == "eng":
        if CleanOrNot == True:
            conclusion_text = "The color of the polygons after checking the texel was cleaned. Good luck!"
        else:
            conclusion_text = "Nothing to clean! Cleaning can only be done after checking the texel when the polygons are painted."
        
    return conclusion_text 


def selectTinyConclusion (language, tinyType, Result):
    
    if (language == "rus"):
        
        CantSelectReasons = "<br>— модели нет в сцене (была открыта новая сцена) <br>— после проверки модель была удалена <br>— после проверки модель была переименована \
        <br>— после проверки модель была модифицирована<br>Попробуйте сделать проверку еще раз учитывая информацию описанную выше. Успехов в работе!"
        
        if tinyType == "UV" and Result == True:
            conclusion_text = "<span style=\"color:#ffc000\">Выделены элементы UV-развертки с очень маленькой площадью.</span> Значение площади задается в пикселях, в поле Tiny UV Shells. \
            Если на UV-развертке у какой-то детали очень маленькая площадь, то вы не сможете там нарисовать хорошую текстуру. Например, \
            размер элемента 1х1 пиксель. Что вы там сможете изобразить? Ничего! Можно закрасить его сплошным цветом и все. Чтобы что-то нарисовать, \
            необходима площадь хотя бы 3х3 пикселя. А если это не диффузная текстура, а normal-map? Конечно, всякое быывает при текстуринге, но для \
            большинства случаев микро-uv-shell это не очень хорошо."
        elif tinyType == "UV" and Result == False:
            conclusion_text = "<span style=\"color:#ffc000\">Невозможно выделить элементы UV-развертки с очень маленькой площадью.</span> Возмоэжные причины:" + CantSelectReasons
            
        if tinyType == "Face" and Result == True:
            conclusion_text = "<span style=\"color:#ffc000\">Выделены полигоны с очень маленькой площадью.</span> Значение площади задается в метрах квадратных, в поле Tiny Polygons. \
            Если на модели у какой-то детали очень маленькая площадь, то скорее всего она будет не видна. Например, размер элемента 1х1х1мм. \
            Что это за микро-деталь? Кто ее увидит и с какого расстояния? Может быть ее лучше нарисовать на текстуре? Конечно, всякое бывает в этом мире, но как правило, детали \
            размер которых меньше 3см лучше реализовать на текстуре (использовать нормал, если он есть). Кстати, у микро-деталей может быть микро-UV-развертка, что также может \
            быть проблемой."
        elif tinyType == "Face" and Result == False:
            conclusion_text = "<span style=\"color:#ffc000\">Невозможно выделить полигоны с очень маленькой площадью.</span> Возможные причины:" + CantSelectReasons

    if language == "eng":        

        CantSelectReasons = "<br>the model is not in the scene (a new scene was opened) <br>— after the check the model was deleted <br>— after the check the model was renamed \
        <br>— after checking the model has been modified<br>Try to check again taking into account the information described above. Good luck!"
        
        if tinyType == "UV" and Result == True:
            conclusion_text = "<span style=\"color:#ffc000\">Highlighted UV elements with a very small area.</span> The area value is set in pixels in the Tiny UV Shells field. \
            If a part has a very small area on a UV layout then you cannot draw a good texture there. For example, \
            element size 1x1 pixel. What can you portray there? Nothing! You can fill it with solid color and that’s it. To draw something, \
            An area of at least 3x3 pixels is required. And if it's not a diffuse texture? Normal-map? Of course anything happens when texturing but for \
            In most cases, micro-uv-shell is not very good."
        elif tinyType == "UV" and Result == False:
            conclusion_text = "<span style=\"color:#ffc000\">Cant select UV elements with a very small area.</span> Possible reasons:" + CantSelectReasons
        
        if tinyType == "Face" and Result == True:
            conclusion_text = "<span style=\"color:#ffc000\">Faces with a very small area are highlighted.</span> The value of the area is set in square meters in the Tiny Polygons field. \
            If some part has a very small area on the model then most likely it will not be visible. For example, the size of an element is 1x1x1mm. \
            What is this micro element? Who will see her and from what distance? Maybe it's better to draw on the texture? Of course, everything happens in this 3D-world but as a rule the details \
            the size of which is less than 3 cm is better to implement on the texture (use the normal map if its possible). By the way micro-parts can have a micro-UV scan which can also \
            to be a problem."
        elif tinyType == "Face" and Result == False:
            conclusion_text = "<span style=\"color:#ffc000\">Cant select Faces with a very small area.</span> Possible reasons:" + CantSelectReasons
        
    return conclusion_text

def uvOperationConclusion (language, Action):    

    CheckerName = ""
    AdditionalDescription = ""

    if (language == "rus"):
        if Action == "assign_std_checker":
            CheckerName = "Вы назначили <span style=\"color:#8dc63f\">стандартный чекер</span> на выделенные объекты. "
            AdditionalDescription = "<br>Он помогает увидеть искажения на UV-развертке. Можно заметить и отражение, но лучше для этого использовать цифровой чекер (Digital). Используется часто."
        if Action == "assign_dig_checker":
            CheckerName = "Вы назначили <span style=\"color:#8dc63f\">цифровой чекер</span> на выделенные объекты. "
            AdditionalDescription = "<br>Он помогает увидеть искажения на UV-развертке и позволяет легко понять отражена текстура или нет. Это важно, когда на текстуре планируются текстовые надписи. \
                Вы сразу увидите, что цифры отражены. Используется часто."
        if Action == "assign_diag_checker":
            CheckerName= "Вы назначили <span style=\"color:#8dc63f\">диагональный чекер</span> на выделенные объекты. "
            AdditionalDescription = "<br>Он помогает увидеть направление и стыковку UV-развертки на разных элементах. Это важно видеть, если вы будете создавать текстуры камуфляжа для объекта. \
                Используется не часто — в специфических случаях."
        if Action == "assign_grad_checker":
            CheckerName = "Вы назначили <span style=\"color:#8dc63f\">градиентный чекер</span> на выделенные объекты. "
            AdditionalDescription = "<br>Он помогает увидеть распределение развертки на всей UV-площади. Позволяет приблизительно понять, где находяться различные элементы UV-развертки, есть ли логическая группировка \
                элементов модели. Используется редко. Не тайлится."        
        if Action == "delete_checker":
            CheckerName = "Вы удалили <span style=\"color:#8dc63f\">все pt-шейдера с чекерами</span> созданными ранее. "
            AdditionalDescription = "В некоторых случаях PolygonTools может вернуть предыдущий шейдер назначенный на объект, но не всегда... "
        if Action == "assign_uv":
            CheckerName = "Вы назначили <span style=\"color:#8dc63f\">снимок UV-развертки как текстуру</span> на выделенные объекты. "
            AdditionalDescription = "Вы можете увидеть есть ли хоть какая-то развертка на объекте, а также наличие overlap UV-элементов на развертке. "

        ConclusionText = CheckerName + AdditionalDescription + " Изменения, эмулирующие изменения разрешения чекера, влияют на все чекер-шейдеры в сцене (кроме градиентного). <br>Успехов в работе!"

    if language == "eng": 

        if Action == "assign_std_checker":
            CheckerName = "You assing <span style=\"color:#8dc63f\">standard checker</span> on selected objects. "
            AdditionalDescription = "<br>It helps to see the distortion in the UV-layout. You can see texture fliping but it is better to use a digital checker (Digital). Used frequently."
        if Action == "assign_dig_checker":
            CheckerName = "You assing <span style=\"color:#8dc63f\">digital checker</span> on selected objects. "
            AdditionalDescription = "<br>It helps to see the distortion in the UV-layout and makes it easy to see if the texture is fliped or not. This is important when text labels are planned on the texture. \
                You will immediately see that the numbers are flipped. Used frequently."
        if Action == "assign_diag_checker":
            CheckerName= "You assing <span style=\"color:#8dc63f\">diagonal checker</span> on selected objects. "
            AdditionalDescription = "<br>It helps to see the direction and connecting of the UV-layout on different elements. This is important to see if you will be creating camouflage textures for the model. \
                It is not used often - in specific cases."
        if Action == "assign_grad_checker":
            CheckerName = "You assing <span style=\"color:#8dc63f\">gradient checker</span> on selected objects. "
            AdditionalDescription = "<br>It helps to see the distribution of the sweep over the entire UV area. Allows you to approximately understand where the various UV elements are located is there a logical grouping \
                elements of model. Used rarely. Do not tile."        
        if Action == "delete_checker":
            CheckerName = "You deleted <span style=\"color:#8dc63f\">all pt-shaders with checkers</span> created earlier. "
            AdditionalDescription = "In some cases PolygonTools may return the previous shader assigned to the object, but not always... "
        if Action == "assign_uv":
            CheckerName = "You assing <span style=\"color:#8dc63f\">UV Snapshot as texture</span> on selected objects. "
            AdditionalDescription = "You can see UV layout on the object and overlaped UV elements on the UV-layout."        

        ConclusionText = CheckerName + AdditionalDescription + " Changes that emulate changes in checker resolution affect all pt-checker shaders in the scene (except gradient). <br> Success in work!"

    return ConclusionText

def toolOperationConclusion (language, Action):

    ConclusionText = "If you see this text - something went wrong..."

    if (language == "rus"):

        if Action == "DelMat":
            ConclusionText = "Вы полностью удалили материалы с выделенных объектов и они должны стать яркого зеленого цвета. Иногда такое бывает нужно, что бы вообще ничего не было назначено."

        if Action == "GlossMat":
            ConclusionText = "Вы назначили на выделенные объекты блестящий (gloss) материал. Когда объект бликует на нем проще заметить артефакты при проверке."

        if Action == "MateMat":
            ConclusionText = "Вы назначили на выделенные объекты матовый (mate) материал. С таким материалом проще всего проверять модели. Не утомляет глаза."

        if Action == "FBXExpProblem":
            ConclusionText = "Вы хотите экспортировать выделенные объекты в формат FBX (*.fbx).\
                <br>Перед экспортом необходимо сохранить сцену с моделью, т.к. экспорт осуществляется в папку с файлом Maya (*.mb).\
                    <br>Сохраните сцену и попробуйте еще раз."

        if Action == "FBXExp":
            ConclusionText = "Вы экспортировали выделенные объекты в формат FBX (*.fbx). Экспорт происходит с самой простой конфигурацией. \
                Экспортируется только геометрия, нормали и материалы. Камеры, свет и прочее — игнорируются."

        if Action == "LOD":
            ConclusionText = "Вы хотите проверить ЛОДы. Как это сделать? Была создана структура LOD_Group_PT с 5-ю группами для ЛОДов (LOD_0, LOD_1 и т.д.)\
                Ваша задача — поместить в эти группы геометрию ваших ЛОДов. Просто перетащите ваши модели (Drag&Drop) в Outliner в соответсвующие папки.\
                    Проверьте или измените значения дистанции переключения ЛОДов в полях Switch range. Теперь вы можете отдалять камеру удобным вам способом и смотерть на переключение ЛОДов.\
                        Дистанция до LOD0 отображается во вьюпорте и на панели. Поле с текущим ЛОДом подсвечено зеленым цветом (кроме LOD0, т.к. это ваша исходная модель).\
                            Если вы не хотите отдалять модель при проверке, то приблизьтесь до LOD0 и двигайте ползунок Virtual Distance. ЛОДы будут переключаться, а модель будет близко.\
                                Проверив ЛОДЫ — отожмите кнопку LOD. Стурктура LOD_Group_PT будет удалена. Остануться только ваши модели. Успехов в работе!"

        if Action == "RenderPreviewProblem":
            ConclusionText = "Вы хотите отрендерить превью объектов на сцене.\
                <br>Перед этим необходимо сохранить сцену с моделью, т.к. сохранение будет осуществляется в папку с файлом Maya (*.mb).\
                    <br>Сохраните сцену и попробуйте еще раз."

        if Action == "RenderPreview":
            ConclusionText = "Вы сделали превью объектов на сцене. Оно было сохранено в JPG-файл в папку с файлом Maya. Для чего необходимо превью? \
                Превью можно отправить вместе с файлом на проверку. Это позволяет проверяющему лучше понять, что находится в Maya-файле не открывая его. \
                    Иногда (хоть и редко) бывает достаточно увидеть превью и отправить модель на переделку."

        if Action == "CheckIntersect":
            ConclusionText = "Вы хотите проверить пересечение элементов составляющих один меш. Для этого, вокруг всех откртых граней моедли была создана вспомогательная геометрия с толщиной \
                заданной в поле Depth (необходимая глубина погружения). Эта геометрия окрашена красным цветом. Почему вокруг открытых граней? Потому что, если один объект пересекает другой, мы не видим погруженную \
                    геометрию (полигоны на торцах) и можем смело их удалить. Таким образом получаются открытые грани. Если вы видите красную обводку — то скорее всего погружение недостаточно глубокое, \
                        или его вобще нет. Это не очень хорошо и в большинстве случаев требует исправления. \
                            <br>При отжатии кноки — вспомогательная красная геометрия будет удалена."

        if Action == "Retop":
            ConclusionText = "Функция осуществляет простейшую ретопологию модели. Не ждите чуда! Количество полигонов будет изменено примерно до значения заданного в поле Target Face Count.\
                Минимальное значение - 10.0, а максимальное - 100.000. Иногда операция ретопологии занимает значительное время и может казаться, что все зависло. Необходимо немного подождать..."


    if language == "eng": 
        
        if Action == "DelMat":
            ConclusionText = "You have completely removed materials from selected objects and they should turn bright green. Sometimes this is necessary so that nothing is assigned."

        if Action == "GlossMat":
            ConclusionText = "You have assigned glossy material to the selected objects. When object is glossy —  it is easier to see artifacts when checking."

        if Action == "MateMat":
            ConclusionText = "You assigned mate material to the selected objects. With such material it is easiest to check models. Does not tire your eyes."

        if Action == "FBXExpProblem":
            ConclusionText = "You want to export the selected objects to the FBX format (*.fbx).\
                <br> Before exporting you must save the model as export is performed to the folder with the Maya file (*.mb).\
                    <br>Save the scene and try again."

        if Action == "FBXExp":
            ConclusionText = "You exported the selected objects to the FBX format (*.fbx). Export happens with the simplest configuration. \
                Only geometry, normals, and materials are exported. Cameras, lights, etc. are ignored."

        if Action == "LOD":
            ConclusionText = "You want to check LODs. How to do it? The LOD_Group_PT structure was created with 5 groups for LODs (LOD_0, LOD_1, etc.).\
               Your task is to place the geometry of your LODs in these groups. Just drag and drop your models into Outliner into the appropriate folders.\
                    Check or change the LOD switching distance in the Switch range fields. Now you can move the camera and watch for switching LODs.\
                        The distance to LOD0 is displayed in the viewport and on the panel. The field with the current LOD is highlighted in green (except for LOD0, because this is your original model).\
                            If you do not want to move the model away while checking, then approach LOD0 and move the Virtual Distance slider. LODs will switch and the model will be close.\
                                After checking the LODs - press the LOD button again. The LOD_Group_PT structure will be deleted. Only your models will stay. Good luck in job!"

        if Action == "RenderPreviewProblem":
            ConclusionText = "You want to render previews of objects on the scene.\
                <br>Before that, it is necessary to save the scene with the model, as saving will be carried out in the folder with the Maya file (*.mb).\
                    <br>Save the scene and try again."

        if Action == "RenderPreview":
            ConclusionText = "You did a preview of the objects on stage. It was saved in a jpg file in the folder with the Maya file. Why do you need a preview?  \
                The preview can be sent along with the file for feedback. This allows the reviewer to better understand what is in the Maya file without opening it. \
                    Sometimes (though rarely) it is enough to see the preview and send the model to re-work."

        if Action == "CheckIntersect":
            ConclusionText = "You want to check the intersection of the elements of the one mesh. To do this auxiliary geometry was created around all open edges of the model with the thickness \
                specified in the Depth field (required intersection depth). This geometry is colored red. Why around open faces? Because if one object intersects another we don’t see the immersed geometry \
                    (polygons at the ends) and we can safely remove them. Thus open faces are obtained. If you see a red stroke, then most likely the dive is not deep enough \
                        or it just doesn’t exist.  This is not very good and in most cases needs to be fixed. \
                            <br>When pressing the buttons again - auxiliary red geometry will be deleted."

        if Action == "Retop":
            ConclusionText = "The function provides the simplest retopology of the model. Do not wait for a miracle! The number of polygons will be changed to approximately the value specified in the Target Face Count field.\
                The minimum value is 10.0 and the maximum is 100.000. Sometimes a retopology operation takes a considerable amount of time and it may seem like everything is freezed. You need to wait a bit..."


    return ConclusionText


def checkResult(language, CheckResultData):
        
    try:
        Result = sum(CheckResultData)
    except:
        Result = 0

    ConclusionText = ""
    ConclusionItems = ""

    if language == "rus":

        if CheckResultData[0] == False:
            ConclusionItems = "единицами измерения"

        if CheckResultData[1] == False:
            ConclusionItems = ConclusionItems + ", именованием"

        if CheckResultData[2] == False:
            ConclusionItems = ConclusionItems + ", положением Pivot Point относительно центра координат"

        if CheckResultData[3] == False:
            ConclusionItems = ConclusionItems + ", положением Pivot Point относительно габаритного контейнера объекта"

        if CheckResultData[4] == False:
            ConclusionItems = ConclusionItems + ", спрятанными объектами и слоями"

        if CheckResultData[5] == False:
            ConclusionItems = ConclusionItems + ", отображением Back Face'ов"

        if CheckResultData[6] == False:
            ConclusionItems = ConclusionItems + ", трансформациями"

        if CheckResultData[7] == False:
            ConclusionItems = ConclusionItems + ", ошибками в геометрии"

        if CheckResultData[8] == False:
            ConclusionItems = ConclusionItems + ", назначенными материалами"

        if CheckResultData[9] == False:
            ConclusionItems = ConclusionItems + ", положением UV-развертки"

        if CheckResultData[10] == False:
            ConclusionItems = ConclusionItems + ", количеством UV-сетов"

        if CheckResultData[11] == False:
            ConclusionItems = ConclusionItems + ", качеством UV-развертки"

        StandardRecomend = ". Хорошо бы проверить модель в ручном режиме. Попробуйте исправить ошибки с помощью чекера, \
                если напротив пункта активна кнопка Fix. Особое внимание обратите на пункты красного цвета. Однако помните, что чекер не может решить все проблемы, особенно сложные."

        if Result == 11:
            ConclusionText = "<span style=\"color:#8dc63f\">Чекер не обнаружил ни одной проблемы.</span> Скорее всего, это хорошая и аккуратная модель. Однако помните, чекер находит простейшие (детские) ошибки. \
                Ничто не может заменить тщательной проверки в ручном режиме. Успехов в работе!"
        elif (Result < 11) and (Result >= 9):
            ConclusionText = "<span style=\"color:#ffc000\">Хорошая модель.</span> Выявлены проблемы с " + ConclusionItems + StandardRecomend
        elif (Result < 9) and (Result >= 6):
            ConclusionText = "<span style=\"color:#ffc000\">Неплохая модель.</span> Выявлены проблемы с " + ConclusionItems + StandardRecomend
        elif (Result < 6) and (Result >= 3):
            ConclusionText = "<span style=\"color:#ff5001\">Проблемная модель.</span> Необходимо разобраться с " + ConclusionItems + StandardRecomend
        elif Result <= 2 and Result > 0:
            ConclusionText = "<span style=\"color:#ff5001\">Обнаружено множество проблем.</span> Видимо эта модель вообще не проверялась. Необходимо исправить все ошибки и проверить ее чекером еще раз." 
        elif Result == 0:
            ConclusionText = "<span style=\"color:#ff5001\">Сбой при проверке.</span> Смотрите лог Script Edtior Maya. Возможно там есть ответ..." 

    if (language == "eng"):
        if CheckResultData[0] == False:
            ConclusionItems = "system units"

        if CheckResultData[1] == False:
            ConclusionItems = ConclusionItems + ", naming"

        if CheckResultData[2] == False:
            ConclusionItems = ConclusionItems + ", Pivot Point position relative to the center of coordinates"

        if CheckResultData[3] == False:
            ConclusionItems = ConclusionItems + ", Pivot Point position relative to the objects boundig box"

        if CheckResultData[4] == False:
            ConclusionItems = ConclusionItems + ", hidden objects and layers"

        if CheckResultData[5] == False:
            ConclusionItems = ConclusionItems + ", Backface Culling"

        if CheckResultData[6] == False:
            ConclusionItems = ConclusionItems + ", transformations"

        if CheckResultData[7] == False:
            ConclusionItems = ConclusionItems + ", geometry problems"

        if CheckResultData[8] == False:
            ConclusionItems = ConclusionItems + ", assigned materials"

        if CheckResultData[9] == False:
            ConclusionItems = ConclusionItems + ", UV-layout position"

        if CheckResultData[10] == False:
            ConclusionItems = ConclusionItems + ", UV sets count"

        if CheckResultData[11] == False:
            ConclusionItems = ConclusionItems + ", UV-layout quality"

        StandardRecomend = ". It would be nice to check the model in manual mode. Try to fix errors with the checker \
                if the Fix button is active opposite the item. Pay particular attention to items in red. However remember that a checker cannot solve all problems especially complex ones."

        if Result == 11:
            ConclusionText = "<span style=\"color:#8dc63f\">The checker did not find any problems.</span> Most likely, this is a good and neat model. However remember that the checker finds the simplest errors. \
                Nothing can replace a thorough manual check. Good luck in job!"
        elif (Result < 11) and (Result >= 9):
            ConclusionText = "<span style=\"color:#ffc000\">Good model.</span> Found problems with " + ConclusionItems + StandardRecomend
        elif (Result < 9) and (Result >= 6):
            ConclusionText = "<span style=\"color:#ffc000\">Model is not bad.</span> Problems with " + ConclusionItems + StandardRecomend
        elif (Result < 6) and (Result >= 3):
            ConclusionText = "<span style=\"color:#ff5001\">Model with problems.</span> Need to fix " + ConclusionItems + StandardRecomend
        elif Result <= 2 and Result > 0:
            ConclusionText = "<span style=\"color:#ff5001\">Found a lot of problems.</span> Apparently this model was not tested at all. It is necessary to correct all errors and check it again with the checker." 
        elif Result == 0:
            ConclusionText = "<span style=\"color:#ff5001\">Conclusion Error.</span> See log Script Edtior Maya. Maybe there is an answer..." 

    return ConclusionText

    
def fixConclusion(language, FixNumber, FixResult):
    
    ConclusionText = ""

    if language == "rus":

        FixErrorText = "<span style=\"color:#ff5001\">Ошибка не была исправлена.</span> Возможные причины:<br>- Объект был удален<br>- Объект был переименован<br>\
        Изучите лог Script Editor Maya - там может быть указан объект, который вызвал сбой. Проверьте и исправьте объекты с ошибками вручную. Успехов в работе!"

        if FixNumber == "1" and FixResult == True:
            ConclusionText = "Системные единицы измерения были переключены на те, что указаны на вкладке Settings в PolygonTools."
        elif FixNumber == "1" and FixResult == False:
            ConclusionText = FixErrorText 

        if FixNumber == "3" and FixResult == True:
            ConclusionText = "<span style=\"color:#8dc63f\">Pivot Point выделенных объектов был установлен в центр координат - точка [0,0,0].</span> Однако, это могло привести к тому, что Pivot Point теперь находиться за пределами\
                габаритного контейнера (BoundingBox) объекта (пункт проверки №4). Используйте это исправление в зависимости от того, что вам важнее - Pivot в 0 или Pivot в центре габаритного контейнера.\
                    Правка средней степени важности, по этому всегда отмечена желтым, для того, чтобы вы обратили на нее внимание и убедились, что так и было задумано."
        elif FixNumber == "3" and FixResult == False:
            ConclusionText = FixErrorText 

        if FixNumber == "4" and FixResult == True:
            ConclusionText = "<span style=\"color:#8dc63f\">Pivot Point выделенных объектов был установлен в центр их габаритного контейнера.</span> Однако, это могло привести к тому, что Pivot Point теперь находиться не\
                в центре координат (пункт проверки №3). Используйте это исправление в зависимости от того, что вам важнее - Pivot в центре габаритного контейнера или Pivot в 0.\
                    Правка средней степени важности, по этому всегда отмечена желтым, для того, чтобы вы обратили на нее внимание и убедились, что так и было задумано."
        elif FixNumber == "4" and FixResult == False:
            ConclusionText = FixErrorText 

        if FixNumber == "5" and FixResult == True:
            ConclusionText = "<span style=\"color:#8dc63f\">Все спрятанные объекты и слои теперь видимы.</span> Важное исправление! В сцене не должно быть лишних, спрятанных объектов и прочего мусора."
        elif FixNumber == "5" and FixResult == False:
            ConclusionText = FixErrorText 

        if FixNumber == "6" and FixResult == True:
            ConclusionText = "<span style=\"color:#8dc63f\">Для всех выделенных объектов ВЫКЛючено отображение обратной стороны полигонов.</span> Правка средней степени важности.\
                Необходима на финальных этапах работы над моделью. Позволяет увидеть проблемы, связанные с 2-ух сторонней (bouble sided) отрисовкой полигонов в движке. Как правило, по умолчанию \
                    в игровых движках отрисовывается только та сторона полигона, нормаль которой направлена в камеру. Если не учитывать это при моделинге или случайно развернуть\
                        нормали, то в движке мжно увидеть сквозные отверстия или модель вывернутую наизнанку. Это заметный визуальный артефакт. В Maya, по умолчанию, полигоны\
                            отрисовываются с 2-ух сторон. Так удобнее моделить. Не забывайте в конце работы включить Backface Culling!"
        elif FixNumber == "6" and FixResult == False:
            ConclusionText = FixErrorText 

        if FixNumber == "7" and FixResult == True:
            ConclusionText = "<span style=\"color:#8dc63f\">Все трансформации для выделенных объектов были заморожены.</span> Важная правка! На объектах не должно быть трансформаций.\
                Их наличие может привести к непредсказуемому результату при экспорте и игровом движке."
        elif FixNumber == "7" and FixResult == False:
            ConclusionText = FixErrorText 

        if FixNumber == "8" and FixResult == True:
            ConclusionText = "<span style=\"color:#8dc63f\">Была проведена операция Cleanup для всех выделенных объектов.</span> Важная правка. \
            Цель - устранить все не планарные, вогнутые и не 4-х уголные полигоны. Если этих правок мало, то запустите Mesh -> Cleanup в ручном режиме с нобходимыми вам опциями."
        elif FixNumber == "8" and FixResult == False:
            ConclusionText = FixErrorText 

        if FixNumber == "9" and FixResult == True:
            ConclusionText = "<span style=\"color:#8dc63f\">На все выделенные объекты был назначен временный материал.</span> Важная правка. \
            Цель - обнаружить и устранить на объектах в сцене материал по-умолчанию или полное отсутствие материала. Вместо временного, вы можете назначить свой\
                корректный материал."
        elif FixNumber == "9" and FixResult == False:
            ConclusionText = FixErrorText 


    if (language == "eng"):

        FixErrorText = "<span style=\"color:#ff5001\">The error has not been fixed.</span> Possible reasons:<br>- Object has been deleted<br>- Object has been renamed<br>\
        Examine the Maya Script Editor log - the object that caused the crash may be listed there. Check and correct objects with errors manually. Good luck in job!"

        if FixNumber == "1" and FixResult == True:
            ConclusionText = "System units have been switched to those indicated on the Settings tab in PolygonTools."
        elif FixNumber == "1" and FixResult == False:
            ConclusionText = FixErrorText 

        if FixNumber == "3" and FixResult == True:
            ConclusionText = "<span style=\"color:#8dc63f\">The Pivot Point of the selected objects was set to the center of coordinates the point [0,0,0].</span> However, this could lead to the fact that the Pivot Point is now outside\
                objects BoundingBox (check item #4). Use this hotfix depending on which is more important to you - Pivot at 0 or Pivot in the center of the object BBox.\
                    Fix of medium importance. Always marked in yellow so that you pay attention to it and make sure that it was intended."
        elif FixNumber == "3" and FixResult == False:
            ConclusionText = FixErrorText 

        if FixNumber == "4" and FixResult == True:
            ConclusionText = "<span style=\"color:#8dc63f\">Pivot Point of the selected objects was installed in the center of their overall Bounding Box.</span> However this could lead to the fact that the Pivot Point is now\
                not in the center of coordinates (check item #3). Use this fix depending on which is more important for you - Pivot in the center of the object BBox or Pivot at 0.\
                    Fix of medium importance. Always marked in yellow so that you pay attention to it and make sure that it was intended."
        elif FixNumber == "4" and FixResult == False:
            ConclusionText = FixErrorText 

        if FixNumber == "5" and FixResult == True:
            ConclusionText = "<span style=\"color:#8dc63f\">All hidden objects and layers are now visible.</span> Important fix! The scene should not have any hidden objects and other garbage."
        elif FixNumber == "5" and FixResult == False:
            ConclusionText = FixErrorText 

        if FixNumber == "6" and FixResult == True:
            ConclusionText = "<span style=\"color:#8dc63f\">Backface Culling enabled for all selected objects.</span> Medium importance fix.\
                It is necessary at the final stages of work on the model. Allows you to see the problems associated with bouble sided rendering of polygons in the engine. usually by default \
                     in game engines only that side of the polygon is drawn the normal of which is directed to the camera. If you do not take this into account when modeling or accidentally flip \
                        normal then in the engine you can see through holes or a model turned inside out. This is a noticeable visual artifact. In Maya by default polygons \
                             drawn from 2 sides. Maybe it’s more convenient to modeling. Remember to turn on Backface Culling at the end of your work!"
        elif FixNumber == "6" and FixResult == False:
            ConclusionText = FixErrorText 

        if FixNumber == "7" and FixResult == True:
            ConclusionText = "<span style=\"color:#8dc63f\">All transformations for the selected objects were freezed.</span> Important fix! There should be no transformations on objects.\
                Their presence can lead to unpredictable results when exporting and in the game engine."
        elif FixNumber == "7" and FixResult == False:
            ConclusionText = FixErrorText 

        if FixNumber == "8" and FixResult == True:
            ConclusionText = "<span style=\"color:#8dc63f\">A Cleanup operation was performed for all selected objects.</span> Important fix. \
            The goal is to fix all non-planar, concave and n-gons. If you wand fix more then run Mesh -> Cleanup in manual mode with the options you need."
        elif FixNumber == "8" and FixResult == False:
            ConclusionText = FixErrorText 

        if FixNumber == "9" and FixResult == True:
            ConclusionText = "<span style=\"color:#8dc63f\">Temporary material has been assigned to all selected objects.</span> Important fix. \
            The goal is to detect and fix default material (lambert1) or a complete lack of material on objects in the scene. Instead of temporary you can assign your own \
                correct material."
        elif FixNumber == "9" and FixResult == False:
            ConclusionText = FixErrorText 


    return ConclusionText