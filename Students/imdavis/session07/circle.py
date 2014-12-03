#!/usr/bin/env python2.7

"""
Circle class
"""

from math import pi

class Circle(object):
    def __init__(self, radius):
        self.radius = float(radius)

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, radius):
        if radius <= 0:
            raise ValueError("radius must be nonzero and non-negative")
        else:
            self.__radius = radius

    @classmethod
    def from_diameter(cls, diameter):
        if diameter <= 0:
            raise ValueError("diameter must be nonzero and non-negative")
        else:
            return cls(diameter / 2.0)

    @property
    def diameter(self):
        return self.radius * 2.0

    @diameter.setter
    def diameter(self, value):
        if value <= 0:
            raise ValueError("diameter must be nonzero and non-negative")
        else:
            self.radius = value / 2.0

    @property
    def area(self):
        return self.radius**2 * pi

    def __repr__(self):
        return "Circle({})".format(self.radius)

    def __str__(self):
        return "Circle with radius {}".format(self.radius)

    def __add__(self, c):
        return Circle(self.radius + c.radius)

    def __mul__(self, c):
        """
        Make sure we can multiply two Circle objects or a number and a 
        Circle object.  In the case of multiplying a Circle object and a
        number, this function will only be able to handle something 
        like:
            c = Circle(2.34)
            c * 1.234
        Need to define __rmul__ special method (below) for swapped 
        operands.
        """
        if isinstance(c, Circle):
            return Circle(self.radius * c.radius)
        else:
            return Circle(c * self.radius)

    def __rmul__(self, c):
        """
        Be able to multiply a number and an existing Circle object, with
        swapped operands. i.e.
            c = Circle(2.34)
            1.234 * c
        """
        return Circle(c * self.radius)

    def __gt__(self, c):
        if (self.radius > c.radius):
            return True
        else:
            return False

    def __lt__(self, c):
        if (self.radius < c.radius):
            return True
        else:
            return False

    def __eq__(self, c):
        if (self.radius == c.radius):
            return True
        else:
            return False

    def __ne__(self, c):
        if (self.radius != c.radius):
            return True
        else:
            return False

    def __iadd__(self, c):
        return Circle(self.radius + c.radius)



if __name__ == '__main__':
    circles = [Circle(6), Circle(7), Circle(2.34), Circle(1.234), 
               Circle(12.15), Circle(0.24), Circle(4.23), Circle(1.999),
               Circle(2.0001), Circle(99), Circle(14.112)]
    print circles
    circles.sort()
    print circles