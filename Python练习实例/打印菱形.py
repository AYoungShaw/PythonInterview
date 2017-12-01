# 打印出如下图案（菱形）:
#    *
#   ***
#  *****
# *******
#  *****
#   ***
#    *

# 程序分析：先把图形分成两部分来看待，
# 前四行一个规律，后三行一个规律，
# 利用双重for循环，第一层控制行，第二层控制列。

# from sys import stdout

# for i in range(4):
# 	for j in range(2 - i + 1):
# 		stdout.write(' ')
# 	for k in range(2 * i + 1):
# 		stdout.write('*')
# 	print()	

# for i in range(3):
# 	for j in range(i + 1):
# 		stdout.write(' ')
# 	for k in range(4 - 2 * i + 1):
# 		stdout.write("*")
# 	print()


# for i in range(1, 5):
# 	print(''*(4-i), end='')
# 	for j in range(1, 2*i):
# 		print('*', end='')
# 	print()

# for i in range(3, 0, -1):
# 	print(''*(4-i), end="")
# 	for j in range(1, 2*i):
# 		print('*', end='')
# 	print()

# output：
# *
# ***
# *****
# *******
# *****
# ***
# *

def pic(lines):
	middle, lines = int(lines / 2), int(lines / 2) * 2 + 1
	for i in range(1, lines + 1):
		empty = abs(i - middle - 1)
		print(''* empty, '*'*(2 * (middle - empty) + 1))

pic(7)
# output：
#  *
#  ***
#  *****
#  *******
#  *****
#  ***
#  *