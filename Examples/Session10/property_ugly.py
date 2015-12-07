#!/usr/bin/env python

class C(object):
    """
    Property defined in about the most ugly way possible
    """
    def __init__(self):
        self._x = None
    def x(self):
        return self._x
    x = property(x)
    def _set_x(self, value):
        self._x = value
    x = x.setter(_set_x)
    def _del_x(self):
        del self._x
    x = x.deleter(_del_x)


