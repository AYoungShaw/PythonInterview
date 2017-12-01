# 在一个m行n列二维数组中，每一行都按照从左到右递增的顺序排序，
# 每一列都按照从上到下递增的顺序排序。
# 请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。

# 1、先举一个例子，给一个4行4列的list

L1 = [1,2,8,9]
L2 = [2,3,9,12]
L3 = [4,7,10,13]
L4 = [6,8,11,15]

# 给一个4行4列的list
L5 = [L1,L2,L3,L4]

# print(len(L5))

第一种方法:
Step-wise线性搜索解法：
每次搜索值从右上角的值比较，如果大于右上角的值，则直接去除一行，否则去掉1列。


def find(lst, num):
	# 先判断是否为空列表
	if lst is None:
		return None

	# 求出几列几行的列表
	# m列
	m = len(lst)
	# n行
	n = len(lst[0])
	
	# 从第一行的最后一列开始
	row = 0
	col = n - 1

	while row < m and col >= 0:
		# 如果小于第一行最后一列的值，列加1
		if num < lst[row][col]:
			col = col - 1
		# 否则行加1
		elif num > lst[row][col]:
			row = row + 1
		else:
			return True
	return False
	
	

print(find(L5, 13))