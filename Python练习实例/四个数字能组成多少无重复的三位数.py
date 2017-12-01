题目：有四个数字：1、2、3、4，
能组成多少个互不相同且无重复数字的三位数？各是多少？
程序分析：可填在百位、十位、个位的数字都是1、2、3、4。
组成所有的排列后再去掉不满足条件的排列。
count = 0
for a in range(1,5):
	for b in range(1,5):
		for c in range(1,5):
			if a != b and a != c and b != c :
				count += 1
				print(a,b,c)

print('总共有%d个这样的数列'% count)

# python 自带这样的函数
from itertools import permutations
L = []
for i in permutations([1,2,3,4],3):
	L.append(i)
print(len(L))
print(L)


l = [1,2,3,4]
for i in l:
	l1 = l.copy()
	l1.remove(i)
	for j in l1:
		l2 = l1.copy()
		l2.remove(j)
		for k in l2:
			print(i,j,k)