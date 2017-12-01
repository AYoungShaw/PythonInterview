# def find_short(s):
#     # your code here
# 	L1 = s.split()
  
# 	L2 = list(map(lambda x : len(x), L1))
# 	l = min(L2)
# 	return min(L2)
   
    
#     # return  # l: shortest word length

# s = 'sdfs sdfsdfsd dsfssfsdf sdfsfsdfdsdffs'

# length = find_short(s)
# print(length)


class Goods(object):
	def __init__(self):
		# 原价
		self.original_price = 100
		# 折扣
		self.discount = 0.8

	@property
	def price(self):
		# 实际价格
		new_price = self.original_price * self.discount
		return new_price

	@price.setter
	def price(self, value):
		self.original_price = value

	# @price.deltter
	# def price(self, value):
	# 	del self.original_price

obj = Goods()
print(obj.price)
obj.price = 123
print(obj.price)

# del obj.price

print(obj.price)