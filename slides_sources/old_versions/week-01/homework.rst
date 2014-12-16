Homework for week 1 (Due week 2)
==================================

(adapted from Downey, "Think Python", ex. 3.5)


Part 1
----------

Write a function that draws a grid like the following::


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

Hint: to print more than one value on a line, you can print a comma-separated sequence:
``print '+', '-'``

If the sequence ends with a comma, Python leaves the line unfinished, so the value printed next appears on the same line.

::

  print '+', 
  print '-'

The output of these statements is ``'+ -'``.

A print statement all by itself ends the current line and goes to the next line.


Part 2:
--------

Write a function ``print_grid()`` that takes one integer argument
and prints a grid like the picture above, BUT the size of the
grid is given by the argument.  

For example, ``print_grid(11)`` prints the grid in the above picture.

This problem is underspecified.  Do something reasonable.

Hints:

  A character is a string of length 1

  ``s + t`` is string ``s`` followed by string ``t``

  ``s * n`` is string ``s`` replicated n times

Part 3:
----------

Write a function that draws a similar grid with three rows and three columns.

(what to do about rounding?)



