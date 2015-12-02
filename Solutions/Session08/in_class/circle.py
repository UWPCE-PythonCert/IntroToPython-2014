#!/usr/bin/env python3

"""
A nifty Circle class
"""

from math import pi

class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def diameter(self):
        return self.radius*2.0
    @diameter.setter
    def diameter(self, value):
        self.radius = value / 2.0

    @property
    def area(self):
        return pi*self.radius**2

