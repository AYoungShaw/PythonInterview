
def make_actions():
	acts = []

	for i in range(5):
		acts.append(lambda x: i**x)
	return acts

foo = make_actions()

print(foo[0](2))
print(foo[1](2))
print(foo[2](2))
print(foo[3](2))
# output:
#16
# 16
# 16
# 16

# 这个函数分析：
# 可以看到这个函数是一个典型的闭包问题，
# 里面的lambda函数接收参数x，并接收外围函数的变量
# 返回一个列表acts

# 所以实际上：
# 当foo = make_actions()时，返回的就是一个列表了
# 但是这个列表中存在多个函数
# 所以foo[0](2)的意思是取列表中第一个元素的函数，并传入参数2

# 为什么输出是16呢？
# 输出16，说明i的值都是4，
# 原因在于闭包对外围函数的内部变量查询发生在其被调用的时候
# 这个时候这个值已经变成4了。所以所有的闭包都查到的是4.


def make_actions():
	acts = []

	for i in range(5):
		acts.append(lambda x, i=i: i**x)
	return acts

foo = make_actions()

print(foo[0](2))
print(foo[1](2))
print(foo[2](2))
print(foo[3](2))
# output:
# 0
# 1
# 9
# 16

# 为什么输出不是16了呢？
# 因为通过缺省值传递，强制定义闭包的时候就对外围函数这个剧本变量求值
# 也就将其当下的值封存在闭包自己局部变量中

