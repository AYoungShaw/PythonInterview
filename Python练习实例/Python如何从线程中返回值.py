# python 从多线程中返回值，有多种方法：
# 1、常见的有写一个自己的多线程类，写一个方法返回
# 2、可以设置一个全局的队列返回值。
# 3、也可以用multiprocessing.pool.ThreadPool

import time

from threading import Thread

def foo(number):
	time.sleep(20)
	return number

class MyThread(Thread):
	def __init__(self, number):
		Thread.__init__(self)
		self.number = number

	def run(self):
		self.result = foo(self.number)

	def get_result(self):
		return self.result


thd1 = MyThread(3)
thd2 = MyThread(5)

thd1.start()
thd2.start()

thd1.join()
thd2.join()

print(thd1.get_result())
print(thd2.get_result())