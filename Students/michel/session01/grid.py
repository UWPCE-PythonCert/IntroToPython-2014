# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def grid(nbCol, nbRow, size):
    
    ''' Draws a grid nbCol wide and nbRow tall
    nbCol and nbRow are integers > 0 and < 10
    size is the width of a cell
    size is an integer > 2
    the function returns nothing'''

    horLine = ''
    verLine = ''
    
    horLine = '+' + '-' * (size - 2) + '+'
    verLine = '|' + ' ' * (size - 2) + '|'
    
    for i in range(nbRow):
        print horLine + (nbCol - 1) * horLine[1:]
        for j in range(size - 2):
            print verLine + (nbCol - 1) * verLine[1:]
    
    print horLine + (nbCol - 1) * horLine[1:]        
    return
    
