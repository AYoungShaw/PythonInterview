创建字典的方法：
1、第一种：
直接创建
dict = {'a' : 'earth', 'b' : 'land'}

2、第二种方法：
工厂方法
items = [('a', 'earth'), ('b', 'land')]
# dict2 = dict(items)

dict3 = dict((['a', 'earth'], ['b', 'land']))

print(dict3)

3、第三种方法：
fromkeys方法
dict1 = {}.fromkeys(('x', 'y'), -1)
print(dict1)
dict2 = {}.fromkeys(('x', 'y'))
print(dict2)

t1 = (1,2,3,4,5)
dict3 = {}.fromkeys(t1, -1)
print(dict3)