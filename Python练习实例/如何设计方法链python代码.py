class Person(object):
	def name(self, value):
		self.name = value
		return self # 返回实例对象自己才能再调用实例对象的方法

	def work(self, value):
		self.working = value
		return self

	def introduce(self):
		print('你的名字是:' , self.name , ',工作是：', self.working, ',初学python编程')

p = Person()

p.name('MrYang').work('IT').introduce()