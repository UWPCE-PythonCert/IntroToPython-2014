'''
Created on Nov 18, 2014

@author: Aleksey
'''

from math import pi
from numbers import Number

class Circle(object):
    def __init__(self, the_radius):
        self._radius = float(the_radius)
        
    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, value):
        self._radius = value
    
    @property
    def diameter(self):
        return self._radius * 2.0
    
    @diameter.setter
    def diameter(self, value):
        self._radius = value / 2.0
    
    @property
    def area(self):
        return pi * self._radius**2.0
    
    @classmethod
    def from_diameter(cls, diam):
        return cls(diam / 2.0)

    def __str__(self):
        return "Circle with radius: %s" % self.radius
    
    def __repr__(self):
        return "Circle(%s)" % self.radius
    
    def __add__(self, cls):
        if isinstance(cls, Circle):
            self.radius = self.radius + cls.radius
        return self.radius
    
    def __mul__(self, num):
        self.radius = self.radius * num
        return self.radius
    
    def __eq__(self, other):
        if isinstance(other, Circle):
            return self.radius == other.radius
    
    def __lt__(self,other):
        if isinstance(other, Circle):
            return(self.radius < other.radius)

    def __gt__(self,other):
        if isinstance(other, Circle):
            return(self.radius > other.radius)

    def __radd__(self, other):
        if isinstance(other, Number):
            self.radius = self.radius + other
    
    def __rmul__(self, other):
        if isinstance(other, Number):
            self.radius = self.radius * other
                
    def __iadd__(self, other):
        if isinstance(other, Number):
            self.radius += other
        
    def __imul__(self, other):
        if isinstance(other, Number):
            self.radius *= other
    
if __name__ == "__main__":
    c = Circle(4)
    print c.radius
    print c.diameter
    print c.area
    print
    
    c = Circle.from_diameter(13)
    print c.radius
    print c.diameter
    print c.area
    print
    
    c1 = Circle(4)
    c2 = Circle(8)
    print c1 + c2
    print
    
    print c2 * 3
    print
    
    c = Circle(4)
    print c
    print
    
    print repr(c)
    d = eval(repr(c))
    print d
    print
    
    circles = [Circle(6), Circle(7), Circle(8), Circle(4), Circle(0), Circle(2), Circle(3), Circle(5), Circle(9), Circle(1)]
    circles.sort()
    print circles
    
    a_circle = Circle(2)
    print a_circle * 3 == 3 * a_circle