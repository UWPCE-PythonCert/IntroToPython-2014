#!/usr/bin/env python

"""
A version of TP's distance -- showing tuple unpacking

"""

import math

# TP's version:
def distance(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    dsquared = dx**2 + dy**2
    result = math.sqrt(dsquared)
    return result

# my version:
def distance2( pt1, pt2 ):
    dx = pt2[0] - pt1[0]
    dy = pt2[1] - pt1[1]
    dsquared = dx**2 + dy**2
    result = math.sqrt(dsquared)
    return result

# my version:
def distance3( (x1, y1), (x2, y2) ):
    
    dx = x2 - x1
    dy = y2 - y1
    dsquared = dx**2 + dy**2
    result = math.sqrt(dsquared)
    return result
