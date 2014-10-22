def grid_n(n): #n rows & columns
	a = ' + ----'
	b = ' |     '
	for i in range(n):
		print a * n, '+'
		print b * n, '|'
		print b * n, '|'
		print b * n, '|'
		print b * n, '|'
	print a * n, '+'