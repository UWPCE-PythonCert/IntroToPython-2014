"""
circle lab
"""
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    @classmethod
    def from_diameter(cls, diameter):
        self = cls(diameter / 2)
        return self

    def __str__(self):
        return "A circle object with radius: {}".format(self.radius)

    def __repr__(self):
        return "Circle({})".format(self.radius)

    @property
    def diameter(self):
        return self.radius * 2
    @diameter.setter
    def diameter(self, val):
        self.radius = val / 2

    @property
    def area(self):
        return self.radius**2 * math.pi

    def __add__(self, other):
        return Circle(self.radius + other.radius)

    def __mul__(self, other):
        return Circle(self.radius * other)

    def __rmul__(self, other):
        return Circle(self.radius * other)


class Sphere(Circle):
    def volume(self):
        return 4/3 * math.pi * self.radius**3

    def area(self):
        raise NotImplementedError("Spheres don't have an area")
