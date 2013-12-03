#!/usr/bin/env python

"""
example code for properties using the decorator syntax
"""

class C(object):
    _x = None
    @property
    def x(self):
        return self._x
    @x.setter
    def x(self, value):
        self._x = value
    @x.deleter    
    def x(self):
        del (self._x)

if __name__ == "__main__":
    c = C()
    c.x = 5
    print c.x
    c.x = 7
    print c.x
    del c.x
    print c.x
