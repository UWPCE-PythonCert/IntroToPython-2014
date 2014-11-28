def grid_nx(n,x): #n rows, x columns
	a = ' + ----'
	b = ' |     '
	for i in range(n):
		print a * x, '+'
		print b * x, '|'
		print b * x, '|'
		print b * x, '|'
		print b * x, '|'
	print a * x, '+'