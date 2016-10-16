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

https://mkaz.tech/python-string-format.html


A Couple Exercises
------------------

* Write a format string that will take:

    ``( 2, 123.4567, 10000)``

    and produce:

    ``'file_002 :   123.46, 1.00e+04'``

**Note:** the idea behind the "file_002" is that if you have a bunch of files that you want to name with numbers that can be sorted, you need to "pad" the numbers with zeros to get the right sort order.

.. nextslide::

For example:

.. code-block:: ipython

    In [10]: fnames = ['file1', 'file2', 'file10', 'file11']
    In [11]: fnames.sort()
    In [12]: fnames
    Out[12]: ['file1', 'file10', 'file11', 'file2']

That is probably not what you want. However:

.. code-block:: ipython

    In [1]: fnames = ['file001', 'file002', 'file010', 'file011']
    In [3]: sorted(fnames)
    Out[3]: ['file001', 'file002', 'file010', 'file011']

That works!

So you want to find a string formatting operator that will "pad" the number with zeros for you.

Dynamically Building up format strings
--------------------------------------

* Rewrite:

``"the 3 numbers are: {:d}, {:d}, {:d}".format(1,2,3)``

to take an arbitrary number of values.

Trick: You can pass in a tuple of values to a function with a ``*``:

.. code-block:: ipython

    In [52]: t = (1,2,3)

    In [53]: "the 3 numbers are: {:d}, {:d}, {:d}".format(*t)
    Out[53]: 'the 3 numbers are: 1, 2, 3'

.. nextslide::

The idea here is that you may have a tuple of three numbers, but might also have 4 or 5 or....

So you can dynamically build up the format string to accommodate the length of the tuple.

The string object has the ``format()`` method, so you can call it with a string that is bound to a name, not just a string literal. For example:

.. code-block:: ipython

    In [16]: fstring = "{:d}, {:d}"

    In [17]: nums = (34, 56)

    In [18]: fstring.format(*nums)
    Out[18]: '34, 56'

So how would you make an fstring that was the right length for an arbitrary tuple?

.. nextslide::

Put your code in a function that will return the formatted string like so:

.. code-block:: ipython

    In [20]: formatter((2,3,5))
    Out[20]: 'the 3 numbers are: 2, 3, 5'

    In [21]: formatter((2,3,5,7,9))
    Out[21]: 'the 5 numbers are: 2, 3, 5, 7, 9'

