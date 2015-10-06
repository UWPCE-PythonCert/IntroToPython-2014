.. _exercise_grid_printer:

======================
Grid Printer Exercise
======================

Printing a Grid
===============

(adapted from Downey, "Think Python", ex. 3.5)

Goal:
------

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

.. nextslide::

Hint: to print more than one value on a line, you can pass multiple names into the print function:
``print('+', '-')``

If you don't want a newline after somethign is printed, you tell python what you want the print to end with like so:

::

  print('+', end=' '),
  print('-')

The output of these statements is ``'+ -'``.

A print function with no arguments ends the current line and goes to the next line::

    print()

.. nextslide::

**Part 2:**

Write a function ``print_grid()`` that takes one integer argument
and prints a grid like the picture above, BUT the size of the
grid is given by the argument.

For example, ``print_grid(11)`` prints the grid in the above picture.

This problem is underspecified.  Do something reasonable.

Hints:

  A character is a string of length 1

  ``s + t`` is string ``s`` followed by string ``t``

  ``s * n`` is string ``s`` replicated n times

.. nextslide::

**Part 3:**

Write a function that draws a similar grid with three rows and three columns.

(what to do about rounding?)

And while you are at it -- n rows and columns...
