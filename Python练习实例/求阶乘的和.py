# 题目：求1+2!+3!+...+20!的和。

# 程序分析：此程序只是把累加变成了累乘。
# t *= i 其实意思就是将前一项都累乘
# s += t  再把累乘的加起来。就是阶乘累加

# 核心思想就是
# t *= i
# s *= t

# 方法1：
t = 1
s = 0

for i in range(1, 21):
	t *= i
	s += t

print(s)

# 方法2：
# 利用map将函数作用到列表上，最后求和
s = 0
l = range(1, 21)

def op(x):
	r = 1
	for i in range(1, x + 1):
		r *= i
	return r

print(sum(map(op, l)))


# 方法3：
# 递归方法
s = 0 
def fact(n):
	if n == 1:
		return 1
	# 阶乘就是前一项乘以后一项
	return n * fact(n-1)

for i in range(1, 21):
	a = fact(i)
	s += a
print(s)