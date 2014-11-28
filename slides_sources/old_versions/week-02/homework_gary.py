#!/usr/bin/env python

"""
Gary's solution to the ackerman function

The only one that is not recursive.

However, it still can't compute ack(m,n) for m,n > 3,4
   ... at least not in a reasonable time and memory
"""


def ack(m,n):
	
	# s is the stack to track
	s=[m, n]
	t = 1
	while True:
		if s[t-1] == 0: # m = 0
			t = t - 1
			s[t] = s[t + 1] + 1 # A (m,n) = n + 1
		elif s[t] == 0: # n = 0
			s[t] = 1
			s[t-1] = s[t-1] - 1 # A (m,n) = A (m-1, 1)
		else:
			s.insert(t + 1, s[t] - 1) # n-1 in A(m,n-1)
			s[t] = s[t - 1]     # m in A(m,n-1)
			s[t - 1] = s[t - 1] - 1 # m-1 in A(m-1, A(m, n-1))
			t = t + 1 # Try to calculated A (m, n-1)
		if not t:
			break
	print "ack(%d,%d) = %d"%(m,n,s[0])

ack(2, 3)
#ack(3, 4)

