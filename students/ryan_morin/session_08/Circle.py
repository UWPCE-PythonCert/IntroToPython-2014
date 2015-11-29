__author__ = 'ryan.morin'


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

     @classmethod
     def from_diameter(cls, diameter):
         radius = diameter / 2.0
         return cls(radius)

     def __str__(self):
         return 'Circle with radius: {}'.format(self.radius)

     def __repr__(self):
         return 'Circle({})'.format(self.radius)

     def __add__(self, other):
         total = self.radius + other.radius
         return total

     def __mul__(self, other):
         total = self.radius * other
         return total

     def __lt__(self, other):
         return self.radius < other.radius