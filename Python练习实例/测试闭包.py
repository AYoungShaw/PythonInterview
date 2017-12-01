def foo():
	for i in range(5):
		def fn():
			print(i)
	return fn


