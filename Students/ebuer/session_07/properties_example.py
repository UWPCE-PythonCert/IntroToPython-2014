#!/usr/bin/env python

"""
Example code for properties

NOTE: if your getters and setters are this simple: don't do this!

"""


class C(object):
    def __init_(self):
        self._x = None
    @property
    def x(self):
        return self._x
    @x.setter
    def x(self, value):
        self._x = value
    @x.deleter
    def x(self):
        del self._x

"""
Note: if the deleter was not there, trying to execute a delete of the attribute (del attribute) would generate an attribute error

Eliminate the setter and the attribute becomes read only
"""

if __name__ == "__main__":
    c = C()
    c.x = 5
    print c.x

