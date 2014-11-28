'''

Dave Fugelso

Problem:

Write a function that draws a grid like the following:

+ - - - - + - - - - +
|         |         |
|         |         |
|         |         |
|         |         |
+ - - - - + - - - - +
|         |         |
|         |         |
|         |         |
|         |         |
+ - - - - + - - - - +
Hint: to print more than one value on a line, you can print a comma-separated sequence: print "+ -"

If the sequence ends with a comma, Python leaves the line unfinished, so the value printed next appears on the same line.

print "+",
print "-"
The output of these statements is "+ -".

A print statement all by itself ends the current line and goes to the next line.

Part 2:

Write a function print_grid() that takes one integer argument and prints a grid like the picture above, BUT the size of the grid is given by the argument.

For example, print_grid(11) prints the grid in the above picture.

This problem is underspecified. Do something reasonable.

Hints:

A character is a string of length 1

s + t is string s followed by string t

s * n is string s replicated n times

Part 3:

Write a function that draws a similar grid with three rows and three columns.

(what to do about rounding?)



'''

def cellTopBottom(cells, size):
   '''
   print cell top or botton, including the '+'
   '''
   for columns in range (0, cells):
      print '+',
      for i in range (0, size):
         print '-',
   print '+'
       
def printSide (cells, size):
   '''
   Just do the sides, no '+'
   '''


   for rows in range (0, size):
      print '|',    
      for column in range (0, cells):
         for spaces in range(0, size):
            print ' ',
         print '|', 
      print

def fixed_grid():
   '''
   print a two by two grid like example above.
   '''
   cells = 2
   size = 4
   
   for rows in range(0, cells):
      cellTopBottom(cells, size)
      printSide (cells, size)
   cellTopBottom(cells, size)

def print_grid(size):
   '''
   Take an argument and print a grid with a vartiable size
   '''
   cells = 2
   
   for rows in range(0, cells):
      cellTopBottom(cells, size)
      printSide (cells, size)
   cellTopBottom(cells, size)

def print_grid_variable_cells(cells, size):
   '''
   Take an argument and print a grid with a variable size
   Take an argument for number of cells
   
   Ah, by using cells and size for the cell size I completely missed the rounding portion of this problem.
   If I did do iut the other way, I would have left off the right and bottom edges.
   '''
   
   for rows in range(0, cells):
      cellTopBottom(cells, size)
      printSide (cells, size)
   cellTopBottom(cells, size)   
   
fixed_grid()
print_grid(4)
print_grid(5)
print_grid_variable_cells (3, 4)

