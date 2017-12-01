import threading

from time import sleep, ctime

loops = [4, 2]

class ThreadFunc(object):
	def __init__(self, func, args, name=''):
		self.name = name
		self.func = func
		self.args = args

	def __call__(self):
		self.res = self.func(*self.args)

class MyThread(threading.Thread):
	def __init__(self, func, args, name=''):
		threading.Thread.__init__(self)
		self.name = name
		self.func = func
		self.args = args

	def run(self):
		# python3
		# 已经不支持了
		# apply(self.func,self.args)
		# 改为
		self.func(*self.args)

def loop(nloop, nsec):
	print('start loop %s at: %s\n' % (nloop, ctime()))
	sleep(nsec)
	print('loop%s done at:%s\n' % (nloop, ctime()))

def main():
	print('starting at:%s\n' % ctime())

	threads = []
	nloops = range(len(loops))

	for i in nloops:
		# 第一种
		# t = threading.Thread(target=loop, args=(i, loops[i]))
		# threads.append(t)
		# 第二种
		# t = threading.Thread(target=ThreadFunc(loop, (i, loops[i]), loop.__name__))
		# threads.append(t)
		# 第三种
		t = MyThread(loop, (i, loops[i]), loop.__name__)
		threads.append(t)

	for i in nloops:
		threads[i].start()

	for i in nloops:
		threads[i].join()

	print('all done at:%s\n' % ctime())

if __name__ == '__main__':
	main()