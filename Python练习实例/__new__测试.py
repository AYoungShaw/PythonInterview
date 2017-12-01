# class A(object):
# 	"""docstring for A"""
# 	def __init__(self):
# 		print('init')

# 	def __new__(cls, *arg, **kw):
# 		print('new %s' % cls)
# 		return object.__new__(cls, *arg, **kw)	

# A()	

# 继承自object的新式类才有__new__
# __new__至少要用一个参数cls，代表要实例化的类，此参数在实例化时由python解释器自动提供
# __new__必须要有返回值，返回实例化出来的类。这点在自己实现__new__时要特别注意，
# 可以return父类__new__出来的实例。或者直接是object的__new__出来的实例
# __init__有一个参数self, 就是这个__new__返回的类的实例。
# 若__new__没有正确返回当前类cls的实例，那__init__是不会被调用的。
# 即使是父类的实例也不行

# class A(object):
# 	"""docstring for A"""
# 	pass

# class B(A):
# 	def __init__(self):
# 		print('init')		

# 	def __new__(cls, *args, **kw):
# 		print('new %s' % cls)
# 		return object.__new__(cls, *args, **kw)


# b = B()
# print(type(b))


# class Foo(object):
# 	def __init__(self, *args, **kw):
# 		pass

# 	def __new__(cls, *args, **kw):
# 		return object.__new__(cls, *args, **kw)

# 以上return等同于：
# return object.__new__(Foo, *args, **kw)

# return Stranger.__new__(cls, *args, **kw)

# return Child.__new__(cls, *args, **kw)

# class Child(Foo):
# 		def __new__(cls, *args, **kw):
# 			return object.__new__(cls, *args, **kw)

# 如果Child中没有定义__new__()方法，那么自动调用其父类的__new__方法来制造实例，即Foo.__new__(cls, *args, **kw)
# 在任何新式类的__new__方法，不能调用自身的__new__来制造实例，
# 因为这会造成死循环，因此必须避免类似以下的写法：
# 在Foo中避免: return Foo.__new__(cls, *args, **kw)
# 或者 return cls.__new__(cls, *args, **kw)
# Child同理

# 使用object或者没有血缘关系的新式类的__new__是安全的。
# 但是如果是在有继承关系的两个类之间，应避免互调造成死循环。
# 例如:
# (FOO) return Child.__new__(cls)
# (Child) return Foo.__new__(cls)

# class Strange(object):
# 	pass

# 在制造Stranger实例时，会自动调用
# object.__new__(cls)

# 通常来说，新式类开始实例化时，__new__() 方法会返回cls(cls指代当前类)的实例，
# 然后该类的__init__()方法作为构造方法会接收这个实例(即self)作为自己的第一个参数。
# 然后依次传入__new__()方法中接收的位置参数和命名参数

# 注意：如果__new__方法没有返回cls(即当前类)的实例, 那么当前类的__init__()方法是不会被调用的。
# 如果__new__()返回其他类(新式类或经典类均可)的实例，那么只会调用被返回的那个类的构造方法

# class Foo(object):
# 	def __init__(self, *args, **kw):
# 		pass

# 	def __new__(cls, *args, **kw):
# 		return object.__new__(Stranger, *args, **kw)


# class Stranger(object):
# 	pass

# foo = Foo()
# print(type(foo))
# output:
# <class '__main__.Stranger'>

# 打印的结果显示foo其实是Stranger类的实例

# 因此可以这么描述__new__和__init__()的区别：
# 在新式类中__new__()才是真正的实例化方法，为类提供外壳制造出实例框架
# ，然后调用该框架内的构造方法__init__()使其丰满
# 如果以盖房子做比喻，__new__()方法负责开发地皮，打下地基，并把原料存放在工地。
# 而__init__()方法负责从工地取材料建造出地皮开发招标书中规定的大楼。
# __init__()负责大楼的细节设计，建造，装修使其可交付给客户。



# 代码1：
class Foo(object):
	def __new__(cls, x, *args, **kw):
		self = object.__new__(cls)
		self.x = x
		return self

	def __init__(self, *args, **kw):
		self.args = args
		self.kw = kw


foo = Foo(10, 'args', name='bar')

# 当执行这条foo = Foo(...)语句时：
# 它依次调用了__new__， __init__两个方法

print(foo.x, foo.args, foo.kw)



class Foo(object):
	def __new__(cls, *args, **kw):
		self = object.__new__(cls)
		self.x = args[0]
		self.args = args
		self.kw = kw
		return self

foo = Foo(10, 'args', name='bar')
print(foo.x, foo.args, foo.kw)



class Bar(Foo):
	def __init__(self, *args, **kw):
		self.bar_args = args
		self.bar_kw = kw


bar = Bar(10, 'args', name='bar')

print(bar.__dict__)


# 代码3：
class Foo(object):
	def __init__(self, *args, **kw):
		self.x = args[0]
		self.args = args
		self.kw = kw

foo = Foo(10, 'args', name='bar')
print(foo.x, foo.args, foo.kw)

class Bar(Foo):
	def __init__(self, *args, *kw):
		self.bar_args = args
		self.bar_kw = kw

bar = Bar(10, 'args', name='bar')
print(bar.__dict__)

