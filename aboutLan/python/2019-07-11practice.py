# 匿名函数的使用
orderList = [{"name": "a", "age": "3"}, {"name": "b", "age": "2"}, {"name": "a", "age": "1"}];
o = orderList.sort(key = lambda x:x["name"]);
print(o);
print(orderList);