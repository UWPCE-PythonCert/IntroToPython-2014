.. _exercise_comprehensions:

******************
Comprehensions Lab
******************

Playing with Comprehensions
============================


.. rst-class:: large left

    Goal:

.. rst-class:: medium left

    Getting Familiar with list, set and dict comprehensions


List comprehensions
--------------------

Note: this is a bit of a "backwards" exercise --
we show you code, you figure out what it does.

As a result, not much to submit -- don't worry about it -- you'll have
a chance to use these in other exercises.

.. code-block:: python

    >>> feast = ['lambs', 'sloths', 'orangutans',
                 'breakfast cereals', 'fruit bats']

    >>> comprehension = [delicacy.capitalize() for delicacy in feast]

What is the output of:

.. code-block:: python

    >>> comprehension[0]
    ???

    >>> comprehension[2]
    ???

(figure it out before you try it)

Filtering lists with list comprehensions
----------------------------------------

.. code-block:: python

    >>> feast = ['spam', 'sloths', 'orangutans', 'breakfast cereals',
                'fruit bats']

    >>> comp = [delicacy for delicacy in feast if len(delicacy) > 6]

What is the output of:

.. code-block:: python

    >>> len(feast)
    ???

    >>> len(comp)
    ???

(figure it out first!)


Unpacking tuples in list comprehensions
---------------------------------------

.. code-block:: python

    >>> list_of_tuples = [(1, 'lumberjack'), (2, 'inquisition'), (4, 'spam')]

    >>> comprehension = [ skit * number for number, skit in list_of_tuples ]

What is the output of:

.. code-block:: python

    >>> comprehension[0]
    ???

    >>> len(comprehension[2])
    ???

Double list comprehensions
---------------------------
.. code-block:: python

    >>> eggs = ['poached egg', 'fried egg']

    >>> meats = ['lite spam', 'ham spam', 'fried spam']

    >>> comprehension = \
    [ '{0} and {1}'.format(egg, meat) for egg in eggs for meat in meats]

What is the output of:

.. code-block:: python

    >>> len(comprehension)
    ???

    >>> comprehension[0]
    ???

Set comprehensions
------------------

.. code-block:: python

    >>> comprehension = { x for x in 'aabbbcccc'}

What is the output of:

.. code-block:: python

    >>> comprehension
    ???

Dictionary comprehensions
-------------------------

.. code-block:: python

    >>> dict_of_weapons = {'first': 'fear',
                           'second': 'surprise',
                           'third':'ruthless efficiency',
                           'forth':'fanatical devotion',
                           'fifth': None}
    >>> dict_comprehension = \
    { k.upper(): weapon for k, weapon in dict_of_weapons.items() if weapon}

What is the output of:

.. code-block:: python

    >>> 'first' in dict_comprehension
    ???
    >>> 'FIRST' in dict_comprehension
    ???
    >>> len(dict_of_weapons)
    ???
    >>> len(dict_comprehension)
    ???

Other resources
---------------


See also:

https://github.com/gregmalcolm/python_koans

Specifically (for comprehensions):

https://github.com/gregmalcolm/python_koans/blob/master/python3/koans/about_comprehension.py


Count Even Numbers
------------------

This is from CodingBat "count_evens" (http://codingbat.com/prob/p189616)

*Using a list comprehension*, return the number of even integers in the given array.

Note: the % "mod" operator computes the remainder, e.g. ``5 % 2`` is 1.

.. code-block:: python

    count_evens([2, 1, 2, 3, 4]) == 3

    count_evens([2, 2, 0]) == 3

    count_evens([1, 3, 5]) == 0


.. code-block:: python

    def count_evens(nums):
       one_line_comprehension_here


``dict`` and ``set`` comprehensions
------------------------------------

Revisiting the dict/set lab -- see how much you can do with
comprehensions instead.

(:ref:`exercise_dict_lab`)

Specifically,  look at these:

First a slightly bigger, more interesting (or at least bigger..) dict:

.. code-block:: python

    food_prefs = {"name": "Chris",
                  "city": "Seattle",
                  "cake": "chocolate",
                  "fruit": "mango",
                  "salad": "greek",
                  "pasta": "lasagna"}

.. nextslide:: Working with this dict:

1. Print the dict by passing it to a string format method, so that you
get something like:

    "Chris is from Seattle, and he likes chocolate cake, mango fruit,
     greek salad, and lasagna pasta"

2. Using a list comprehension, build a dictionary of numbers from zero
to fifteen and the hexadecimal equivalent (string is fine).
(the ``hex()`` function gives you the hexidecimal representation of a number.)

3. Do the previous entirely with a dict comprehension -- should be a one-liner

4. Using the dictionary from item 1: Make a dictionary using the same
keys but with the number of 'a's in each value. You can do this either
by editing the dict in place, or making a new one. If you edit in place,
make a copy first!

.. nextslide::

5. Create sets s2, s3 and s4 that contain numbers from zero through twenty,
divisible 2, 3 and 4.

    a. Do this with one set comprehension for each set.

    b. What if you had a lot more than 3? -- Don't Repeat Yourself (DRY)

       - create a sequence that holds all three sets

       - loop through that sequence to build the sets up -- so no repeated code.

    c. Extra credit:  do it all as a one-liner by nesting a set comprehension
       inside a list comprehension. (OK, that may be getting carried away!)
