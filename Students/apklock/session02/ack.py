def ack(m,n): # m and n are integers in between 0 and 4
	if m<0 or n<0:
		return 'None'
	elif m is 0:
		return n+1
	elif m>0 and n is 0:
		return ack(m-1,1)
	elif m>0 and n>0:
		return ack(m-1, ack(m, n-1))
