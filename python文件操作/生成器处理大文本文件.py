# 对于大文件，可以先切分N个小文件
# 几十G的先切分为N个小文件，再处理

import time

start_time = time.time()

def find_ip(path):
	
	for line in open(path):
		s = line.find("Sogou web spider")
		if s >= 0:
			yield line[:s].strip()

p = find_ip("bigfile.txt")
p = list(set(list(p)))
for item in p:
	print(item)

print(time.time() -start_time, 'seconds')