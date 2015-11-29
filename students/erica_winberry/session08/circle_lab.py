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


