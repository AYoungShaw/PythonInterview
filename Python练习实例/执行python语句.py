dashes = '\n' + '-'*50
exec_dict = {
	'f':''' 	#for loop
	for %s in %s:
		print(%s)
''',
	's': ''' 	# sequence while loop
	%s = 0
	%s = %s
	while %s < len(%s):
		print(%s[%s])
		%s = %s + 1
	''',
	'n': '''	# counting while loop
	%s = %d
	while %s < %d:
		print(%s)
		%s = %s + %d
	'''
}

def main():
	Itype = input('Loop type?(For/While):')
	dtype = input('Data type?(Number/Sequence):')

	if dtype == 'n':
		start = input('Starting value:')
		stop = input('Ending value(non-inclusive):')
		step = input('Stepping value?：')
		seq = str(range(start, stop, step))
	
	else:
		seq = input('Enter sequence:')

	var = input('Iterative variable name?：')

	if Itype == 'f':
		exec_str = exec_dict['f'] %(var, seq, var)

	elif Itype == 'w':
		if dtype == 's':
			svar = input('Enter sequence name?：')
			exec_str = exec_dict['s'] % (var, svar, seq, var, svar, svar, var, var, var)
		elif dtype == 'n':
			exec_str = exec_dict['n'] % (var, start, var, stop, var, var, var, step)

	print(dashes)
	print('The custom-generated code for you is :' + dashes)
	print(exec_str + dashes)
	print('The execution of the code:' + dashes)
	exec(exec_str)
	print(dashes)

if __name__ == '__main__':
	main()