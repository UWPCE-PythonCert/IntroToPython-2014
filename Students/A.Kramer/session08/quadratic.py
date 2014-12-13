'''
Created on Nov 25, 2014

@author: Aleksey
'''

# Quadratic equation
class Quadratic(object):
    def __init__(self, a, b, c):
        self._a = a
        self._b = b
        self._c = c
    
    def __call__(self, x):
        self._x = x
        return self._a * self._x**2 + self._b * self._x + self._c


if __name__ == "__main__":
    q = Quadratic(1,2,3)
    print q(3)