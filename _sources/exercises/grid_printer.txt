.. _exercise_grid_printer:

*********************
Grid Printer Exercise
*********************

Printing a Grid
================

(adapted from Downey, "Think Python", ex. 3.5)

Goal:
-----

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

hints
-----

.. rst-class:: center medium

    A couple features to get you started...

printing
--------

To print more than one value on a line, you can pass multiple names into the print function:

.. code-block:: python

  print('+', '-')

If you don't want a newline after something is printed, you tell python what you want the print to end with like so:

.. code-block:: python

  print('+', end=' ')
  print('-')

The output of these statements is ``'+ -'``.

(that end parameter defaults to a newline...)

.. nextslide:: no arguments...

A print function with no arguments ends the current line and goes to the next line:

.. code-block:: python

    print()


Simple string manipulation:
---------------------------

You can put two strings together with the plus operator:

.. code-block:: ipython

  In [20]: "this" + "that"
  Out[20]: 'thisthat

Particularly useful if they have been assigned names:

.. code-block:: ipython

  In [21]: plus = '+'

  In [22]: minus = '-'

  In [23]: plus+minus+plus
  Out[23]: '+-+'

Note that you can string any number of operations together in an expression.

.. nextslide:: multiplication of strings

You can also multiply strings:

.. code-block:: ipython

  In [24]: '+' * 10
  Out[24]: '++++++++++'

And combine that with plus in a complex expression:

.. code-block:: ipython

  In [29]: first_name = 'Chris'

  In [30]: last_name = 'Barker'

  In [31]: 5 * '*' + first_name +' ' + last_name + 5 * '*'
  Out[31]: '*****Chris Barker*****'

Note that there are better ways to build up complex strings -- we'll get to that later.

Now you've got what you need to print that grid...

Part 2
=======

.. rst-class:: center medium

    Making it more general

Make it a function
------------------

One of the points of writing functions is so you can write code that does similar things, but customized to input parameters. So what if we want to be able to print that grid at an arbitrary size?

Write a function ``print_grid(n)`` that takes one integer argument
and prints a grid just like before, BUT the size of the
grid is given by the argument.

For example, ``print_grid(11)`` prints the grid in the above picture.

``print_grid(3)`` would print a smaller grid::

  + - + - +
  |   |   |
  + - + - +
  |   |   |
  + - + - +

.. nextslide::

``print_grid(15)`` prints a larger grid::

    + - - - - - - - + - - - - - - - +
    |               |               |
    |               |               |
    |               |               |
    |               |               |
    |               |               |
    |               |               |
    |               |               |
    + - - - - - - - + - - - - - - - +
    |               |               |
    |               |               |
    |               |               |
    |               |               |
    |               |               |
    |               |               |
    |               |               |
    + - - - - - - - + - - - - - - - +

.. nextslide::

This problem is underspecified.  Do something reasonable.

Part 3:
=======

Even more general...

A function with two parameters
-------------------------------

Write a function that draws a similar grid with a specified number of rows and columns, and each cell a given size.

for example,  ``print_grid2(3,4)`` results in::

    + - - - - + - - - - + - - - - +
    |         |         |         |
    |         |         |         |
    |         |         |         |
    |         |         |         |
    + - - - - + - - - - + - - - - +
    |         |         |         |
    |         |         |         |
    |         |         |         |
    |         |         |         |
    + - - - - + - - - - + - - - - +
    |         |         |         |
    |         |         |         |
    |         |         |         |
    |         |         |         |
    + - - - - + - - - - + - - - - +

.. nextslide::

What to do about rounding? -- you decide.

Another example: ``print_grid2(5,3)``::

    + - - - + - - - + - - - + - - - + - - - +
    |       |       |       |       |       |
    |       |       |       |       |       |
    |       |       |       |       |       |
    + - - - + - - - + - - - + - - - + - - - +
    |       |       |       |       |       |
    |       |       |       |       |       |
    |       |       |       |       |       |
    + - - - + - - - + - - - + - - - + - - - +
    |       |       |       |       |       |
    |       |       |       |       |       |
    |       |       |       |       |       |
    + - - - + - - - + - - - + - - - + - - - +
    |       |       |       |       |       |
    |       |       |       |       |       |
    |       |       |       |       |       |
    + - - - + - - - + - - - + - - - + - - - +
    |       |       |       |       |       |
    |       |       |       |       |       |
    |       |       |       |       |       |
    + - - - + - - - + - - - + - - - + - - - +



