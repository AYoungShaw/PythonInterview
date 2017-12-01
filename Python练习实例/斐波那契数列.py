# 题目：斐波那契数列。
def fib(max):
	n,a,b = 0,0,1
	while n < max:
		yield b
		a, b = b, a + b
		n = n + 1
	return 'done'

d = fib(10)
for i in d:
	print(i)