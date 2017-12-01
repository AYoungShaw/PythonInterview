# 解题思路：
# 先把第一个取出来，然后拿后面的元素跟第一个递归对比
# 小的放在第一个元素的前面，大的放在第一个元素的后面
# def qsort(seq):
# 	if seq == []:
# 		return []
# 	else:
# 		pivot = seq[0]
# 		# 递归将小于pivot的放在前面
# 		lesser = qsort([x for x in seq[1:] if x < pivot])
# 		# 递归把大于pivot的放后面
# 		greater = qsort([x for x in seq[1:] if x >= pivot])
# 		return lesser + [pivot] + greater

# seq = [5,6,7,3,7,34,67,32,67,45,56,343]
# 从索引为1开始取。
# seq[1:]
# print(seq[1:])

# print(qsort(seq))


