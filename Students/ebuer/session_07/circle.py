
"""
circle.py
"""

from math import pi

class Circle(object):

    def __init__(self, radius):
        self.radius = float(radius)
        # self.diameter = self.radius * 2 # example of static attribute, let's not store it just calculate it on the fly when asked for

    @classmethod
    def from_diameter(cls, diameter): # note cls is the instance of the class variable (cls is the conventional name like 'self')
        return cls(diameter / 2.0)  # cls is the class object, given a value it creates a class instance

    @property #this is actually a getter, get diameter when called
    def diameter(self):
        return self.radius * 2.0

    @diameter.setter
    def diameter(self, value):
        self.radius = value / 2.0

    @property  # here we get the area, but do not provide a setter, so user can't get at it
    def area(self):
        return self.radius  ** 2 * pi

    def __repr__(self):
        return "Circle(%s)" %self.radius

class SubCircle(Circle):  # subclass of circle
    pass

