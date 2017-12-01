# 1. 你首先说出三个不同的特殊数，要求必须是个位数，比如3、5、7。
# 2. 让所有学生拍成一队，然后按顺序报数。

# 3. 学生报数时，
# 如果所报数字是第一个特殊数（3）的倍数，那么不能说该数字，而要说Fizz；
# 如果所报数字是第二个特殊数（5）的倍数，那么要说Buzz；
# 如果所报数字是第三个特殊数（7）的倍数，那么要说Whizz。

# 4. 学生报数时，如果所报数字同时是两个特殊数的倍数情况下，也要特殊处理，
# 比如第一个特殊数和第二个特殊数的倍数，那么不能说该数字，而是要说FizzBuzz, 以此类推。
# 如果同时是三个特殊数的倍数，那么要说FizzBuzzWhizz。

# 5. 学生报数时，如果所报数字包含了第一个特殊数，那么也不能说该数字，而是要说相应的单词，
# 比如本例中第一个特殊数是3，那么要报13的同学应该说Fizz。
# 如果数字中包含了第一个特殊数，那么忽略规则3和规则4，比如要报35的同学只报Fizz，不报BuzzWhizz。

# 方法1：
# def check(a, dic, d):
# 	answer = ''

# 	# 如果数字中包含这三个数字，就输出
# 	if str(a) in str(d):
# 		return dic[a]
	
# 	# 从字典中读出key值
# 	for x in dic.keys():
# 		# 判断如果数字除以key的值余数为0时，说明是这三个数的倍数
# 		if not (d % x):
# 			# 就需在在answer上加入key对应的value
# 			answer = answer + dic[x]

# 	# 如果answer为空，返回原数字
# 	if not answer:
# 		return d
# 	# 不然就返回answer	
# 	return answer

# # 第一步输入三个数
# a = int(input('first number:'))
# b = int(input('second number:'))
# c = int(input('third number:'))

# # 用字典接收这三个数字：
# dic = {a:'Fizz', b:'Buzz', c:'Whizz'}

# for x in range(1, 101):
# 	print(check(a, dic, x))


# # 方法2：
# ['Fizz'[(str(3)not in str(i)) * 4:] or 'Fizz'[i % 3 * 5:] + 'Buzz'[i % 5 * 5:] + 'Whizz'[i % 7 * 5:] or i for i in range(1, 101)]


a = 0
b = 20

# if a or b:
# 	print(a)
# else:
# 	print(b)

print(cmp(a,b))

choice(seq)
# 从序列中随机挑选一个元素
random.choice(range(10))

uniform(x,y)
# 随机生成下一个实数，在(x,y)范围内。