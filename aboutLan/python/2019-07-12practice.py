# 对文件的操作
import os
import os.path
import datetime
import time

rootDir = "E:\\aDream\\squirrel"  # 指明遍历的文件夹

# parent: 根目录; dirNames: 根目录下的所有文件夹目录; fileNames: 根目录下的所有文件名
# 这个遍历是深度遍历, 
for parent, dirNames, fileNames in os.walk(rootDir):
	print("parent dictory is: " + parent);
	for dirName in dirNames:
		print(parent + "下的目录: " + dirName);
	for fileName in fileNames:
		print(parent + "下的文件:" + fileName);

# 获取单个目录下的子节点(文件夹和文件)
for dirName in os.listdir(rootDir):
	print (dirName);
# 获取当前时间
now = datetime.datetime.now();
print("当前年份: %s, 当前月份: %s, 当前几号: %s"%(now.year, now.month, now.day);
# 打印年-月-日
print(time.strftime("%F"));
	