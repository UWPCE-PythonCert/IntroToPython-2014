#!/usr/bin/env python

"""
Circle class -- my solution to the exercise

Test code to run it is in test_circle.py
"""

import math

class Circle(object):
    def __init__(self, radius):
        self.radius = radius

    @classmethod
    def from_diameter(cls, diameter):
        return cls(diameter/2.0)
    
    @staticmethod
    def circumference(radius):
        return math.pi * 2 * radius

    @property
    def diameter(self):
        return self.radius * 2
    @diameter.setter
    def diameter(self, value):
        self.radius = value / 2.0

    @property
    def area(self):
        return self.radius**2 * math.pi
    
    def __add__(self, other):
        return Circle(self.radius + other.radius)
    
    def __repr__(self):
        return "Circle(%f)"%self.radius

    def __str__(self):
        return "Circle Object with radius: %f"%self.radius

