def print_grid(n): #n characters wide/tall
	x = (n - 3) / 2
	print '+', x * '-', '+', x * '-', '+'
	for i in range(x):
		print '|', x * ' ', '|', x * ' ', '|'
	print '+', x * '-', '+', x * '-', '+'
	for i in range(x):
		print '|', x * ' ', '|', x * ' ', '|'
	print '+', x * '-', '+', x * '-', '+'