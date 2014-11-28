#!/usr/bin/env python

"""
nifty Circle class
"""

from math import pi


class Circle(object):

    def __init__(self, radius):
        self.radius = float(radius)

    @classmethod
    def from_diameter(cls, diameter):
        return cls(diameter/2.0)

    @property
    def diameter(self):
        return self.radius * 2.0
    @diameter.setter
    def diameter(self, value):
        self.radius = value / 2.0

    @property
    def area(self):
        return self.radius**2 * pi

    def __repr__(self):
        return "Circle(%s)"%self.radius

    def __str__(self):
        return "Circle with radius: %.4f"%self.radius

    def __add__(self, other):
        return Circle(self.radius + other.radius)

    def __iadd__(self, other):
        """
        for "augmented assignment" -- can be used for in-place addition

        generally used that way for mutable types. This approach returns
        self, so that the object is changed in place.
        """
        self.radius += other.radius
        return self

    def __mul__(self, factor):
        return Circle(self.radius * factor)

    def __imul__(self, factor):
        self.radius *= factor
        return self

    def __rmul__(self, factor):
        return Circle(self.radius * factor)

    def __cmp__(self, other):
        return cmp(self.radius, other.radius)


class SubCircle(Circle):
    pass

