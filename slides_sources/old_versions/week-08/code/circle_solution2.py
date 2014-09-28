#!/usr/bin/env python

"""
circle class -- my solution to the second part of the exercise

test code to run it is in test_circle2.py
"""

import math

class Circle(object):
    def __init__(self, radius):
        self.radius = radius

    def _get_d(self):
        return self.radius * 2
    def _set_d(self, d):
        self.radius = d / 2.0
    diameter = property(_get_d, _set_d, doc="The diameter of the circle")

    def _get_area(self):
        return math.pi * self.radius**2
    area = property(_get_area, doc="The area of the circle")

    # alternate constructor that takes diameter
    def from_diameter(klass, d):
        return klass(d / 2.0)
    from_diameter = classmethod(from_diameter)

    ## The magic methods:
    def __str__(self):
        return "Circle with radius: %f"%self.radius

    def __repr__(self):
        return "Circle(%s)"%self.radius

    def __add__(self, other):
        return Circle(self.radius + other.radius)

    def __mul__(self, factor):
        return Circle(self.radius * factor)

    ## comparisons
    def __eq__(self, other):
        return self.radius == other.radius
    def __ne__(self, other):
        return self.radius != other.radius
    def __gt__(self, other):
        return self.radius > other.radius
    def __ge__(self, other):
        return self.radius >= other.radius
    def __lt__(self, other):
        return self.radius < other.radius
    def __le__(self, other):
        return self.radius <= other.radius

    # ## or, in this simple case:
    # def __cmp__(self, other):
    #     return cmp(self.radius, other.radius)
