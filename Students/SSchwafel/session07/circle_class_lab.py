#!/usr/bin/python
from math import pi

class Circle(object):
    def __init__(self, radius):
        self.radius = float(radius)
    
    @classmethod
    def from_diameter(cls, diameter):
        
        return cls(diameter/2.0)
        
    
    
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

print c.radius
print c.diameter
print c.area
print c.__repr__

