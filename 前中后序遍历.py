# 前中后序遍历
class Node(object):
	def __init__(self, value, left, right):
		self.value = value
		self.left = left
		self.right = right

# 中序遍历
def mid_travelsal(root):
	mid_travelsal(root.left)
	# 访问当前节点
	print(root.value)
	if root.right is not None:
		mid_travelsal(root.right)

# 前序遍历：访问当前节点，遍历左子树，遍历右子树
def pre_travelsal(root):
	print(root.value)
	if root.left is not None:
		pre_travelsal(root.left)
	if root.right is not None:
		pre_travelsal(root.right)

# 后序遍历：遍历左子树，遍历右子树，访问当前节点
def post_travelsal(root):
	if root.left is not None:
		post_travelsal(root.left)
	if root.right is not None:
		post_travelsal(root.right)
	print(root.value)

# 求最大树深
def maxDepth(root):
	if not root:
		return 0
	return max(maxDepth(root.left), maxDepth(root.right)) + 1

# 求两棵树是否相同
def isSameTree(p, q):
	if p == None and q == None:
		return True
	elif p and q:
		return p.val == q.val and isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
	else:
		return False

# 前序中序求后序
def rebuild(pre, center):
	if not pre:
		return 
	cur = Node(pre[0])
	index = center.index(pre[0])
	cur.left = rebuild(pre[i:index + 1], center[:index])
	cur.right = rebuild(pre[index + 1:], center[index + 1:])
	return cur

def deep(root):
	if not root:
		return
	deep(root.left)
	deep(root.right)
	print(root.data)