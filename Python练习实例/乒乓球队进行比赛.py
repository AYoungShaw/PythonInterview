题目：两个乒乓球队进行比赛，各出三人。甲队为a,b,c三人，乙队为x,y,z三人。已抽签决定比赛名单。
有人向队员打听比赛的名单。a说他不和x比，c说他不和x,z比，请编程序找出三队赛手的名单。

这题的思路是：
	先将三个循环中两两相同的都去除掉，这样就九种情况，
	这九种情况就是把两队所对应的人员都打印出来了。
	最后再进行条件判断，得到需要对应的匹配信息

# for  i in range(ord('x'), ord('z') + 1):
# 	for j in range(ord('x'), ord('z') + 1):
# 		if i != j:  #去掉两两相同
# 			print('%s  ----- %s ' %(i ,j))
# 			for k in range(ord('x'), ord('z') + 1):
# 				if (i != k) and (j != k):  #去掉 三者都相同
# 					# print(' %s ---- %s ---- %s' %(i, j, k))
# 					pass
# 					if i != ord('x') and (k != ord('x')) and (k != ord('z')):
# 						print('order a ----> %s \t b ----> %s \t c--->%s' %(chr(i), chr(j), chr(k)))





















