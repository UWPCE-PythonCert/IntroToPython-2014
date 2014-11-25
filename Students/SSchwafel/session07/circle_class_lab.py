#!/usr/bin/python
from math import pi

class Circle(object):
    def __init__(self, radius):
        self.radius = float(radius)
    
    @classmethod
    def from_diameter(cls, diameter):
        
        return cls(diameter/2.0)
        
    def __add__(self, other):

        return Circle(self.radius + other.radius)

    def __mul__(self, other):
        try:
    
            return Circle(self.radius * other.radius)
        except AttributeError:

            return Circle(self.radius * other)

    __rmul__ = __mul__

    def __lt__(self, other):

         return self.radius < other.radius

    def __gt__(self, other):

         return self.radius > other.radius

    def __eq__(self, other):

         return self.radius == other.radius
    
    @property
    def diameter(self):
        return self.radius*2.0
    @diameter.setter
    def diameter(self, value):
        self.radius = value/2.0
    @property
    def area(self):
        return self.radius**2*pi
    def __repr__(self):
	return "Circle{}".format(self.radius)
     
c = Circle(4)
c2 = Circle(5)

print c.radius
print c.diameter
print c.area
#print c.__repr__

print c + c2
print c2 * 2
print 2 * c2
print c2 < c2

print c2 * c2
