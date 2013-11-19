#!/usr/bin/env python

"""
circle class -- my solution to the firt part of the exercise

test code to run it is in test_circle1.py
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


