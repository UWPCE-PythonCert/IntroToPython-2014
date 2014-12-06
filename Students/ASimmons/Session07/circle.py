__author__ = 'Ari'


## ALWAYS INHERIT FROM OBJECT

## radius is a REQUIRED parameter

## the resulting circle should have an attribute

## since we don't want to have radius
## and diameter be two seperate things
## we are doing to 'get' the diameter
## from the radius (a getter)

## create an alternate constructor
## so that you can define the Circle
## using a diameter

## add __str__ and __repr__ methods to your circle class

import math
import functools

@functools.total_ordering
class Circle(object):
    def __init__(self, radius):
        self.radius = int(radius)

    # alternate constructor - need a class method
    @classmethod
    def from_diameter(cls, diameter):
        # how to create an instance of the cicle class
        # use the cls - which is the class object Circle() itself
        return cls(diameter/2.0)

    @property
    def diameter(self):
        return self.radius * 2.0

    @diameter.setter
    def diameter(self, value):
        return self.radius == value / 2.0

    @property
    def area(self):
        return self.radius**2 * math.pi

    def __repr__(self):
        return "Circle(%s)"%self.radius

    def __str__(self):
        return "Circle with radius: %4f"%self.radius

    def __add__(self, other):
        return Circle(self.radius + other.radius)

    def __iadd__(self, other):
        """
        can be used for 'in place' addition

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

    def __eq__(self, other):
        return self.radius == other.radius

    def __gt__(self, other):
        return self.radius > other.radius

class SubCircle(Circle):
    pass

