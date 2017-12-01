题目：输入某年某月某日，判断这一天是这一年的第几天？
程序分析：以3月5日为例，应该先把前两个月的加起来，然后再加上5天即本年的第几天，
特殊情况，闰年且输入月份大于2时需考虑多加一天：

p = [31,28,31,30,31,30,31,31,30,31,30,31] #平年
w = [31,29,31,30,31,30,31,31,30,31,30,31] #闰年

year = int(input('输入年：' + '\n'))
month = int(input('输入月份：'+'\n'))
day = int(input('输入日：'+ '\n'))

if year % 100 == 0:
	if year % 400 == 0:
		d = w
	else:
		d = p
else:
	if year % 4 == 0:
		d = w 
	else:
		d = p
days = sum(d[0:month-1]) + day

print('%d年%d月%d日是%d年的第%s天。' %(year, month, day, year, days))
