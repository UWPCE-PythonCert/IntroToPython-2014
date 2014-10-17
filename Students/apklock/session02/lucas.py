def lucas(n): # return Lucas series to the 'nth' values
	if n == 1:
		return 2
	elif n == 2:
		return 1
	else:
		return lucas(n-2) + lucas(n-1)