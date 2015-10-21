*********************************************************
Session Three: Sequences, Iteration and String Formatting
*********************************************************

Review/Questions
================

Review of Previous Session
--------------------------

* Functions

  - recursion
  - optional arguments

* Booleans

  - if and conditional expressions

* Modules


Homework Review
---------------

* FizzBuzz

* Series

.. rst-class:: center large

Any questions that are nagging?

git
---

.. rst-class:: center large

  OK -- we'll answer git questions...

Lightning Talks Today:
----------------------

.. rst-class:: mlarge

   Eric Rosko

   Michael Waddle

   Robert Alford


Sequences
=========

.. rst-class:: center large

Ordered collections of objects


What is a Sequence?
-------------------

Remember Duck Typing?

A *sequence* can be considered as anything that supports
*at least* these operations:

.. rst-class:: build

* Indexing
* Slicing
* Membership
* Concatenation
* Length
* Iteration


Sequence Types
--------------

There are eight builtin types in Python that are *sequences*:

* string
* list
* tuple
* bytes
* bytearray
* buffer
* array.array
* range object (almost)

For this class, you won't see much beyond string, lists, and tuples -- the rest are pretty special purpose.

But what we learn today applies to all sequences (with minor caveats)


Indexing
--------

Items in a sequence may be looked up by *index* using the indexing
operator: ``[]``

Indexing in Python always starts at zero.

.. code-block:: ipython

    In [98]: s = "this is a string"
    In [99]: s[0]
    Out[99]: 't'
    In [100]: s[5]
    Out[100]: 'i'


.. nextslide::

You can use negative indexes to count from the end:

.. code-block:: ipython

    In [2]: a_list = [34, 56, 19, 23, 55]

    In [3]: a_list[-1]
    Out[3]: 55

    In [4]: a_list[-2]
    Out[4]: 23

    In [5]: a_list[-4]
    Out[5]: 56

.. nextslide::

Indexing beyond the end of a sequence causes an IndexError:

.. code-block:: ipython

    In [6]: a_list
    Out[6]: [34, 56, 19, 23, 55]

    In [7]: a_list[5]
    ---------------------------------------------------------------------------
    IndexError                                Traceback (most recent call last)
    <ipython-input-7-c1f9ac3b6fee> in <module>()
    ----> 1 a_list[5]

    IndexError: list index out of range

Slicing
-------

Slicing a sequence creates a new sequence with a range of objects from the
original sequence.

It also uses the indexing operator (``[]``), but with a twist.

``sequence[start:finish]`` returns all sequence[i] for which start <= i < finish:

.. code-block:: ipython

    In [121]: s = "a bunch of words"
    In [122]: s[2]
    Out[122]: 'b'
    In [123]: s[6]
    Out[123]: 'h'
    In [124]: s[2:6]
    Out[124]: 'bunc'
    In [125]: s[2:7]
    Out[125]: 'bunch'

.. nextslide:: Helpful Hint

Think of the indexes as pointing to the spaces between the items::

       a       b   u   n   c   h       o   f       w   o   r   d   s
     |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
     0   1   2   3   4   5   6   7   8   9  10  11  12  13  14  15



.. nextslide:: Slicing

You do not have to provide both ``start`` and ``finish``:

.. code-block:: ipython

    In [6]: s = "a bunch of words"
    In [7]: s[:5]
    Out[7]: 'a bun'
    In [8]: s[5:]
    Out[8]: 'ch of words'

Either ``0`` or ``len(s)`` will be assumed, respectively.

You can combine this with the negative index to get the end of a sequence:

.. code-block:: ipython

    In [4]: s = 'this_could_be_a_filename.txt'
    In [5]: s[:-4]
    Out[5]: 'this_could_be_a_filename'
    In [6]: s[-4:]
    Out[6]: '.txt'


Why start from zero?
--------------------

Python indexing feels 'weird' to some folks -- particularly those that don't come with a background in the C family of languages.

Why is the "first" item indexed with **zero**?

Why is the last item in the slice **not** included?

Because these lead to some nifty properties::

    len(seq[a:b]) == b-a

    seq[:b] + seq[b:] == seq

    len(seq[:b]) == b

    len(seq[-b:]) == b

There are very many fewer "off by one" errors as a result.


.. nextslide:: Slicing

Slicing takes a third argument, ``step`` which controls which items are
returned:

.. code-block:: ipython

    In [18]: a_tuple
    Out[18]: (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19)

    In [19]: a_tuple[0:15]
    Out[19]: (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)

    In [20]: a_tuple[0:15:2]
    Out[20]: (0, 2, 4, 6, 8, 10, 12, 14)

    In [21]: a_tuple[0:15:3]
    Out[21]: (0, 3, 6, 9, 12)

    In [22]: a_tuple[::-1]
    Out[22]: (19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0)

.. nextslide:: Slicing vs. Indexing


Though they share an operator, slicing and indexing have a few important
differences:

Indexing will always return one object, slicing will return a sequence of
objects.

Indexing past the end of a sequence will raise an error, slicing will not:

.. code-block:: ipython

    In [129]: s = "a bunch of words"
    In [130]: s[17]
    ----> 1 s[17]
    IndexError: string index out of range
    In [131]: s[10:20]
    Out[131]: ' words'
    In [132]: s[20:30]
    Out[132]: "


(demo)

Membership
----------

All sequences support the ``in`` and ``not in`` membership operators:

.. code-block:: ipython

    In [15]: s = [1, 2, 3, 4, 5, 6]
    In [16]: 5 in s
    Out[16]: True
    In [17]: 42 in s
    Out[17]: False
    In [18]: 42 not in s
    Out[18]: True

.. nextslide:: Membership in Strings

For strings, the membership operations are like ``substring`` operations in
other languages:

.. code-block:: ipython

    In [20]: s = "This is a long string"
    In [21]: "long" in s
    Out[21]: True

This does not work for sub-sequences of other types (can you think of why?):

.. code-block:: ipython

    In [22]: s = [1, 2, 3, 4]
    In [23]: [2, 3] in s
    Out[23]: False


Concatenation
-------------

Using ``+`` or ``*`` on sequences will *concatenate* them:

.. code-block:: ipython

    In [18]: l1 = [1,2,3,4]
    In [19]: l2 = [5,6,7,8]
    In [20]: l1 + l2
    Out[20]: [1, 2, 3, 4, 5, 6, 7, 8]
    In [21]: (l1+l2) * 2
    Out[21]: [1, 2, 3, 4, 5, 6, 7, 8, 1, 2, 3, 4, 5, 6, 7, 8]

.. nextslide:: Multiplying and Slicing

You can apply this concatenation to slices as well, leading to some nicely
concise code:

from CodingBat: Warmup-1 -- front3

.. code-block:: python

    def front3(str):
      if len(str) < 3:
        return str+str+str
      else:
        return str[:3]+str[:3]+str[:3]

This non-pythonic solution can also be expressed like so:

.. code-block:: python

    def front3(str):
        return str[:3] * 3

Length
------

All sequences have a length.  You can get it with the ``len`` builtin:

.. code-block:: ipython

    In [36]: s = "how long is this, anyway?"
    In [37]: len(s)
    Out[37]: 25

Remember: Sequences are 0-indexed, so the last index is ``len(s)-1``:

.. code-block:: ipython

    In [38]: count = len(s)
    In [39]: s[count]
    ------------------------------------------------------------
    IndexError                Traceback (most recent call last)
    <ipython-input-39-5a33b9d3e525> in <module>()
    ----> 1 s[count]
    IndexError: string index out of range

Even better: use ``s[-1]``


Miscellaneous
-------------

There are a more operations supported by all sequences

.. nextslide:: Min and Max

All sequences also support the ``min`` and ``max`` builtins:

.. code-block:: ipython

    In [42]: all_letters = "thequickbrownfoxjumpedoverthelazydog"
    In [43]: min(all_letters)
    Out[43]: 'a'
    In [44]: max(all_letters)
    Out[44]: 'z'

Why are those the answers you get? (hint: ``ord('a')``)

Of course this works with numbers, too!

.. nextslide:: Index

All sequences also support the ``index`` method, which returns the index of the first occurence of an item in the sequence:

.. code-block:: ipython

    In [46]: all_letters.index('d')
    Out[46]: 21

This causes a ``ValueError`` if the item is not in the sequence:

.. code-block:: ipython

    In [47]: all_letters.index('A')
    ---------------------------------------------------------------------------
    ValueError                                Traceback (most recent call last)
    <ipython-input-47-2db728a46f78> in <module>()
    ----> 1 all_letters.index('A')

    ValueError: substring not found

.. nextslide:: Count

A sequence can also be queried for the number of times a particular item
appears:

.. code-block:: ipython

    In [52]: all_letters.count('o')
    Out[52]: 4
    In [53]: all_letters.count('the')
    Out[53]: 2

This does not raise an error if the item you seek is not present:

.. code-block:: ipython

    In [54]: all_letters.count('A')
    Out[54]: 0


Iteration
---------

.. rst-class:: center mlarge

    All sequences are "iterables" --

    More on this in a while.

Slicing LAB
===========

.. rst-class:: center medium

  Let's practice Slicing!

  :ref:`exercise_slicing`


Lightning Talks
----------------

|
| Eric Rosko
|
|
| Michael Waddle
|


Lists, Tuples...
================

.. rst-class:: center large

The *primary* sequence types.

Lists
-----

Lists can be constructed using list Literals (``[]``):

.. code-block:: ipython

    In [1]: []
    Out[1]: []
    In [2]: [1,2,3]
    Out[2]: [1, 2, 3]
    In [3]: [1, 'a', 7.34]
    Out[3]: [1, 'a', 7.34]

Or by using the ``list`` type object as a constructor:

.. code-block:: ipython

    In [6]: list()
    Out[6]: []
    In [7]: list(range(4))
    Out[7]: [0, 1, 2, 3]
    In [8]: list('abc')
    Out[8]: ['a', 'b', 'c']

It will take any "iterable"

.. nextslide:: List Elements

The elements contained in a list need not be of a single type.

Lists are *heterogenous*, *ordered* collections.

Each element in a list is a value, and can be in multiple lists and have
multiple names (or no name)

.. code-block:: ipython

    In [9]: name = 'Brian'
    In [10]: a = [1, 2, name]
    In [11]: b = [3, 4, name]
    In [12]: a[2]
    Out[12]: 'Brian'
    In [13]: b[2]
    Out[13]: 'Brian'
    In [14]: a[2] is b[2]
    Out[14]: True


Tuples
------

Tuples can be constructed using tuple literals (``()``):

.. code-block:: ipython

    In [15]: ()
    Out[15]: ()
    In [16]: (1, 2)
    Out[16]: (1, 2)
    In [17]: (1, 'a', 7.65)
    Out[17]: (1, 'a', 7.65)
    In [18]: (1,)
    Out[18]: (1,)

.. nextslide:: Tuples and Commas...

Tuples don't NEED parentheses...

.. code-block:: ipython

    In [161]: t = (1,2,3)
    In [162]: t
    Out[162]: (1, 2, 3)
    In [163]: t = 1,2,3
    In [164]: t
    Out[164]: (1, 2, 3)
    In [165]: type(t)
    Out[165]: tuple

.. nextslide:: Tuples and Commas...

But they *do* need commas...!

.. code-block:: ipython

    In [156]: t = ( 3 )
    In [157]: type(t)
    Out[157]: int
    In [158]: t = ( 3, )
    In [160]: type(t)
    Out[160]: tuple

.. nextslide:: Converting to Tuple

You can also use the ``tuple`` type object to convert any iterable(sequence) into a tuple:

.. code-block:: ipython

    In [20]: tuple()
    Out[20]: ()
    In [21]: tuple(range(4))
    Out[21]: (0, 1, 2, 3)
    In [22]: tuple('garbanzo')
    Out[22]: ('g', 'a', 'r', 'b', 'a', 'n', 'z', 'o')


.. nextslide:: Tuple Elements

The elements contained in a tuple need not be of a single type.

Tuples are *heterogenous*, *ordered* collections.

Each element in a tuple is a value, and can be in multiple tuples and have
multiple names (or no name)

.. code-block:: ipython

    In [23]: name = 'Brian'
    In [24]: other = name
    In [25]: a = (1, 2, name)
    In [26]: b = (3, 4, other)
    In [27]: for i in range(3):
       ....:     print(a[i] is b[i], end=' ')
       ....:
    False False True

.. nextslide:: Lists vs. Tuples

.. rst-class:: center large

    So Why Have Both?


Mutability
==========

.. image:: /_static/transmogrifier.jpg
   :width: 35%
   :alt: Presto change-o

.. rst-class:: credit

image from flickr by `illuminaut`_, (CC by-nc-sa)

.. _illuminaut: https://www.flickr.com/photos/illuminaut/3595530403


Mutability in Python
--------------------

All objects in Python fall into one of two camps:

* Mutable
* Immutable

Objects which are mutable may be *changed in place*.

Objects which are immutable may not be changed.

Ever.

.. nextslide:: The Types We Know

========= =======
Immutable Mutable
========= =======
Unicode   List
String
Integer
Float
Tuple
========= =======


.. nextslide:: Lists Are Mutable

Try this out:

.. code-block:: ipython

    In [28]: food = ['spam', 'eggs', 'ham']
    In [29]: food
    Out[29]: ['spam', 'eggs', 'ham']
    In [30]: food[1] = 'raspberries'
    In [31]: food
    Out[31]: ['spam', 'raspberries', 'ham']


.. nextslide:: Tuples Are Not

And repeat the exercise with a Tuple:

.. code-block:: ipython

    In [32]: food = ('spam', 'eggs', 'ham')
    In [33]: food
    Out[33]: ('spam', 'eggs', 'ham')
    In [34]: food[1] = 'raspberries'
    ---------------------------------------------------------------------------
    TypeError                                 Traceback (most recent call last)
    <ipython-input-34-0c3401794933> in <module>()
    ----> 1 food[1] = 'raspberries'

    TypeError: 'tuple' object does not support item assignment


.. nextslide:: Watch When Binding

This property means you need to be aware of what you are doing with your lists:

.. code-block:: ipython

    In [36]: original = [1, 2, 3]
    In [37]: altered = original
    In [38]: for i in range(len(original)):
       ....:     if True:
       ....:         altered[i] += 1
       ....:

Perhaps we want to check to see if altered has been updated, as a flag for
whatever condition caused it to be updated.

What is the result of this code?

.. nextslide:: Perhaps Not What You Expect

Our ``altered`` list has been updated:

.. code-block:: ipython

    In [39]: altered
    Out[39]: [2, 3, 4]

But so has the ``original`` list:

.. code-block:: ipython

    In [40]: original
    Out[40]: [2, 3, 4]

Why?


.. nextslide:: Other Gotchas

Easy container setup, or deadly trap?

(note: you can nest lists to make a 2D-ish array)

.. code-block:: ipython

    In [13]: bins = [ [] ] * 5

    In [14]: bins
    Out[14]: [[], [], [], [], []]

    In [15]: words = ['one', 'three', 'rough', 'sad', 'goof']

    In [16]: for word in words:
       ....:     bins[len(word)-1].append(word)
       ....:

So, what is going to be in ``bins`` now?

.. nextslide:: There is Only **One** Bin

.. code-block:: ipython

    In [65]: bins
    Out[65]:
    [['one', 'three', 'rough', 'sad', 'goof'],
     ['one', 'three', 'rough', 'sad', 'goof'],
     ['one', 'three', 'rough', 'sad', 'goof'],
     ['one', 'three', 'rough', 'sad', 'goof'],
     ['one', 'three', 'rough', 'sad', 'goof']]

We multiplied a sequence containing a single *mutable* object.

We got a list containing five references to a single *mutable* object.


.. nextslide:: Mutable Default Argument

Watch out especially for passing mutable objects as default values for function parameters:

.. code-block:: ipython

    In [71]: def accumulator(count, list=[]):
       ....:     for i in range(count):
       ....:         list.append(i)
       ....:     return list
       ....:
    In [72]: accumulator(5)
    Out[72]: [0, 1, 2, 3, 4]
    In [73]: accumulator(7)
    Out[73]: [0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 5, 6]


Mutable Sequence Methods
========================

.. rst-class:: left

In addition to all the methods supported by sequences we've seen above, mutable sequences (the List), have a number of other methods that are
used to change the list.

You can find all these in the Standard Library Documentation:

https://docs.python.org/3/library/stdtypes.html#typesseq-mutable

Assignment
-----------

You've already seen changing a single element of a list by assignment.

Pretty much the same as "arrays" in most languages:

.. code-block:: ipython

    In [100]: list = [1, 2, 3]
    In [101]: list[2] = 10
    In [102]: list
    Out[102]: [1, 2, 10]


Growing the List
----------------

``.append()``, ``.insert()``, ``.extend()``

.. code-block:: ipython

    In [74]: food = ['spam', 'eggs', 'ham']
    In [75]: food.append('sushi')
    In [76]: food
    Out[76]: ['spam', 'eggs', 'ham', 'sushi']
    In [77]: food.insert(0, 'beans')
    In [78]: food
    Out[78]: ['beans', 'spam', 'eggs', 'ham', 'sushi']
    In [79]: food.extend(['bread', 'water'])
    In [80]: food
    Out[80]: ['beans', 'spam', 'eggs', 'ham', 'sushi', 'bread', 'water']


.. nextslide:: More on Extend

You can pass any sequence to ``.extend()``:

.. code-block:: ipython

    In [85]: food
    Out[85]: ['beans', 'spam', 'eggs', 'ham', 'sushi', 'bread', 'water']
    In [86]: food.extend('spaghetti')
    In [87]: food
    Out[87]:
    ['beans', 'spam', 'eggs', 'ham', 'sushi', 'bread', 'water',
     's', 'p', 'a', 'g', 'h', 'e', 't', 't', 'i']


Shrinking the List
------------------

``.pop()``, ``.remove()``

.. code-block:: ipython

    In [203]: food = ['spam', 'eggs', 'ham', 'toast']
    In [204]: food.pop()
    Out[204]: 'toast'
    In [205]: food.pop(0)
    Out[205]: 'spam'
    In [206]: food
    Out[206]: ['eggs', 'ham']
    In [207]: food.remove('ham')
    In [208]: food
    Out[208]: ['eggs']

.. nextslide:: Removing Chunks of a List

You can also delete *slices* of a list with the ``del`` keyword:

.. code-block:: ipython

    In [92]: nums = range(10)
    In [93]: nums
    Out[93]: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    In [94]: del nums[1:6:2]
    In [95]: nums
    Out[95]: [0, 2, 4, 6, 7, 8, 9]
    In [96]: del nums[-3:]
    In [97]: nums
    Out[97]: [0, 2, 4, 6]


Copying Lists
-------------

You can make copies of part of a list using *slicing*:

.. code-block:: ipython

    In [227]: food = ['spam', 'eggs', 'ham', 'sushi']
    In [228]: some_food = food[1:3]
    In [229]: some_food[1] = 'bacon'
    In [230]: food
    Out[230]: ['spam', 'eggs', 'ham', 'sushi']
    In [231]: some_food
    Out[231]: ['eggs', 'bacon']

If you provide *no* arguments to the slice, it makes a copy of the entire list:

.. code-block:: ipython

    In [232]: food
    Out[232]: ['spam', 'eggs', 'ham', 'sushi']
    In [233]: food2 = food[:]
    In [234]: food is food2
    Out[234]: False


.. nextslide:: Shallow Copies

The copy of a list made this way is a *shallow copy*.

The list is itself a new object, but the objects it contains are not.

*Mutable* objects in the list can be mutated in both copies:

.. code-block:: ipython

    In [249]: food = ['spam', ['eggs', 'ham']]
    In [251]: food_copy = food[:]
    In [252]: food[1].pop()
    Out[252]: 'ham'
    In [253]: food
    Out[253]: ['spam', ['eggs']]
    In [256]: food.pop(0)
    Out[256]: 'spam'
    In [257]: food
    Out[257]: [['eggs']]
    In [258]: food_copy
    Out[258]: ['spam', ['eggs']]


.. nextslide:: Copies Solve Problems

Consider this common pattern:

.. code-block:: python

    for x in somelist:
        if should_be_removed(x):
            somelist.remove(x)

This looks benign enough, but changing a list while you are iterating over it can be the cause of some pernicious bugs.

.. nextslide:: The Problem

For example:

.. code-block:: ipython

    In [27]: l = list(range(10))
    In [28]: l
    Out[28]: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    In [29]: for item in l:
       ....:     l.remove(item)
       ....:
    In [30]: l
    Out[30]: [1, 3, 5, 7, 9]

Was that what you expected?

.. nextslide:: The Solution

Iterate over a copy, and mutate the original:

.. code-block:: ipython

    In [33]: l = list(range(10))

    In [34]: for item in l[:]:
       ....:     l.remove(item)
       ....:
    In [35]: l
    Out[35]: []


.. nextslide:: Just Say It, Already

Okay, so we've done this a bunch already, but let's state it out loud.

You can iterate over a sequence.

.. code-block:: python

    for element in sequence:
        do_something(element)

which is what we mean when we say a sequence is an "iterable".

Again, we'll touch more on this in a short while, but first a few more words about Lists and Tuples.


Miscellaneous List Methods
--------------------------


These methods change a list in place and are not available on immutable sequence types.

``.reverse()``

.. code-block:: ipython

    In [129]: food = ['spam', 'eggs', 'ham']
    In [130]: food.reverse()
    In [131]: food
    Out[131]: ['ham', 'eggs', 'spam']

``.sort()``

.. code-block:: ipython

    In [132]: food.sort()
    In [133]: food
    Out[133]: ['eggs', 'ham', 'spam']

Because these methods mutate the list in place, they have a return value of ``None``


.. nextslide:: Custom Sorting

``.sort()`` can take an optional ``key`` parameter.

It should be a function that takes one parameter (list items one at a time) and returns something that can be used for sorting:

.. code-block:: ipython

    In [137]: def third_letter(string):
       .....:     return string[2]
       .....:
    In [138]: food.sort(key=third_letter)
    In [139]: food
    Out[139]: ['spam', 'eggs', 'ham']



List Performance
----------------

.. rst-class:: build

* indexing is fast and constant time: O(1)
* ``x in l`` is proportional to n: O(n)
* visiting all is proportional to n: O(n)
* operating on the end of list is fast and constant time: O(1)

  * append(), pop()

* operating on the front (or middle) of the list depends on n: O(n)

  * ``pop(0)``, ``insert(0, v)``
  * But, reversing is fast. ``Also, collections.deque``

 http://wiki.python.org/moin/TimeComplexity


Choosing Lists or Tuples
------------------------

Here are a few guidelines on when to choose a list or a tuple:

* If it needs to mutable: list

* If it needs to be immutable: tuple

  * (safety when passing to a function)

Otherwise ... taste and convention


Convention
-----------


Lists are Collections (homogeneous):
-- contain values of the same type
-- simplifies iterating, sorting, etc

tuples are mixed types:
-- Group multiple values into one logical thing
-- Kind of like simple C structs.


Other Considerations
--------------------

.. rst-class:: build

* Do the same operation to each element?

  * list

* Small collection of values which make a single logical item?

  * tuple

* To document that these values won't change?

  * tuple

* Build it iteratively?

  * list

* Transform, filter, etc?

  * list


More Documentation
------------------

For more information, read the list docs:

https://docs.python.org/3.5/library/stdtypes.html#mutable-sequence-types

(actually any mutable sequence....)

LAB
====

List Lab
---------

Let's play a bit with Python lists...

:ref: `exercise_list_lab`



Lightning Talk
---------------

|
| Robert Alford
|


Iteration
=========

.. rst-class:: build

Repetition, Repetition, Repetition, Repe...


For Loops
---------

We've seen simple iteration over a sequence with ``for ... in``:

.. code-block:: ipython

    In [170]: for x in "a string":
       .....:         print(x)
       .....:
    a
    s
    t
    r
    i
    n
    g


.. nextslide:: No Indexing Required

Contrast this with other languages, where you must build and use an ``index``:

.. code-block:: javascript

    for(var i = 0; i < arr.length; i++) {
        var value = arr[i];
        alert(i + ") " + value);

If you *do* need an index, you can use ``enumerate``:

.. code-block:: ipython

    In [140]: for idx, letter in enumerate('Python'):
       .....:     print(idx, letter, end=' ')
       .....:
    0 P 1 y 2 t 3 h 4 o 5 n


``range`` and ``for`` Loops
---------------------------

The ``range`` builtin is useful for looping a known number of times:

.. code-block:: ipython

    In [171]: for i in range(5):
       .....:     print(i)
       .....:
    0
    1
    2
    3
    4

But you don't really need to do anything at all with ``i``

.. nextslide::

In fact, it's a common convension to make this clear with a "nothing" name:

.. code-block:: ipython

    In [21]: for __ in range(5):
       ....:     print("*")
       ....:
    *
    *
    *
    *
    *


.. nextslide:: No Namespace

Be alert that a loop does not create a local namespace:

.. code-block:: ipython

    In [172]: x = 10
    In [173]: for x in range(3):
       .....:     pass
       .....:
    In [174]: x
    Out[174]: 2


.. nextslide:: Loop Control

Sometimes you want to interrupt or alter the flow of control through a loop.

Loops can be controlled in two ways, with ``break`` and ``continue``


.. nextslide:: Break

The ``break`` keyword will cause a loop to immediately terminate:

.. code-block:: ipython

    In [141]: for i in range(101):
       .....:     print(i)
       .....:     if i > 50:
       .....:         break
       .....:
    0 1 2 3 4 5... 46 47 48 49 50 51

.. nextslide:: Continue

The ``continue`` keyword will skip later statements in the loop block, but
allow iteration to continue:

.. code-block:: ipython

    In [143]: for in in range(101):
       .....:     if i > 50:
       .....:         break
       .....:     if i < 25:
       .....:         continue
       .....:     print(i, end=' ')
       .....:
       25 26 27 28 29 ... 41 42 43 44 45 46 47 48 49 50

.. nextslide:: else

For loops can also take an optional ``else`` block.

Executed only when the loop exits normally (not via break):

.. code-block:: ipython

    In [147]: for x in range(10):
       .....:     if x == 11:
       .....:         break
       .....: else:
       .....:     print('finished')
    finished
    In [148]: for x in range(10):
       .....:     if x == 5:
       .....:         print(x)
       .....:         break
       .....: else:
       .....:     print('finished')
    5

This is a really nice unique Python feature!

While Loops
-----------

The ``while`` keyword is for when you don't know how many loops you need.

It continues to execute the body until condition is not ``True``::

    while a_condition:
       some_code
       in_the_body

.. nextslide:: ``while`` vs. ``for``

``while``  is more general than ``for``

-- you can always express ``for`` as ``while``, but not always vice-versa.

``while``  is more error-prone -- requires some care to terminate

loop body must make progress, so condition can become ``False``

potential error -- infinite loops:

.. code-block:: python

    i = 0;
    while i < 5:
        print(i)


.. nextslide:: Terminating a while Loop

Use ``break``:

.. code-block:: ipython

    In [150]: while True:
       .....:     i += 1
       .....:     if i > 10:
       .....:         break
       .....:     print(i)
       .....:
    1 2 3 4 5 6 7 8 9 10

.. nextslide:: Terminating a while Loop

Set a flag:

.. code-block:: ipython

    In [156]: import random
    In [157]: keep_going = True
    In [158]: while keep_going:
       .....:     num = random.choice(range(5))
       .....:     print(num)
       .....:     if num == 3:
       .....:         keep_going = False
       .....:
    3

.. nextslide:: Terminating a While Loop

Use a condition:

.. code-block:: ipython

    In [161]: while i < 10:
       .....:     i += random.choice(range(4))
       .....:     print(i)
       .....:
    0 0 2 3 4 6 8 8 8 9 12


Similarities
------------

Both ``for`` and ``while`` loops can use ``break`` and ``continue`` for
internal flow control.

Both ``for`` and ``while`` loops can have an optional ``else`` block

In both loops, the statements in the ``else`` block are only executed if the
loop terminates normally (no ``break``)


String Features
================

.. rst-class:: center large

  Fun with Strings

Strings
---------

A string literal creates a string type

(we've seen this already...)

::

    "this is a string"

    'So is this'

    """and this also"""

You can also use ``str()``

.. code-block:: ipython

    In [256]: str(34)
    Out[256]: '34'

(demo)


String Methods
===============

String objects have a lot of methods.

Here are just a few:

String Manipulations
---------------------

``split`` and ``join``:

.. code-block:: ipython

    In [167]: csv = "comma, separated, values"
    In [168]: csv.split(', ')
    Out[168]: ['comma', 'separated', 'values']
    In [169]: psv = '|'.join(csv.split(', '))
    In [170]: psv
    Out[170]: 'comma|separated|values'


Case Switching
--------------

.. code-block:: ipython

    In [171]: sample = 'A long string of words'
    In [172]: sample.upper()
    Out[172]: 'A LONG STRING OF WORDS'
    In [173]: sample.lower()
    Out[173]: 'a long string of words'
    In [174]: sample.swapcase()
    Out[174]: 'a LONG STRING OF WORDS'
    In [175]: sample.title()
    Out[175]: 'A Long String Of Words'


Testing
--------

.. code-block:: ipython

    In [181]: number = "12345"
    In [182]: number.isnumeric()
    Out[182]: True
    In [183]: number.isalnum()
    Out[183]: True
    In [184]: number.isalpha()
    Out[184]: False
    In [185]: fancy = "Th!$ $tr!ng h@$ $ymb0l$"
    In [186]: fancy.isalnum()
    Out[186]: False


String Literals
-----------------

Common Escape Sequences::

    \\  Backslash (\)
    \a  ASCII Bell (BEL)
    \b  ASCII Backspace (BS)
    \n  ASCII Linefeed (LF)
    \r  ASCII Carriage Return (CR)
    \t  ASCII Horizontal Tab (TAB)
    \ooo  Character with octal value ooo
    \xhh  Character with hex value hh

for example -- for tab-separted values:

.. code-block:: ipython

    In [25]: s = "these\tare\tseparated\tby\ttabs"

    In [26]: print(s)
    these   are separated    by  tabs

https://docs.python.org/3/reference/lexical_analysis.html#string-and-bytes-literals
https://docs.python.org/3/library/stdtypes.html#string-methods

Raw Strings
------------

Add an ``r`` in front of the string literal:

Escape Sequences Ignored

.. code-block:: ipython

    In [408]: print("this\nthat")
    this
    that
    In [409]: print(r"this\nthat")
    this\nthat

**Gotcha**

.. code-block:: ipython

    In [415]: r"\"
    SyntaxError: EOL while scanning string literal

(handy for regex, windows paths...)


Ordinal values
--------------

Characters in strings are stored as numeric values:

* "ASCII" values: 1-127

* Unicode values -- 1 - 1,114,111 (!!!)

To get the value:

.. code-block:: ipython

    In [109]: for i in 'Chris':
       .....:     print(ord(i), end=' ')
    67 104 114 105 115
    In [110]: for i in (67,104,114,105,115):
       .....:     print(chr(i), end='')
    Chris

(these days, stick with ASCII, or use full Unicode: more on that in a few weeks)


Building Strings
-----------------

You can, but please don't do this:

.. code-block:: python

    'Hello ' + name + '!'

(I know -- we did that in the grid_printing excercise)

Do this instead:

.. code-block:: python

    'Hello {}!'.format(name)

It's much faster and safer, and easier to modify as code gets complicated.

https://docs.python.org/3/library/string.html#string-formatting

Old and New string formatting
-----------------------------

back in early python days, there was the string formatting operator: ``%``

.. code-block:: python

    " a string: %s and a number: %i "%("text", 45)

This is very similar to C-style string formatting (`sprintf`).

It's still around, and handy --- but ...

The "new" ``format()`` method is more powerful and flexible, so we'll focus on that in this class.

.. nextslide:: String Formatting

The string ``format()`` method:

.. code-block:: ipython

    In [62]: "A decimal integer is: {:d}".format(34)
    Out[62]: 'A decimal integer is: 34'

    In [63]: "a floating point is: {:f}".format(34.5)
    Out[63]: 'a floating point is: 34.500000'

    In [64]: "a string is the default: {}".format("anything")
    Out[64]: 'a string is the default: anything'


Multiple placeholders:
-----------------------

.. code-block:: ipython

    In [65]: "the number is {} is {}".format('five', 5)
    Out[65]: 'the number is five is 5'

    In [66]: "the first 3 numbers are {}, {}, {}".format(1,2,3)
    Out[66]: 'the first 3 numbers are 1, 2, 3'

The counts must agree:

.. code-block:: ipython

    In [67]: "string with {} formatting {}".format(1)
    ---------------------------------------------------------------------------
    IndexError                                Traceback (most recent call last)
    <ipython-input-67-a079bc472aca> in <module>()
    ----> 1 "string with {} formatting {}".format(1)

    IndexError: tuple index out of range


Named placeholders:
-------------------

.. code-block:: ipython


    In [69]: "Hello, {name}, whaddaya know?".format(name="Joe")
    Out[69]: 'Hello, Joe, whaddaya know?'

You can use values more than once, and skip values:

.. code-block:: ipython

    In [73]: "Hi, {name}. Howzit, {name}?".format(name='Bob')
    Out[73]: 'Hi, Bob. Howzit, Bob?'

.. nextslide::

The format operator works with string variables, too:

.. code-block:: ipython

    In [80]: s = "{:d} / {:d} = {:f}"

    In [81]: a, b = 12, 3

    In [82]: s.format(a, b, a/b)
    Out[82]: '12 / 3 = 4.000000'

So you can dynamically build a format string

Complex Formatting
------------------

There is a complete syntax for specifying all sorts of options.

It's well worth your while to spend some time getting to know this
`formatting language`_. You can accomplish a great deal just with this.

.. _formatting language: https://docs.python.org/3/library/string.html#format-specification-mini-language


One Last Trick
---------------

.. rst-class:: left

For some of the exercises, you'll need to interact with a user at the
command line.

There's a nice built in function to do this - ``input``:

.. code-block:: ipython

    In [85]: fred = input('type something-->')
    type something-->I've typed something

    In [86]: print(fred)
    I've typed something

This will display a prompt to the user, allowing them to input text and
allowing you to bind that input to a symbol.


String Formatting LAB
=====================

Let's play with these a bit:

:ref:`exercise_string_formatting`

Homework
========

Task 1
------

Finish the List Lab from class

Finish the string formatting lab

Task 2
------

.. rst-class:: mlarge

ROT13

:ref:`exercise_rot13`

Task 3
------

.. rst-class:: mlarge

Mail Room

:ref:`exercise_mailroom`

Reading
-------

Think Python: Chapters 11, 13, 14

Learn Python the Hard way: 15-17, 39

Dive Into Python3: Sections 2.6, 2.7, 11

Next Week:
===========

.. rst-class:: mlarge

    **Lightning talks next week:**

Andrey Gusev

Cheryl Ohashi

Maxwell MacCamy






