# 2019-07-09 practice

# 可变数据类型: 列表, 字典..
# 不可变数据类型: 数值, 字符串, 元组..

def for_practice(param):
	turple = ('1', '2', '3'); # 元组是不可变数据类型
	for element in turple:
		if element == param:
			print('找到了%s'%element);
			break;
	else:
		print('啥玩意耶!');

for_practice('2');

a = [1, 2];
b = a + [3, 4];
# 最终 a = [1, 2], b = [1, 2, 3, 4];
# 如果使用+=则: a = b = [1, 2, 3, 4];
# 列表是可变数据类型, '='赋值时, 会先将'='右边的表达式计算出来
# 在内存中生成一个新的常量, 然后将左边的指向这个常量
