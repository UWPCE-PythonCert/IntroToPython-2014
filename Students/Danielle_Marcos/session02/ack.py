def ack (m, n):
	"""Return a value based on the Ackermann-Peter function."""
	
	if m == 0:
		return n + 1
	elif m > 0 and n == 0:
		return ack(m-1, 1)
	elif m > 0 and n > 0:
		return ack(m-1, ack(m, n-1))
	elif m < 0 and n < 0: 
		return None

if __name__ == "__main__":

	assert ack(0,0) == 1
	assert ack(0,1) == 2
	assert ack(0,2) == 3
	assert ack(0,3) == 4
	assert ack(0,4) == 5

	assert ack(1,0) == 2
	assert ack(1,1) == 3
	assert ack(1,2) == 4
	assert ack(1,3) == 5
	assert ack(1,4) == 6

	assert ack(2,0) == 3
	assert ack(2,1) == 5
	assert ack(2,2) == 7
	assert ack(2,3) == 9
	assert ack(2,4) == 11

	assert ack(3,0) == 5
	assert ack(3,1) == 13
	assert ack(3,2) == 29
	assert ack(3,3) == 61
	assert ack(3,4) == 125

	print""
	print "All Tests Pass"