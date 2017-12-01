题目：一个整数，它加上100后是一个完全平方数，
再加上168又是一个完全平方数，请问该数是多少？
分析:
x + 100 = n^2, x + 100 + 168 = m^2
m^2 - n^2 = (m + n)(m - n) = 168
设置 m + n = i, m - n = j , i * j = 168 , i 和 j 至少一个是偶数
m = (i + j)/2, n = (i - j)/2
由于i * j  = 168 ,j >= 2  则 1 < i <  168/2 + 1
for i in range(1,85):
	if 168 % i == 0:
		j = 168 / i
		if i > j and (i + j) % 2 == 0 and (i - j) % 2 == 0:
			m = (i + j)/2
			n = (i - j)/2
			x = n*n -100
			print(x)

for m in range(168):
	for n in range(m):
		if (m+n)*(m-n) == 168:
			x = n**2 - 100
			print('符合条件的数为:%d' % x)