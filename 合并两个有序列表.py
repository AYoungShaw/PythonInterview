
1、尾递归
尾递归的效率也不是那么高，预防爆栈

递归判断第一个元素谁大，小的就插入进去，并删除这个元素，然后再判断第一个元素

def _recursion_merge_sort2(l1, l2, tmp):
	if len(l1) == 0 or len(l2) == 0:
		tmp.extend(l1)
		tmp.extend(l2)
		return tmp
	else:
		if l1[0] < l2[0]:
			tmp.append(l1[0])
			del l1[0]
		else:
			tmp.append(l2[0])
			del l2[0]
		return _recursion_merge_sort2(l1, l2, tmp)

def recursion_merge_sort2(l1, l2):
	return _recursion_merge_sort2(l1, l2, [])

l1=[2,3,5,6,1,7]
l2=[4,8,10,9,2]
print(recursion_merge_sort2(l1, l2))

====================================================================
第二种方法:
循环算法

定义一个新列表
比较两个列表的首元素
小的就插入到新列表中
将已经插入的删除从旧列表中删除
判断如果有一个列表为空，就将旧列表插入到新列表中

def recursion_merge_sort3(l1, l2):
	tmp = []
	while len(l1) > 0 and len(l2) > 0:
		if l1[0] < l2[0]:
			tmp.append(l1[0])
			del l1[0]
		else:
			tmp.append(l2[0])
			del l2[0]

	tmp.extend(l1)
	tmp.extend(l2)

	return tmp

l1=[2,35,5,23,54,23]
l2=[4,42,54,12,43,2]

print(recursion_merge_sort3(l1, l2))
======================================================================
