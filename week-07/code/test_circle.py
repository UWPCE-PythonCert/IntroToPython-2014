#!/usr/bin/env python

"""
code that tests the circle class defined in circle.py

can be run with py.test
"""

import math

from circle import Circle
#from circle_solution import Circle

def test_create():
	c = Circle(4)

	assert c.radius == 4

def test_change_radius():
	c = Circle(3)
	c.radius = 4

	assert c.radius == 4
    
def test_area():
	c = Circle(4)

	assert c.get_area() == math.pi * 16

def test_area2():
	"""
	area should change if radius changes 
	"""
	c = Circle(4)

	c.radius = 2

	assert c.get_area() == math.pi * 4


def test_str():
	c = Circle(2)

	print str(c)

	assert str(c) == 'Circle Object with radius: 2.000000'

def test_repr():
	c = Circle(3)

	assert repr(c) == 'Circle(3.000000)'

def test_change_radius():
	c = Circle(3)

	assert repr(c) == 'Circle(3.000000)'

def test_add():
	"""
	see if you can add two circles together
	"""

	c1 = Circle(2)
	c2 = Circle(4)

	c3 = c1+c2 

	assert c3.radius == 6
	assert c3.get_area() == math.pi * 36


