import os

path = 'E://Test'

absdir = 'C://'
file = 'E://Test//Test1.txt'
newfile = 'E://Test//Test2.txt'

testfile = 'Test4.txt'
remove1 = 'E://Test//remove1'
# file1

# 1、获取当前python脚本工作的目录路径
print(os.getcwd())
# output:
# E:\Python\Repository\Python面试题\python文件操作

# 2、返回指定目录下的所有文件和目录名
# 返回的是一个list
print(os.listdir('E://Python'))
# output:
# ['Book', 'Install', 'python-3.6.2-amd64.exe', 'Python-3.6.2.tgz', 'Repository']

# 3、包含环境变量的映射关系
# 返回类似environ({key:value})
# 获取path变量的值
# print(os.environ['PATH'])
# output:
# environ({'PROMPT': '$P$G',})

# 4、改变当然目录
# 先改变路径，再获取改变后的路径
os.chdir(path)
print(os.getcwd())

# 5、判断给出的路径是否是一个文件，
# 返回True或者False
print(os.path.isfile(file))

# 6、判断给出的路径是否是一个文件夹。
# 返回True或者False
print(os.path.isdir(path))

# 7、判断是否是绝对路径
# 返回True或者False
print(os.path.isabs(path))

# 8、检验给出的路径是否存在
print(os.path.exists(path))

# 9、返回一个路径的目录名和文件名
# 返回的是一个元组
path1, file1 = os.path.split(file)
print(path1, file1)
# output:
# ('E://Test', 'Test1.txt')

# 10、分离扩展名
# 返回的是一个元组
print(os.path.splitext(file1))
# output:
# ('Test1', '.txt')

# 11、获取路径名
# 返回的是该目录的父级目录
print(os.path.dirname(remove1))
# output:
# E://Test

# 12、获取文件名
print(os.path.basename(file))
# output:
# Test1.txt

# 13、可以运行操作系统里面的命令
# print(os.system('command'))

# 14、读取和设置环境变量
# print(os.getenv('PATH'))
# 设置环境变量
# os.putenv(key, value)

# 15、读取使用的平台：
print(os.name)

# 将两个文件用\进行连接
# 拼接路径用的
print(os.path.join(path, testfile))
# output:
# E://Test\Test4.txt

# 16、重命名：
# os.rename(file, newfile)

# 17、创建多级目录
# os.makedirs('E://Test//test1//test2//test3')

# 18、创建单个目录：
# os.mkdir(r"E:\Test\Test4")

# 19、获取文件属性
# print(os.stat(newfile))

# 20、修改文件权限和时间戳
# os.chmod(newfile, st_atime=1511162830)

# 22、终止当前进程
# os.exit()

# 23、获取文件大小
# print(os.path.getsize(newfile))

# # 24、创建空文件(linux)
# # os.mknod('hello.txt')

# # 25、直接打开一个文件，如果文件不存在则创建文件

# fp = open(newfile, w)
# # w 为打开模式
# # w：以写方式打开，
# # a：以追加模式打开 (从 EOF 开始, 必要时创建新文件)
# # r+：以读写模式打开
# # w+：以读写模式打开 
# # a+：以读写模式打开 
# # rb：以二进制读模式打开
# # wb：以二进制写模式打开 
# # ab：以二进制追加模式打开 
# # rb+：以二进制读写模式打开 
# # wb+：以二进制读写模式打开 
# # ab+：以二进制读写模式打开 

# # 读取size长度的字符，以byte为单位
# fp.read([size])

# #读一行，如果定义了size，有可能返回的只是一行的一部分
# fp.readline([size])

# #把文件每一行作为一个list的一个成员，并返回这个list。如果提供size参数，size是表示读取内容的总长，可能只读到文件的一部分
# fp.readlines([size])

# #把str写到文件中。write()并不会在str后加入一个换行符
# fp.write(str)

# #把seq的内容全部写到文件中(多好一次性写入)，只会写入，不会再每行后面加入任何东西
# fp.writelines(seq)

# # 关闭文件
# fp.close()

# # 把缓冲区的内容写到硬盘中
# fp.flush()


try:
	fh = open('testfile', 'w')
	try:
		fh.write('这是一个测试文件，用于测试异常')
	finally:
		print('关闭文件')
		fh.close()
		
except IOError:
	print('Error: 没有找到文件或读取文件失败')