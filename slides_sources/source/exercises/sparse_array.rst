.. _exercise_sparse_array:

======================
Sparse Array Exercise
======================

Sparse Array
============

.. rst-class:: medium

    Goal:

Learn how to emulate a built-in class.

Sparse Array:
-------------

Oftentimes, at least in computation programming, we have large arrays of data that hold mostly zeros.

These are referred to as "sparse" as the information in them is widely scattered, or sparse.

Since they are mostly zeros, it can be memory and computationally efficient to store only the value that are non-zero.

But you want it to look like a regular array in user code.

In the real world, these are usually 2 dimensional arrays. But to keep it a bit simpler, we'll make a 1 dimensional sparse array in this class.

(feel free to make it 2d for an extra challenge!)

A Sparse array class
--------------------

A spare array class should present to the user the same interface as a regular list.

Some ideas of how to do that:

* Internally, it can store the values in a dict, with the index as the keys. So that only the indexes with non-zero values will be stored.

* It should take a sequence of values as an initializer:

.. code-block:: python

    sa = SparseArray([1,2,0,0,0,0,3,0,0,4])

* you should be able to tell how long it is:

.. code-block:: python

    len(my_array)

  This will give its "virtual" length --  with the zeros

.. nextslide::

* It should support getting and setting particular elements via indexing:

.. code-block:: python

    sa[5] = 12
    sa[3] = 0 # the zero won't get stored!
    val = sa[13] # it should get a zero if not set

* It should support deleting an element by index:

.. code-block:: python

    del sa[4]

* It should raise an ``IndexError`` if you try to access an index beyond the end.

* it should have an append() method

.. nextslide::

* Can you make it support slicing?

* How else can you  make it like a list?

.. code-block:: ipython

    In [10]: my_array = SparseArray( (1,0,0,0,2,0,0,0,5) )
    In [11]: my_array[4]
    Out[11]: 2
    In [12]: my_array[2]
    Out[12]: 0
