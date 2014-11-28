#!/usr/bin/env python

"""
tests for the iterator solutions
"""

from iterator_1 import IterateMe_1
from iterator_2_solution import IterateMe_2
from iterator_3_solution import IterateMe_3

def test_1():
	l = []
	for i in IterateMe_1(4):
		l.append(i)	
	print l
	assert l == [0, 1, 2, 3]

def test_3a():
	l = []
	for i in IterateMe_3(1, 4):
		l.append(i)	
	print l
	assert l == [1, 2, 3]

def test_3b():
	l = []
	for i in IterateMe_3(0, 3):
		l.append(i)	
	print l
	assert l == [0, 1, 2]

def test_3c():
	l = []
	for i in IterateMe_3(2, 10, 2):
		l.append(i)	
	print l
	assert l == [2, 4, 6, 8]

def test_3_break():
	"""
	this tests if the iterator re-sets itself when called again.
	"""
	iter = IterateMe_3(2,10,2)

	l = []
	for i in iter:
		l.append(i)	
		if i > 4: break
	print l
	assert l == [2, 4, 6]

	## doing it again should give the same result
	##  i.e. the iterator should reset when it its used again
	l = []
	for i in iter:
		l.append(i)	
		if i > 4: break
	print l
	assert l == [2, 4, 6]


