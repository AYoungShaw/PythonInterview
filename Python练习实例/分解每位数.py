# 题目：给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字。
# 程序分析：学会分解出每一位数。


def fn(a):
	wan = a // 10000
	qian = a % 10000 // 1000
	bai = a % 1000 // 100
	shi = a % 100 // 10
	ge = a % 10

	if wan != 0:
		print('这是五位数:', wan, qian, bai, shi, ge)
	elif qian != 0 :
		print('这是四位数:', qian, bai, shi, ge)
	elif bai != 0:
		print('这是三位数:', bai, shi, ge)
	elif shi != 0 :
		print('这是二位数:', shi, ge)
	else:
		print('这是一位数:', ge)

fn(432)