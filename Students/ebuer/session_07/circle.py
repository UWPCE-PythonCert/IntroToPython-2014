
"""
circle.py
"""

from math import pi
import functools  # imported to access @total_ordering


@functools.total_ordering
class Circle(object):

    def __init__(self, radius):
        self.radius = float(radius)
        # self.diameter = self.radius * 2 # example of static attribute, let's not store it just calculate it on the fly when asked for

    @classmethod
    # Step 5 -- alternate constructor for circle using diameter
    def from_diameter(cls, diameter): # note cls is the instance of the class variable (cls is the conventional name like 'self')
        return cls(diameter / 2.0)  # cls is the class object, given a value it creates a class instance

    @property #this is actually a getter, get diameter when called
    def diameter(self):
        return self.radius * 2.0

    @diameter.setter
    def diameter(self, value):
        self.radius = value / 2.0

    @property  # here we set class properties, is more than one decorator needed?
    def area(self):
        """calculates area, circle property not mutable by user"""
        return self.radius  ** 2 * pi

    # Step 6, add __str__ and __repr__ to circle class
    def __repr__(self):
        return "Circle(%s)" %self.radius  #  note __repr__ is sort of an inverse of the function

    def __str__(self):
        return 'Circle with radius: %.2f' % self.radius

    # Add some numeric protocol to the circle class
    def __add__(self, c):
        """adds two circle radii together, returns new circle"""
        return Circle(self.radius + c.radius)

    def __mul__(self, n):
        """multiplies circle radius times n, returns new circle"""
        return Circle(self.radius * n)

    """ define the rich comparison operators, then use
        functools.total_ordering to autogen the rest"""
    def __eq__(self, c):
        """defines equal to property"""
        return (self.radius == c.radius)

    def  __lt__(self, c):
        """defines less than property"""
        return(self.radius < c.radius)

    # reflected operation multiplication
    def __rmul__(self, n):
        """reflected multiplication"""
        return self.__mul__(n)

    """functools.total_ordering already created assignment operators
        but let's create at least one"""

    def __iadd__(self, c):
        self.radius = self.radius + c.radius
        return Circle(self.radius)

    # similar operation for assignment multiplication: Circle(sr = sr * cr)

# subclassing from Circle is easy!
class SubCircle(Circle):  # subclass of circle
    pass
