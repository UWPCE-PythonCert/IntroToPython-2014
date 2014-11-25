'''

Defines Circle Class.

'''

from math import pi

class Circle (object):
    '''
    Defines methods and attributes that apply to a circle.
    '''
    def __init__(self, radius):
        self.radius = radius
    
    @property
    def diameter(self):
        return self.radius * 2.
        
    @diameter.setter
    def diameter (self, val):
        self.radius = val//2.
        
    def area (self):
        return self.radius*self.radius * pi 