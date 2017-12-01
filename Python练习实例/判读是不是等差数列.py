# 输入N = 10, A = [3,4,63,3,63,12,32,43,12,23]

N = 10
A = [3,4,63,6,33,12,32,43,16,23]

min1 = min(A)
max1 = max(A)

d1 = (max1 - min1) // (N-1)
B = [0]*N

for i in A:
	j = (i - min1) / d1
	B[j] = 1

if sum(B) == N:
	print(True)
else:
	print(False)