'''
Eric Rosko
fibonacci.py
Tuesday, Nov. 10, 2015

Description:
	Implementation of fibonacci sequence using TDD

Requirements:
	You must have py.test installed from http://pytest.org
	python3 -m pip install pytest
Usage: 
	py.test -v series.py
	or
	python3 series.py

'''

def fibonacci(n, Lucas=False):
	'''
	Arguments:
	 n = the position in the sequence to return
	 Lucas = choose True to use the Lucas sequence instead of Fibonacci
	
	Returns:
	 the number at n position in the sequence.

	'''

	#default to Fibonacci
	first = 0
	second = 1
	if Lucas:
		first=2
		second=1

	if n == 0:
		return first
	elif n == 1:
		return second
	else:
		previousprevious=first
		previous=second
		current=0
		for i in range(2,n+1):
			print(i, "  ", previousprevious, " ", previous)
			current = (previous+previousprevious)
			previousprevious=previous
			previous = current
		return current


if __name__ == "__main__":
	print(fibonacci(2))


# tests
def test_fibonacci_position_zero():
	assert fibonacci(0) == 0

def test_fibonacci_position_one():
	assert fibonacci(1) == 1

def test_fibonacci_position_two():
	assert fibonacci(2) == 1

def test_fibonacci_position_three():
	assert fibonacci(3) == 2

def test_fibonacci_position_fortytwo():
	assert fibonacci(20) == 6765

def test_fibonacci_position_fortytwo():
	assert fibonacci(42) == 267914296

def test_lucas_position_one():
	assert fibonacci(0, Lucas=True) == 2

def test_lucas_position_two():
	assert fibonacci(1, Lucas=True) == 1

def test_lucas_position_four():
	assert fibonacci(4, Lucas=True) == 7
	