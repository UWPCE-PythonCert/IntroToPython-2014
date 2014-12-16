#!/usr/bin/env python

"""
examples of static and class methods
"""

class C(object):

    def a_static_method(a, b):
        print "in a_static_method"
        return a+b
    a_static_method = staticmethod(a_static_method)

    def test(self):
        return self.a_static_method(2,3)

if __name__ == "__main__":

    print C.a_static_method(3,4)

    c = C()

    print c.a_static_method(4,5)
