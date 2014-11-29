'''

Defines Circle Class.

'''

from math import pi

class Circle (object):
    '''
    Defines methods and attributes that apply to a circle.
    '''
    def __init__(self, radius):
        self.radius = float(radius)
    
    @property
    def diameter(self):
        return self.radius * 2.
        
    @diameter.setter
    def diameter (self, val):
        self.radius = val/2.
        
    def area(self):
        '''
        Calculate the area of this circle
        '''
        return self.radius*self.radius * pi 
        
    @classmethod
    def from_diameter(cls, diameter):
        return cls(diameter/2.)
        
    def __repr__(self):
        return 'Circle.Circle({})'.format(self.radius)
        
    def __str__(self):
        return 'Circle wih radius {}'.format(self.radius)
 
    def __add__(self, other):
        if isinstance(other, Circle):
            return Circle (self.radius + other.radius)
        else:
            self.radius += other
            return self
    
    def __mul__(self, other):
        if isinstance(other, Circle):
            return Circle (self.radius * other.radius)
        else:
            self.radius *= other
            return self
            
    def __rmul__(self, other):
        self.radius *= other
        return self
        
    def __gt__(self, other):
        return self.radius > other.radius
        
    def __lt__(self, other):
        return self.radius < other.radius
        
    def __eq__(self, other):
        return self.radius == other.radius