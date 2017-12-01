# 题目：求100之内的素数。

# 素数只能被1和它本身整除

# 分析：
# 将自己分别于它一半的数就余数，如果余数为0就不是素数

# for  i in range(1,101):
# 	if i > 1:
# 		for j in range(2, i // 2 + 1):
# 			if (i % j) == 0:
# 				break
# 		else:
# 			print(i)

# a = [1,2,3]
# b = ['a','b','c']
# z = zip(a, b)
# print(z)


