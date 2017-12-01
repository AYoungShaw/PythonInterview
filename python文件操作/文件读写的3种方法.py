# read() 将文本文件所有行读到一个字符串中。
# readline()是一行一行的读
# readlines() 是将文本文件中所有行读到一个list中，文本文件每一行是list的一个元素

# 优点：
# readline()可以在读行的过程中跳过特定的行

# # 第一种方法：
# file1 = open('test.txt')

# file2 = open('output.txt', 'w')

# while True:
# 	line = fie1.readline()
# 	#进行逻辑处理
# 	file2.write('"' + line[:s] + '"' + ',')
# 	if not line:
# 		break

# # 关闭文件
# file1.close()
# file2.close()

# # 第二种方法：

# # 文件迭代器，用for循环的方法
# file2 = open('output.txt', 'w')

# for line in open('test.txt'):
# 	file2.write('"' + line[:s] + '"' + ',')

# file2.close()


# # 第三者方法：
# # 文件上下文管理器

# with open('somefile.txt', 'r') as f:
# 	data = f.read()

# with open('somefile.txt', 'r') as f:
# 	for line in f:
# 		process line

# with open('somefile.txt', 'w') as f:
# 	f.write(text1)
# 	f.write(text2)


# with open('somefile.txt', 'w') as f:
# 	print(line1, file=f)
# 	print(line2, fiel=f)
	

filename = 'test.txt'

with open(filename, 'r', encoding='utf8') as f:
	for line in f:
		print(type(line))
		print(line)