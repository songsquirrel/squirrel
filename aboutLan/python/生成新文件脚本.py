import os, time, sys

# 当前文件所在的绝对路径, 不包括文件名
folderPath = sys.path[0];

# 在此脚本同级路径的Local文件夹下创建新文件
# fileName : 新文件的文件名,
# fileType : 新文件的文件类型
def makeFile(fileName, fileType, folderPath):
	print(type(fileName));
	if type(fileName) != str :
		print("参数fileName传入有误.");
		return;
	if type(fileType) != str :
		print("参数fileType传入有误.");
		return;
	if fileType.startswith("."):
		pass;
	else:
		fileType = "." + fileType;
	print(os.getcwd());
	#print("sys.path:%s"%sys.path);
	# 判断文件夹是否存在,不存在则创建
	#if not folderPath:
	#	os.makedirs(folderPath);
	# 创建文件
	filePath = os.path.join(folderPath, fileName+fileType);
	f = open(filePath, "w+");
# 根据当前日期获取生成新文件的文件名
def getFileName(date, folderPath):
	# 记录当前日期总共有几个同名文件的参数
	i = 1;
	for path in os.listdir(folderPath):
		# 如果遍历的是文件
		print(path);
		print("sys.path[0]:"+folderPath);
		print("abspath:"+os.path.abspath(path));
		print("realpath:"+os.path.realpath(path));
		print(path.startswith(date));
		print(os.path.isfile(os.path.join(folderPath, path)));
		if os.path.isfile(os.path.join(folderPath, path)) and path.startswith(date) :
			i += 1;
	else : # for循环执行完之后执行
		fileNameConfigPath = os.path.join(folderPath, "config", "fileNameConfig")
		if os.path.isfile(fileNameConfigPath) :
			fileRW = open(fileNameConfigPath);
			try:
				fileNameConfig = fileRW.readlines();
				print(fileNameConfig);
				for line in fileNameConfig:
					print(line);
					if line.strip().startswith("#") :
						continue;
					else :
						pass
			finally:
				fileRW.close();

	return "%s-practice-%02d"%(date, i);






# 新文件格式: 年-月-日-practice-01.py
# 先判断当前是否存在同日的文件, 再添加序号
def main():
	# 获取文件名前缀--年-月-日
	date = time.strftime("%F");
	print(date);
	fileType = ".py";
	fileName = getFileName(date, folderPath);
	makeFile(fileName, fileType, folderPath);

main();
