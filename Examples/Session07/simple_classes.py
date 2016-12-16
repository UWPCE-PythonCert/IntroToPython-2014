#!/usr/bin/env python
"""
simple_classes.py

demonstrating the basics of a class
"""

import math


# create a point class
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# create an instance of that class
p = Point(3, 4)

# access the attributes
print("p.x is:", p.x)
print("p.y is:", p.y)


class Point2:
    size = 4
    color = "red"

    def __init__(self, x, y):
        self.x = x
        self.y = y

p2 = Point2(4, 5)
print(p2.size)
print(p2.color)


class Point3:
    size = 4
    color = "red"

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_color(self):
        return self.color

    def get_size(self):
        return  self.size

class Rect:

    def __init__(self, w, h):
        self.w = w
        self.h = h

    def get_size(self):
        return self.w * self.h


p3 = Point3(4, 5)
print(p3.size)
print(p3.get_color())


class Circle:
    color = "red"
    styles = ['dashed']

    def __init__(self, diameter):
        self.diameter = diameter

    def grow(self, factor=2):
        """
        grows the circle's diameter

        :param factor=2: factor by which to grow the circle
        """
        self.diameter = self.diameter * factor

    def add_style(self, style):
        self.styles.append(style)

    def get_area(self):
        return math.pi * self.diameter / 2.0


class NewCircle(Circle):
    color = "blue"

    def grow(self, factor=2):
        """grows the area by factor..."""
        self.diameter = self.diameter * math.sqrt(2)

nc = NewCircle
print(nc.color)


class CircleR(Circle):
    def __init__(self, radius):
        diameter = radius*2
        Circle.__init__(self, diameter)


class CircleR2(Circle):
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return Circle.get_area(self, self.radius*2)
