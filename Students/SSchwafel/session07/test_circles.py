#!/usr/bin/python

from circle_class_lab import Circle

def test_area():

    circle1 = Circle(4)
    circle2 = Circle(5)
    
    assert circle1.area < circle2.area

def test_adding():

    circle1 = Circle(4)
    circle2 = Circle(5)
    
    assert circle1+circle2 == Circle(9)


def test_mul():

    circle1 = Circle(4)
    circle2 = Circle(5)
    
    assert circle1*circle2 == Circle(20)
    #assert circle1*2 == Circle8
