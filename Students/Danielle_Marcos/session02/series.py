def fibonacci(n):
	"""Return the n value based on the Fibonacci series."""
	if n <= 0:
		return 0
	elif n == 1:
		return 1
	else:
		return fibonacci(n-1) + fibonacci(n-2)

def lucas(n):
	"""Return the n value in the Lucas Numbers."""
	if n <= 0:
		return 2
	elif n == 1:
		return 1
	else:
		return lucas(n-1) + lucas(n-2)

def sum_series(n, x=0, y=1):
	if n <= 0:
		return x
	elif n == 1:
		return y
	else:
		return sum_series(n-1, x, y) + sum_series(n-2, x, y)

if __name__ == "__main__":
	"""Validate that when an nth values are passed different positions are returned"""
	
# Validate Fibonacci tests pass successfully. 
	assert fibonacci(0) == 0
	assert fibonacci(1) == 1
	assert fibonacci(2) == 1
	assert fibonacci(3) == 2
	assert fibonacci(4) == 3
	assert fibonacci(5) == 5
	assert fibonacci(6) == 8
	assert fibonacci(7) == 13

# Validate Lucas tests pass successfully. 

	assert lucas(0) == 2
	assert lucas(1) == 1
	assert lucas(2) == 3
	assert lucas(3) == 4
	assert lucas(4) == 7
	assert lucas(5) == 11
	assert lucas(6) == 18
	assert lucas(7) == 29

# Validate sum_series tests for Fibonacci pass successfully. 

	assert sum_series(0) == 0
	assert sum_series(1) == 1
	assert sum_series(2) == 1
	assert sum_series(3) == 2
	assert sum_series(4) == 3
	assert sum_series(5) == 5
	assert sum_series(6) == 8
	assert sum_series(7) == 13
	
# Validate sum_series tests for Lucas pass successfully.

	assert sum_series(0) == 0
	assert sum_series(1) == 1
	assert sum_series(2) == 1
	assert sum_series(3) == 2
	assert sum_series(4) == 3
	assert sum_series(5) == 5
	assert sum_series(6) == 8
	assert sum_series(7) == 13
	
	print ""	
	print "All Tests Pass"