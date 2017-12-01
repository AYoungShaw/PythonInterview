import os

# 判断文件夹是否在其中， r是对字符串里面的所有特殊字符不转义
for tmpdir in(r'\tmp', r'E:\Test'):
	# 判断是否文件夹，是就直接退出
	if os.path.isdir(tmpdir):
		break
	else:
		print('no temp directory availiable')
		tmpdir = ''

# 如果有该文件夹
if tmpdir:
	# 切换到该文件夹
	os.chdir(tmpdir)
	# 获取当前的路径，不包括文件
	cwd = os.getcwd()
	print('current temporary directory')
	print(cwd)

	print('creating example directory....')
	# 创建一个文件夹
	os.mkdir('example')
	os.chdir('example')
	cwd = os.getcwd()
	print('new working directory:')
	print(cwd)
	print('original directory listing')
	# 获取指定文件夹下所有的文件或者文件夹,返回一个列表
	print(os.listdir(cwd))

	print('creating test file')
	# 打开一个文件,以写入的模式打开,如果该文件夹不存在就创建
	fobj = open('test', 'w')
	# 写入
	fobj.write('foo\n')
	fobj.write('bar\n')
	# 关闭
	fobj.close()
	print('updated directory listing')
	print(os.listdir(cwd))

	print("renameing 'test' to 'filetest.txt'")
	# 对该文件重命名(old， new)
	os.rename('test', 'filetest.txt')
	print('updated directory listing')
	print(os.listdir(cwd))

	# 将文件夹和文件组成一个完整的路径
	path = os.path.join(cwd, os.listdir(cwd)[0])
	print('full file pathname')
	print(path)
	print('(pathname, basename==)')
	# 将文件和文件夹分割开，返回元组
	print(os.path.split(path))
	print('(filename, extenion)==')
	# os.path.basename(path)去掉文件夹，获取文件名，并返回文件名
	# os.path.splitext(path) 将文件与后缀名分开，返回元组
	print(os.path.splitext(os.path.basename(path)))

	print('displaying file contents')
	fobj = open(path)
	# 读取文件
	for eachline in fobj:
		print(eachline)
	fobj.close()

	print('deleting test file')
	# 删除文件
	os.remove(path)
	print('updated directory listing:')
	print(os.listdir(cwd))
	# 切换到上级目录
	os.chdir(os.pardir)
	print('deleting teset directory')
	# 删除目录
	os.rmdir('example')
	print('done')

