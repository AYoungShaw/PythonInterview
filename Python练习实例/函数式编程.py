# 自己实现filter ， map ， reduce

def filter(bool_func, seq):
	filter_seq = []

	for eachItem in seq:
		if bool_func(eachItem):
			filter_seq.append(eachItem)

	return filter_seq



def map(func, seq):
	mapped_seq = []
	for eachItem in seq:
		mapped_seq.append(func(eachItem))

	return mapped_seq

def reduce(bin_func, seq, init=None):
	lseq = list(seq)

	if init is None:
		res = lseq.pop(0)
	else:
		res = init
	for item in lseq:
		res = bin_func(res, item)
	return res