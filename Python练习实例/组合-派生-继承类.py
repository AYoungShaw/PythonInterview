# 组合类:
# 类是由它自身和其他类组合而成
# 这就在一个类和其他组成类之间定义了一个"has-a"关系

# class Name(object):
# 	def __init__(self, nm):
# 		self.name = nm

# class Phone(object):
# 	def __init__(self, ph):
# 		self.phone =  ph


# class NewAddrBookEntry(object):
# 	def __init__(self, nm, ph):
# 		self.name = Name(nm)
# 		self.phone = Phone(ph)
# 		print('Created instance for :', self.name)
# 		# 调用self.name这个实例的name属性
# 		print('Created instance for :', self.name.name)

# foo = NewAddrBookEntry('Paul', 123456)


# 子类和派生
# 当类与类之间有显著的不同，并且较小的类是较大的类所需要的组件时
# 组合表现的不错。
# 但如果要设计"相同的类但由一些不同的功能"时，派生就是更合理的选择了。


# 继承：
# 继承描述了基类的属性如何"遗传"给派生类，一子类可以继承它的基类的任何属性，不管是数据属性还是方法


# class P:
# 	def __init__(self):
# 		print('created an instance of ', self.__class__.__name__)

# class C(P):
# 	pass

# p = P()

# a = P()

# print(p.__class__)
# print(P.__bases__)

# c = C()
# print(c.__class__)

# print(C.__bases__)

# __bases__类属性
# __bases__类属性是一个包含其父类的集合的元组。

# 核心笔记：重写__init__不会自动调用基类的__init__


# 1、不可变类型的例子：
# 处理一个浮点数的子类，每次得到一个货币值，都需要四舍五入，变为带两位小数位的数值
class RoundFloat(float):
	def __new__(cls, val):
		return float.__new__(cls, round(val, 2))

# 我们使用round()内建函数对元浮点数进行舍入操作，然后实例化我们的float，RoundFloat、
# 我们是通过调用父类的构造器来创建真实的对象， float.__new__()。注意所有的__new__()方法是类方法，我们要显式传入类作为第一个参数

print(RoundFloat(1.539483))

# 2、可变类型的例子
# 子类化一个可变类型于此相似
class SortedKeyDict(dict):
	"这是文档注释"
	def keys(self):
		return sorted(super(SortedKeyDict, self).keys())

	# def keys(self):
	# 	return sorted(self.keys())

d = SortedKeyDict({'Anna':68, 'John':56, 'Frank':67})
print('By iterator', [key for key in d])


print(SortedKeyDict.__doc__)
print('By keys():', d.keys())


# 类、实例和其他对象的内建函数
# issubclass()
# 这是布尔函数，判断一个类是不是另一个类的子类或者子孙类

# isinstance()
# 这个布尔函数判断一个对象是否是另一个给定类的实例

# hasattr()
# 是布尔类型，它的目的是为了决定一个对象是否有一个特定的属性，
# 一般用于访问某些属性前做一下检查。

# getattr()和setattr()
# 相应的取得和赋值给对象的属性，
# getattr()在你试图读取一个并不存在的属性，会引发AttributeError异常
# setattr()将要加入一个新的属性，要么取代一个已存在的属性，
# 而delattr()函数会从一个对象中删除属性

# dir()和super()
