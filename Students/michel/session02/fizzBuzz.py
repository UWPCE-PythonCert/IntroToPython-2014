# -*- coding: utf-8 -*-
"""
Created on Tue Oct 07 20:33:17 2014

@author: Michel
"""

for number in range(100):
    
    if not number % 3 == 0 and not number % 5 == 0:
        print number
        
    elif number % 3 == 0 and not number % 5 == 0:
        print 'Fizz'
        
    elif not number % 3 == 0 and number % 5 == 0:
        print 'Buzz'
        
    else:
        print 'FizzBuzz'
        
        