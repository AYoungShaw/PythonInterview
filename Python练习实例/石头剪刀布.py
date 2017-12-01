# 最好的算法是尽量少用if语句

# 用户输入一个选项，然后计算机随机一个选项，然后判断输赢

# import random

# guess_list = ['石头', '剪刀', '布']

# win_combination = [['布', '石头'], ['石头', '剪刀'], ['剪刀', '布']]


# while True:
# 	computer = random.choice(guess_list)

# 	people = input('请输入: 剪刀石头布\n').strip()

# 	if people not in guess_list:
# 		continue
# 	elif computer == people:
# 		print('平手， 再玩一次')
# 	elif [computer, people] in win_combination:
# 		print('电脑获胜，再玩一次， 人获胜才能退出')
# 	else:
# 		print('人胜')
# 		break






list1 = [3,7,8,9,12]


list2 = [5,6,10,13,25,30]

for i in list1:
	list2.append(i)

list3 = sorted(list2)

print(list3)