.. _exercise_args_kwargs_lab:

*******************
args and kwargs Lab
*******************

Learning about ``args`` and ``kwargs``
======================================

Goal:
-----

Develop an understanding of using advanced argument passing and parameter definitons.

If this is all confusing -- you may want to review this:

http://stupidpythonideas.blogspot.com/2013/08/arguments-and-parameters.html

Procedure
---------

**Keyword arguments:**

* Write a function that has four optional parameters (with defaults):

  - `fore_color`
  - `back_color`
  - `link_color`
  - `visited_color`

* Have it print the colors (use strings for the colors)

* Call it with a couple different parameters set

  - using just positional arguments:

    - ``func('red', 'blue', 'yellow', 'chartreuse')``

  - using just keyword arguments:

    -  ``func(link_color='red', back_color='blue')``

  - using a combination of positional and keyword

    -  ````func('purple', link_color='red', back_color='blue')``

  - using ``*some_tuple`` and/or ``**some_dict``

    - ``regular = ('red', 'blue')``

    - ``links = {'link_color': 'chartreuse'}``

    - ``func(*regular, *links)``

.. nextslide::

**Generic parameters:**

* Write a the same function with the parameters as:

``*args`` and ``**kwags``

* Have it print the colors (use strings for the colors)

* Call it with the same various combinations of arguments used above.

*  Also have it print `args` and `kwargs` directly, so you can be sure you understand what's going on.

* Note that in general, you can't know what will get passed into ``**kwargs`` So maybe adapt your function to be able to do something reasonable with any keywords.


