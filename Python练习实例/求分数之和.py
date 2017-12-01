# 有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前20项之和。
# 程序分析：请抓住分子与分母的变化规律。

# 分子加分母为第二项的分子。
# 第一项的分子为第二项的分母

# 把 a 赋值给 b
# 再把 a + b 赋值给 a
# 核心的语法是 b, a = a, a + b

a = 2.0
b = 1.0 
s = 0
# 方法1：
for i in range(1, 21):
	s += a/b
	b, a = a, a + b
print(s)

# 方法2：
# 将数据放在数组中，再利用reduce作用在数组上进行求和
from functools import reduce
l = []
l.append(a/b)
for i in range(1, 20):
	b, a = a, a + b 
	l.append(a/b)
print(reduce(lambda x , y: x + y, l))
