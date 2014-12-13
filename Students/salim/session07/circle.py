#!usr/local/bin/python

from math import pi


class Circle(object):
    """Generic Circle class."""

    def __init__(self, radius):
        self.radius = radius

    @property
    def diameter(self):
        return self.radius * 2.0

    @diameter.setter
    def diameter(self, value):
        self.radius = value / 2.0

    @property
    def area(self):
        return pi * self.radius ** 2

    @classmethod
    def from_diameter(cls, diameter):
        return cls(diameter / 2.0)

    def __str__(self):
        return 'Circle with radius: {:.2f}'.format(self.radius)

    def __repr__(self):
        return 'Circle({})'.format(self.radius)

    def __add__(self, other):
        return Circle(self.radius + other.radius)

    def __mul__(self, other):
        return Circle(self.radius * other)

    def __rmul__(self, other):
        return Circle(self.radius * other)

    def __cmp__(self, other):
        result = float(self.radius) - float(other.radius)
        return -1 if result < 0 else 1 if result > 0 else 0
