# 利用 time模块的sleep函数

import time

myD = {'a':1, 'b':2, 'c':3}

for k , v in dict.items(myD):
	print(k, v)
	time.sleep(1)

for i in range(1, 5):
	print(i)
	time.sleep(1)