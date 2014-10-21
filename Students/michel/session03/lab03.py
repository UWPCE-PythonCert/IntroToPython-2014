# -*- coding: utf-8 -*-
"""
Created on Tue Oct 14 18:36:14 2014

@author: Michel
"""


# return string with first and last character exchanged
def exchange(a_string):
    return a_string[-1] + a_string[1:-1] + a_string[0]


# return string with every other character removed
def removeChar(a_string):
    return a_string[::2]
    
    
# return a string with the first and last 4 characters removed and every other character in between
def removeFour(a_string):
    return a_string[4:-4]
    

# return a string reversed with slicing
def reverseSlicing(a_string):
    return a_string[::-1]
    
#return a string with thirds in different order: middle, last, first
def mixedString(a):
    return a[len(a)/3:2*len(a)/3] + a[2*len(a)/3:] + a[:len(a)/3]