# 生成器：python3 中next变为__next__
# 关键词 yield
# def simpleGen():
# 	yield 1
# 	yield '2--->puhch'


# myG = simpleGen()

# print(myG.__next__())
# print(myG.__next__())
# print(myG.__next__())
# for eachItem in myG:
# 	print(eachItem)

# 除了用next()来获得下个生成的值，用户可以将值送回生成器[send()]
def counter(start_at=0):
	count = start_at
	while True:
		val = (yield count)
		if val is not None:
			count = val
		else:
			count += 1

count = counter(5)
print(count.__next__())

count.send(9)
count.__next__()
count.close()
count.__next__()