from math import pi


class Circle:
    """Defines a circle."""

    def __init__(self, radius):
        self.radius = radius

    @property
    def diameter(self):
        return self.radius * 2

    @diameter.setter
    def diameter(self, value):
        self.radius = value / 2.0

    @property
    def area(self):
        return pi * self.radius ** 2

    @classmethod
    def from_diameter(cls, value):
        return cls(value / 2)

    def __str__(self):
        return "Circle with radius: {:.6f}".format(self.radius)

    def __repr__(self):
        return "Circle({:.0f})".format(self.radius)

    def __add__(self, other):
        new_radius = self.radius + other.radius
        return Circle(new_radius)

    def __sub__(self, other):
        new_radius = self.radius - other.radius
        return Circle(new_radius)

    def __mul__(self, other):
        new_radius = self.radius * other
        return Circle(new_radius)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __eq__(self, other):
        return self.radius == other.radius

    def __lt__(self, other):
        return self.radius < other.radius

    def __gt__(self, other):
        return self.radius > other.radius
