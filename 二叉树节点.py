class Node(object):
	def __init__(self, data, left=None, right=None):
		self.data = data
		self.left = left
		self.right = right

tree = Node(1, Node(3, Node(7, Node(0)), Node(6)), Node(2, Node(5), Node(4)))
#        1
#      /   \
#     3     2
#    / \   / \
#   7   6 5   4
#  /
# 0

# 层次遍历：
def lookup(root):
	stack = [root]
	while stack:
		# 移除列表中的一个值，并返回该值
		current = stack.pop(0)
		print(current.data)
		if current.left:
			stack.append(current.left)
		if current.right:
			stack.append(current.right)
# lookup(tree)

# 深度遍历
def deep(root):
	if not root:
		return
	print(root.data)
	deep(root.left)
	deep(root.right)

deep(tree)



