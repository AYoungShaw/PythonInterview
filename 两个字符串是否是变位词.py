class Anagram:
	# s1: first  string
	# s2: second string
	# return true of false
	def Solution1(s1, s2):
		alist = list(s2)

		post1 = 0
		stillOK = True

		while post1 < len(s1) and stillOK:
			post2 = 0
			found = False
			while post2 < len(alist) and not found:
				if s1[post1] == alist[post2]:
					found = True
				else:
					post2 = post2 + 1

			if found:
				alist[post2] = None
			else:
				stillOK = False

			post1 = post1 + 1

		return stillOK

	print(Solution1('abcd', 'dcba'))

	# 方法2：
	# 先排序再进行比较
	def Solution2(s1, s2):
		alist1 = list(s1)
		alist2 = list(s2)
		
		# 先排序
		alist1.sort()
		alist2.sort()

		pos = 0
		matches = True

		while pos < len(alist1) and matches:
			if alist1[pos] == alist2[pos]:
				pos += 1
			else:
				matches = False

		return matches

	print(Solution2('abc', 'cba'))

	# 方法3：
	def Solution3(s1, s2):
		c1 = [0]*26
		c2 = [0]*26

		for i in range(len(s1)):
			pos = ord(s1[i]) - ord('a')
			c1[pos] = c1[pos] + 1

		for i in range(len(s2)):
			pos = ord(s2[i]) - ord('a')
			c2[pos] = c2[pos] + 1

		j = 0
		stillOK = True
		while j < 26 and stillOK:
			if c1[j] == c2[j]:
				j = j + 1
			else:
				stillOK = False

		return stillOK

	print(Solution3('apple', 'pleap'))