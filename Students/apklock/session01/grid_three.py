def grid_three(n): #n characters wide/tall
	x = (n - 4) / 3
	print '+', x * '-', '+', x * '-', '+', x * '-', '+'
	for i in range(x):
		print '|', x * ' ', '|', x * ' ', '|', x * ' ', '|'
	print '+', x * '-', '+', x * '-', '+', x * '-', '+'
	for i in range(x):
		print '|', x * ' ', '|', x * ' ', '|', x * ' ', '|'
	print '+', x * '-', '+', x * '-', '+', x * '-', '+'
	for i in range(x):
		print '|', x * ' ', '|', x * ' ', '|', x * ' ', '|'
	print '+', x * '-', '+', x * '-', '+', x * '-', '+'