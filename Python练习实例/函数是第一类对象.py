# 1、 函数名字是对函数的引用
# python中所有都是对象，函数名字是函数对象的引用。

# def foo():
# 	print('in foo')

# print(foo)
# output:
# <function foo at 0x1018f7668>

# 2、函数做为第一类对象可以赋值给其他变量。
# def foo():
# 	print('in foo')

# print(foo)

# f = foo

# print(foo())
# print(f())


# 3、函数作为第一类对象，可以作为参数传递

# def f(*args, **kw):
# 	if args:
# 		for item in args:
# 			print(item)

# 	if kw:
# 		for key in kw:
# 			print(key, kw[key])

# def foo(func, *args, **kw):
# 	func(*args, **kw)

# t1 = (2,3,4,5)
# d1 = {'1':'python', '2':'php', '3':'golang'}

# foo(f, *t1, **d1)


# 4、 函数作为第一类对象， 可以作为函数的返回值。

def foo(x):
	def inner(y):
		return x + y
	return inner

# p = foo(3)
print(foo(3)(5))
# print(p(5))
