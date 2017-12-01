def binarySearch(l, t):
	low, high = 0, len(l) - 1
	while low < high:
		print(low, high)
		mid = (low + high) // 2
		if l[mid] > t:
			# 把最大值给中间值
			high = mid
		elif l[mid] < t:
			low = mid + 1
		else:
			return mid
	return low if l[low] == t else False

l = [1,5,3,23,5,23,343,23,123]

print(binarySearch(l, 3))