#!/usr/bin/env python

"""
Example code for properties

NOTE: if your getters and setters are this simple: don't do this!

"""


class C:
    def __init__(self):
        self._x = None
    @property
    def x(self):
        print("in getter")
        return self._x
    @x.setter
    def x(self, value):
        print("in setter", value)
        self._x = value
    @x.deleter
    def x(self):
        del self._x

if __name__ == "__main__":
    c = C()
    c.x = 5
    print(c.x)

