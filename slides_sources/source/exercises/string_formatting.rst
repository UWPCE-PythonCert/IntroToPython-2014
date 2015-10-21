.. _exercise_string_formatting:

*********************
String Formatting Lab
*********************

Building up strings
===================

.. rst-class:: left

For reference:

The official reference docs:

https://docs.python.org/3/library/string.html#string-formatting

And a more human-readable intro:

https://pyformat.info/

And a nice "Cookbook":

https://mkaz.github.io/2012/10/10/python-string-format/


A couple Exercises
------------------

* Write a format string that will take:

    ``( 2, 123.4567, 10000)``

    and produce:

    ``'file_002 :   123.46, 1e+04'``

* Rewrite: ``"the first 3 numbers are: {:d}, {:d}, {:d}".format(1,2,3)``
  to take an arbitrary number of values

Trick: You can pass in a tuple of values to a function with a ``*``::

.. code-block:: ipython

    In [52]: t = (1,2,3)

    In [53]: "the first 3 numbers are: {:d}, {:d}, {:d}".format(*t)
    Out[53]: 'the first 3 numbers are: 1, 2, 3'
