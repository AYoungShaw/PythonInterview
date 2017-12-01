# 利用递归方法求5!

def fn(x):
	if x == 1 or x == 0:
		return 1
	return x * fn(x-1)

print(fn(5))