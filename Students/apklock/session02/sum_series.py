def sum_series(l,m,n): # return the 'lth' place in the series with starting values of m and n
	if l == 1:
		return m
	if l == 2:
		return n
	return sum_series(l-2,m,n) + sum_series(l-1,m,n)