def series(n): # return Fibonacci series to the 'nth' value
	if n < 2:
		return n
	return series(n-2) + series(n-1)
			