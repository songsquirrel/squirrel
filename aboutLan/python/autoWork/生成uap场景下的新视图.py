# encoding utf-8
import xml.dom.minidom
import os, sys

# 文件的绝对路径
absPath = sys.path[0]
# 文件类型,默认js
fileType = '.js'
# 场景名
faceId = ''
faceName = ''
faceDescrption = ''

# 生成view的全局变量
viewName = 'MainView'

# 生成controller的全局变量


# 初始化获取全局变量的值
def __initVariable () :
    # 打开common.xml文件
    dom_common = xml.dom.minidom.parse(os.path.join(absPath, 'resources', 'config', 'common.xml'))
    faceId = dom_common.getElementsByTagName('faceId')
    # faceName = dom_common.getElementsByTagName('faceName')
    # faceDescrption = dom_common.getElementsByTagName('descrption')
    # 打开view.xml文件
    dom = xml.dom.minidom.parse(os.path.join(absPath, 'resources', 'config', 'view.xml'))
    viewName = dom.getElementsByTagName("fileName")
    components = dom.getElementsByTagName("component")

def createFile ():
    # 输出文件路径
    outputFilePath = os.path.join(absPath, 'output', viewName+fileType)

    # 数据来源路径
    resourcePath = os.path.join(absPath, 'resources', 'static', 'scripts', 'views', 'MainView.js')

    outputFile = open(outputFilePath, 'w')
    with open(resourcePath, 'r') as resource :
        for line in resource :
            if(line.index('${faceId}') > -1) :
                line.replace('${faceId}', faceId)
                outputFile.write(line)
            elif (line.index('//component_import') > -1):
                line_write = '$import '
                outputFile.write(line_write)
            elif (line.index('//component_invoke') > -1):
                    pass
            elif (line.index('//component_init') > -1):
                    pass
            elif (line.index('//component_show') > -1):
                    pass
            else :
                outputFile.write(line)
        else :
            outputFile.close()

__initVariable()    

