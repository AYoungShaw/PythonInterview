# 题目：请输入星期几的第一个字母来判断一下是星期几，如果第一个字母一样，则继续判断第二个字母。
# 程序分析：用情况语句比较好，如果第一个字母一样，则判断用情况语句或if语句判断第二个字母。

# l1 = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

a = 'S'
b = 'u'
c = 'u'

# 先输入一个字母：a
a = input('please input:')

# 判断
if a == "S" or a == "s":
	# 再提示输入一个字母：b
	print('please input again:')
	b = input('please input second:')	
	if b == 'u':
		print('Sunday')
	elif b == 'a':
		print('Saturday')
	else:
		print('data error')

elif a == 'M' or a == 'm':
	print('Monday')

elif a == 'T' or a == 't':
	# 再输入一个字母:c
	print('please input again:')
	c = input('please input second:')
	if c == 'u':
		print('Tuesday')
	elif c == 'h':
		print('Thursday')
	else:
		print('data error')

elif a == 'W' or a == 'w':
	print('Wednesday')

else:
	print('data error')
