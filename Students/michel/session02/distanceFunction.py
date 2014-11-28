# -*- coding: utf-8 -*-
"""
Created on Tue Oct 07 20:25:04 2014

@author: Michel
"""

def distance(x1, y1, x2, y2):
    """ Return distance between 2 points in 2D cartesian coordinates
    x1, y1, x2, y2 are float
    """
    
    distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
    
    return distance
    
