# -*- coding: utf-8 -*-
"""
Created on Tue Oct 14 20:03:39 2014

@author: Michel
"""

fruit = ['Apples', 'Pears', 'Oranges', 'Peaches']
print fruit
otherFruit = raw_input('Other fruit? ')
fruit.append(otherFruit)
print fruit
number = raw_input('Enter a number: ')
number = int(number)
print number, fruit[number]
# fruit = 'Cherries' + fruit
print fruit
fruit.insert(0, 'Lemons')
print fruit
print for i in fruit: 
    
# adding a comment for test purposes
