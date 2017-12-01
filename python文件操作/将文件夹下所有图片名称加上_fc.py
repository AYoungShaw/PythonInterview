import re

import os

import time

def change_name(path):
	global i
	# 如果给定的路径不是文件夹也不是文件名就返回false
	if not os.path.isdir(path) and not os.path.isfile(path):
		return False

	if os.path.isfile(path):
		# 分割目录和文件
		file_path = os.path.split(path)

		# 分割文件和扩展名
		lists = file_path[1].split('.')

		# 取出后缀名
		file_ext = lists[-1]
		
		img_ext = ['bmp', 'jpeg', 'jpg', 'png', 'psd']

		if file_ext in img_ext:
			# 改名
			os.rename(path, file_path[0] + '/' + lists[0] + '_fc.' + file_ext)
			i += 1

	# 如果是目录的话		
	elif os.path.isdir(path):
		# 列出当前目录下所有文件和目录
		for x in os.listdir(path):
			# 在调用函数，将当前目录下的文件或者目录用join组合起来
			change_name(os.path.join(path, x))

img_dir = 'E://Test'
img_dir = img_dir.replace('\\', '/')

start = time.time()
i = 0
change_name(img_dir)
c = time.time() - start
print('程序运行耗时:%0.2f'%(c,))
print('总共处理了%s张图片'%(i,))		