# 所谓单例，是指一个类的实例从始至终只能被创建一次。


# 方法1：
# 实现__new__方法
# 并在将一个类的实例绑定到类变量_instance上
# 如果cls._instance 不为None, 直接返回cls._instance

# class Singleton(object):
# 	def __new__(cls, *args, **kw):
# 		if not hasattr(cls, '_instance'):
# 			orig = super(Singleton, cls)
# 			print(type(orig))
# 			cls._instance = orig.__new__(cls, *args, **kw)
# 			print(cls._instance)
# 		return cls._instance

# class MyClass(Singleton):
# 	a = 1

# 类名使用我们所熟悉的函数操作符（()），
# 以“函数调用”的形式出现。然后你通常会把这个新建的实例赋给一个变量。赋值在语法上不是必须的

# 其实在实例类的时候是用函数调用的形式，通常会在新建一个实例的时候赋值给一个变量，也就是这里的one，但是赋值在语法上不是必须的

# one = MyClass()
# 慢慢来分析：
# 当执行one = MyClass()这条语句时
# 分别调用MyClass()的__new__, __init__方法
# 由于MyClass类中没有__new__方法，则会去它的父类查找
# 它的父类Singleton实现了__new__方法
# 先判断这个类中是否

# print(MyClass.__mro__)
# print(Singleton.__mro__)


# two = MyClass()
# # print(MyClass)
# two.a = 3
# print(one.a)
# print(id(one), id(two))

# print(one == two)
# print(one is two)


# 方法2：
# 共享属性，所谓单例就是所有引用都拥有相同的状态和行为
# 同一个类的所有实例天然拥有相同的行为
# 只需要保证同一个类的所有实例具有相同的状态即可
# 所有实例共享属性的最简单最直接的方法是__dict__属性指向同一个字典

# class Borg(object):
# 	_state = {}

# 	def __new__(cls, *args, **kw):
# 		ob = super(Borg, cls).__new__(cls, *args, *kw)
# 		ob.__dict__ = cls._state
# 		return ob

# class MyClass2(Borg):
# 	a = 1

# one = MyClass2()
# two = MyClass2()

# # one 和 two是两个不同的对象
# two.a = 3
# print(one.a)
# print(id(one), id(two))

# print(one is two)
# print(one == two)

# # 但是one和two具有相同的(同一个__dict__属性)
# print(id(one.__dict__), id(two.__dict__))

# print(one.__dict__)




# 方法3：
# 本质上是方法1的升级版
# 使用metaclass的高级python用法
# class Singleton2(type):
# 	def __init__(cls, name, bases, dict):
# 		super(Singleton2, cls).__init__(name, bases, dict)
# 		cls._instance = None

# 	def __call__(cls, *args, **kw):
# 		if cls._instance is None:
# 			cls._instance = super(Singleton2, cls).__call__(*args, **kw)

# 		return cls._instance

# class MyClass3(object):
# 	__metaclass__ = Singleton2

# one = MyClass3()
# two = MyClass3()

# two.a = 3
# # print(one.a)

# print(id(one), id(two))

# print(one == two, one is two)


# 方法4：
# 使用装饰器
# def singleton3(cls, *args, **kw):
# 	instances = {}

# 	def _singleton():
# 		if cls not in instances:
# 			instances[cls] = cls(*args, **kw)
# 		return instances[cls]
# 	return _singleton

# @singleton3
# class Myclass4(object):
# 	a = 1
# 	def __init__(self, x=0):
# 		self.x = x

# one = Myclass4()
# two = Myclass4()

# two.a = 3
# print(one.a)

# print(id(one), id(two))

# print(one == two, one is two)


class Foo(object):
	"""docstring for Foo"""
	def __init__(self, arg):
		self.arg = arg


class Child(Foo):
	def fn(self):
		print('this is child')	

a = Child('hello')