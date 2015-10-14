#! /bin/env python3

import sys as s

def print_grid(cols, rows):
    """ Function to print a grid.
    
    Args:
        cols (int): Number of colums in the grid.
        rows (int): Number of rows in the grid.
    """
    
    def h():
        """Function to draw a one line horizontal bar."""
        a = '+ '
        b = '- '*4
        print((a + b)*cols + '+\n')
        
    def v():
        """Function to draw one line of the vertical bars."""
        a = '|' + ' '*9
        print(a*cols + '|\n')
          
    def draw_row():
        """Function to draw one row of the grid."""
        c = 1
        while c <=  5:
            if c == 5:
                h()
            else:
                v()
            c = c + 1
            
    r = 1
    while r <= rows:
        if r == 1:
            h()
        draw_row()
        r = r + 1
    

if __name__ == "__main__":
    try:
        print_grid(int(s.argv[1]), int(s.argv[2]))
    except:
        print("\nUsage: print_grid.py [# of columns] [# of rows]")
        s.exit(0)
