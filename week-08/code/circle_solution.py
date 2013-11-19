#!/usr/bin/env python

"""
circle class -- my solution to the exercise

test code to run it is in test_circle.py
"""

import math

class Circle(object):
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return self.radius**2 * math.pi
    
    def __add__(self, other):
        return Circle(self.radius + other.radius)
    
    def __repr__(self):
        return "Circle(%f)"%self.radius

    def __str__(self):
        return "Circle Object with radius: %f"%self.radius

