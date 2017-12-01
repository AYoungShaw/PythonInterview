

L1 = ['1','3','6','2','5','3','8','2','8']

# 第一种方法：
# 用set
print(list(set(L1)))

# 第二种方法：
# 用字典
L2 = {}.fromkeys(L1).keys()

print(list(L2))

# 第三种方法：
# 用字典并保持顺序
L3 = list(set(L1))
L3.sort(key=L1.index)
print(L3)

# 第四种方法：
# 列表生成式
L4 = []

print([i for i in L1 if i not in L4])

for i in L1:
	if i not in L4:
		L4.append(i)

print(L4)
