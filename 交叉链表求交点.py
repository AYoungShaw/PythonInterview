# 其实思想可以按照从尾开始比较两个链表，
# 如果相交，则从尾开始必然一致，
# 只要从尾开始比较，直至不一致的地方即为交叉点

# 使用啊a, b 来模拟两个链表
# 可以看到这两个链表从7开始作为交叉点
=======================================================
第一种方法：
a = [1,3,5,2,5,7,1,9,5]
b = [3,4,22,42,7,1,9,5]
# min是求给定序列中最小的一个元素
# for i in range(1, min(len(a), len(b))):
# 	if i == 1 and a[-1] != b[-1]:
# 		print('这个链表无交叉点')
# 		break
# 	else:
# 		if a[-i] != b[-i]:
# 			print('交叉点为：', a[-i+1])
# 			print('从第%s个开始交叉.' % a.index(a[-i+1]))
# 			break
# 		else:
# 			pass

# print(a.index(a[-2]))
======================================================
第二种方法:
构造链表类：
class ListNode:
	def __init__(self, x):
		self.val = x
		self._next = None

def node(l1, l2):
	length1, length2 = 0, 0
	#求链表长度
	while l1._next:
		# 尾节点
		l1 = l1._next
		length1 += 1
	while l2._next:
		l2 = l2._next
		length2 += 1

	#如果相交
	if l1._next == l2._next:
		#长链表的先走
		if length1 > length2:
			for _ in range(length1 - length2):
				l1 = l1._next
			return l1 # 返回交点
		else:
			for _ in range(length2 - length1):
				l2 = l2._next
			return l2
	# 如果不相交
	else:
		return