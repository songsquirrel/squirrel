# 全局变量与局部变量在函数中使用的区别
def practice(x, *args, **kwargs):
	b = 19;
	if type(x) == int:
		x = 12;
		print("第一个参数为全局变量, 函数中调用并赋值的值为: %s"%x);
		global a
		a = 13;
		print("函数中改变全局变量指向的方法, 改变后的值为: %s"%a);
		print("输入的第一个参数为int型.");
	for arg in args:
		print("输入的多个参数值为: %s"%arg);
	for arg in kwargs:
		print("输入的带键值参数为: %s"%arg);
	print("缺省参数b的默认值为: %s"%b);

def practice1(x, y = 1):
	print("缺省参数b的默认值为: %s"%y);

a = 1;
practice(a, 2, 3, int1 = 1, int2 = 2);
practice1(a);