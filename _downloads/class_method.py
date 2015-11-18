#!/usr/bin/env python

"""
example of a class method
"""


class C:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @classmethod
    def a_class_method(cls, y):
        print("in a_class_method", cls)
        return cls(y, y**2)


class C2(C):
    pass


if __name__ == "__main__":

    c = C(3, 4)
    print(type(c), c.x, c.y)

    c2 = C.a_class_method(3)
    print(type(c2), c2.x, c2.y)

    c3 = c2.a_class_method(2)
    print(type(c3), c3.x, c3.y)
