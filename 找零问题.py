def coinChange(values, money, coinsUsed):
	# values T[1:n]数组
	# valuesCounts 钱币对应的种类数
	# money 找出来的总钱数
	# coinsUsed 对应的钱币总数i所使用的硬币数目
	for cents in range(1, money+1):
		minCoins = cents
		for value in values:
			if value <= cents:
				temp = coinsUsed[cents - value] + 1
				if temp < minCoins:
					minCoins = temp
		coinsUsed[cents] = minCoins
		print('面值：{0} 的最小硬币数目为：{1}'.format(cents, coinsUsed[cents]))

values = [25, 21, 10, 5, 1]
money = 63
coinsUsed = {i:0 for i in range(money+1)}
# print(coinsUsed)
coinChange(values, money, coinsUsed)