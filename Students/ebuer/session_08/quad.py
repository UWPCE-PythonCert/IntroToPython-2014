

"""
my_quad = Quadratic(a=2, b=3, c=1)
y=ax**2+b*x+c
    
my_array = SparseArray((1,0,0,0,2,0,0,0,5))
"""

class Quadratic(object):

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __call__(self, x):
        return self.a*x**2+self.b*x+self.c


