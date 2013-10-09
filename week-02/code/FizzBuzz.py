#!/usr/bin/env python

"""
Fizz Buzz example
"""

for i in range(1, 101):
    msg = ''
    if not (i % 3):
        msg = msg+"Fizz"
    if not (i % 5):
        msg = msg+"Buzz"
    if msg:
        print msg
    else:
        print i
#    print msg or i
    
