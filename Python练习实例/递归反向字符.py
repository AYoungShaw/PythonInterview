# 题目：利用递归函数调用方式，将所输入的5个字符，以相反顺序打印出来。

# 思路：
# 函数的功能先打印最后一位，然后再调用函数，每次打印最后一位
def output(s, l):
	if l == 0:
		return
	print(s[l-1], end='')
	output(s, l-1)

s = 'abcd'

l = len(s)
output(s, l)