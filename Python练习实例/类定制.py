# class RoundFloatManual(object):
# 	def __init__(self, val):
# 		assert isinstance(val, float),\
# 		'Value must be a float'
# 		self.value = round(val, 2)

# 	def __str__(self):
# 		return str(self.value)

# 	__repr__ = __str__

# rmf = RoundFloatManual(12.2323)
# print(rmf)



# 数值定制：

# class Time60(object):
# 	'''Time60- track hours and minutes'''

# 	def __init__(self, hr, min):
# 		self.hr = hr
# 		self.min = min

# 	def __str__(self):
# 		return '%d:%d' %(self.hr, self.min)

# 	__repr__ = __str__
	
# 	# 加法：
# 	def __add__(self, other):
# 		newhr = self.hr + other.hr
# 		newmin = self.min + other.min
# 		if newmin >=60:
# 			newmin -= 60
# 			newhr += 1

# 		if newhr >= 24:
# 			newhr -= 24
# 			return self.__class__(newhr, newmin)

# 	# 3、原位加法
# 	def __iadd__(self, other):
# 		self.hr += other.hr
# 		self.min += other.min

# 		if self.min >= 60:
# 			self.min -= 60
# 			self.hr += 1

# 		if self.hr >= 24:
# 			self.hr -= 24

# 		return self


# mon = Time60(10, 30)
# tue = Time60(11, 15)

# print(mon, tue)


# 迭代器

# from random import choice

# class RandSeq(object):
# 	'''随机无穷迭代'''
# 	def __init__(self, seq):
# 		self.data = seq

# 	def __iter__(self):
# 		return self

# 	def __next__(self):
# 		return choice(self.data)

# class AnyIter(object):
# 	'''任意项的迭代器'''
# 	def __init__(self, data, safe=False):
# 		self.safe = safe
# 		self.iter = iter(data)

# 	def __iter__(self):
# 		'''让类变成迭代器'''
# 		return self

# 	def __next__(self, howmany=1):
# 		retval = []
# 		for eachitem in range(howmany):
# 			try:
# 				retval.append(self.iter.__next__())
# 			except StopIteration:
# 				if self.safe:
# 					break
# 				else:
# 					raise

# 		return retval


# a = AnyIter(range(10))

# i = iter(a)
# for j in range(1,5):
# 	print(j, ':', i.__next__(j))


# 多类型定制
# 我们创造一个新类，NumStr，由一个数字-字符对组成，相应地，记为n和s，数值类型使用整型。
# 尽管这组顺序对的合适的记号是(n, s)但是我们选用[n::s]来表示它。
# 暂不管这个记号，我们只需要考虑数据元素模型就好了，是一个整体。
# 这个新类有这样的特征：
# 初始化：对数字和字符串进行初始化，
# 如果其中一（或二）个没有初始化，数字用0，字符串用空字符串作为默认参数。
# 加法：功能是数字相加，字符串按顺序相连。
# 乘法：数字相乘，字符串累积相连。
# False值：当数字为0且字符串为空是，这个实体有一个False值。
# 比较：一对NumStr对象比较应该有九种不同的组合（n1>n2 and s1<s2,n1 == n2 and s1>s2等等）。
# 对数字和字符串，我们按标准的数值和字典顺序进行比较，然后将比较的值相加返回结果。

# class NumStr(object):
# 	def __init__(self, num=0, string=''):
# 		self.__num = num
# 		self.__string = string

# 	def __str__(self):
# 		# define for str()
# 		return '[%d::%r]' %(self.__num, self.__string)

# 	__repr__ = __str__

# 	def __add__(self, other):
# 		# define for s+o
# 		if isinstance(other, NumStr):
# 			return self.__class__(
# 						self.__num + other.__num,
# 				 		self.__string + other.__string)
# 		else:
# 			raise TypeError,
# 			'Illegal argument type for built-in operation'


# 	def __mul__(self, num):
# 		# define for s*o
# 		if isinstance(num, int):
# 			return self.__class__(
# 					self.__num * num,
# 					self.__string * num)
# 		else:
# 			raise TypeError,
# 			'Illegal argument type for built-in operation'

# 	def __nonzero__(self):
# 		# define reveal tautology
# 		return self.__num or len(self.__string)

# 	def __norm_cval(self, cmpres):
# 		# normalize cmp()
# 		return cmp(cmpres, 0)

# 	def __cmp__(self, other):
# 		# define for cmp()
# 		return self.__norm_cval(cmp(self.__num, other.__num)) +
# 				self.__norm_cval(cmp(self.__string, other.__string))


# 授权

# class WrapMe(object):
# 	def __init__(self, obj):
# 		self.__data = obj

# 	def get(self):
# 		return self.__data

# 	def __repr__(self):
# 		return self.__data

# 	def __str__(self):
# 		return str(self.__data)

# 	def __getattr__(self, attr):
# 		return getattr(self.__data, attr)

# # 复数举例
# wrappedComplex = WrapMe(3.3 +1.2j)

# print(wrappedComplex)

# print(wrappedComplex.real)
# print(wrappedComplex.imag)
# print(wrappedComplex.conjugate())
# print(wrappedComplex.get())
# output:
# (3.3+1.2j)
# 3.3
# 1.2
# (3.3-1.2j)
# (3.3+1.2j)
# 我们访问了复数的三种属性，而这在类中一种都没有定义。
# 对这种属性的访问，是通过__getattr__()方法，授权给对象。
# 最终调用的get()方法没有授权，因为它是为我们对象单独定义的。

# 添加时间属性的类

from time import time, ctime

class TimeWrapMe(object):
	def __init__(self, obj):
		self.__data = obj
		self.__ctime = self.__mtime = self.__atime = time()

	def get(self):
		self.__atime = time()
		return self.__data

	def gettimeval(self, t_type):
		if not isinstance(t_type, str) or t_type[0] not in 'cma':
			raise TypeError('argument of c, m, or a req\'d')

		return getattr(self, '_%s__%stime' %(self.__class__.__name__, t_type[0]))

	def gettimestr(self, t_type):
		return ctime(self.gettimeval(t_type))

	def set(self, obj):
		self.__data = obj
		self.__mtime = self.atime = time()

	def __repr__(self):
		self.__atime = time()
		return self.__data

	def __str__(self):
		self.__atime = time()
		return str(self.__data)

	def __getattr__(self, attr):
		self.__atime = time()
		return getattr(self.__data, attr)

TimeWrapMeObkj = TimeWrapMe(123)
print(TimeWrapMeObkj.gettimestr('c'))
print(TimeWrapMeObkj.gettimestr('m'))
print(TimeWrapMeObkj.gettimestr('a'))

TimeWrapMeObkj.set('Update time!')
print(TimeWrapMeObkj.gettimestr('c'))