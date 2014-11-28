#!/usr/bin/env python

"""
circle class -- 

basic skeleton: fill in with properties..

Write a Circle class with decorator syntax for properties:
  instantiate with a radius: c = Circle(4)

Use a property for the diameter: get and settable:
    d = c.diameter
    c.diameter = 5

use a property for the area: only gettable
    a = c.area
    a.area = 5 => AttributeError
 
add methods so that str(circle) and repr(circle)
    produce something reasonable.

extra credit: make it so you can add two circles:

>>> Circle(2) + Circle(3)
Circle(5.000000)


see test_circle_properties.py for requirements.

"""

import math

class Circle(object):
    def __init__(self, radius):
        self.radius = radius

    # put the rest in here...