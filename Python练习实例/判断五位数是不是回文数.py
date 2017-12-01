# 题目：一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同。

# 方法1：
# a = 12321

# x = str(a)
# flag = True

# for i in range(len(x)//2):
# 	if x[i] != x[-i - 1]:
# 		flag = False
# 		break

# if flag:
# 	print('这是一个回文数', a)
# else:
# 	print('这不是一个回文数', a)


# 方法2：

a = '12321'
b = a[::-1]

if a == b:
	print('这是一个回文数', a)
else:
	print('这不是一个回文数', a)