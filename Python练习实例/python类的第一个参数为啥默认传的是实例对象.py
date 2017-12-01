
# 如果类没有定义__new__方法，就从父类继承这个__new__方法
# __new__先于__init__执行，
# 类带括号调用时，发生这样的事
# 先调用类的__new__方法，返回该类的实例对象，
# 这个实例对象就是__init__方法的第一个参数

class Foo(object):
	"""docstring for Foo"""
	def __new__(cls, *arg, **kw):
		"""如果不覆盖这个__new__方法，
		类就继承object类的__new__方法返回值实例对象
		"""
		print('__new__ 方法先被调用')
		tmp = super(Foo, cls).__new__(cls, *arg, **kw)
		print(id(tmp))
		print(type(tmp))

		print(isinstance(tmp, Foo))
		print(issubclass(type(tmp), Foo))

		return tmp



	def __init__(self):
		print('__init__被调用')		
		print(id(self))


p = Foo()
print(id(p))
print(type(p))
