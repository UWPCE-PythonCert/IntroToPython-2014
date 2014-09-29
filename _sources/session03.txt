*********************************************************
Session Three: Sequences, Iteration and String Formatting
*********************************************************

Review/Questions
================

Review of Previous Session
--------------------------

.. rst-class:: build

* Functions
* Booleans
* Modules


Homework Review
---------------

.. rst-class:: center large

Any questions that are nagging?


Sequences
=========

.. rst-class:: center large

Ordered collections of objects


What is a Sequence?
-------------------

Remember Duck Typing?  A *sequence* can be considered as anything that supports
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

There are seven builtin types in Python that are *sequences*:

* strings
* Unicode strings
* lists
* tuples
* bytearrays
* buffers
* array.arrays
* xrange objects (almost)

For this class, you won't see much beyond the string types, lists, tuples -- the rest are pretty special purpose.

But what we say today applies to all sequences (with minor caveats)


Indexing
--------

Items in a sequence may be looked up by *index* using the subscription
operator: ``[]``

Indexing in Python always starts at zero.

.. code-block:: ipython

    In [98]: s = u"this is a string"
    In [99]: s[0]
    Out[99]: u't'
    In [100]: s[5]
    Out[100]: u'i'


.. nextslide::

You can use negative indexes to count from the end:

.. code-block:: ipython

    In [105]: s = u"this is a string"
    In [106]: s[-1]
    Out[106]: u'g'
    In [107]: s[-6]
    Out[107]: u's'

.. nextslide::

Indexing beyond the end of a sequence causes an IndexError:

.. code-block:: ipython

    In [4]: s = [0, 1, 2, 3]
    In [5]: s[4]
    ---------------------------------------------------------------------------
    IndexError                                Traceback (most recent call last)
    <ipython-input-5-42efaba84d8b> in <module>()
    ----> 1 s[4]

    IndexError: list index out of range


Slicing
-------

Slicing a sequence creates a new sequence with a range of objects from the
original sequence.

It also uses the subscription operator (``[]``), but with a twist.

``sequence[start:finish]`` returns all sequence[i] for which start <= i < finish:

.. code-block:: ipython

    In [121]: s = u"a bunch of words"
    In [122]: s[2]
    Out[122]: u'b'
    In [123]: s[6]
    Out[123]: u'h'
    In [124]: s[2:6]
    Out[124]: u'bunc'
    In [125]: s[2:7]
    Out[125]: u'bunch'

.. nextslide:: Helpful Hint

Think of the indexes as pointing to the spaces between the items::

       a       b   u   n   c   h       o   f
     |   |   |   |   |   |   |   |   |   |
     0   1   2   3   4   5   6   7   8   9



.. nextslide:: Slicing

You do not have to provide both ``start`` and ``finish``:

.. code-block:: ipython

    In [6]: s = u"a bunch of words"
    In [7]: s[:5]
    Out[7]: u'a bun'
    In [8]: s[5:]
    Out[8]: u'ch of words'

Either ``0`` or ``len(s)`` will be assumed, respectively.

You can combine this with the negative index to get the end of a sequence:

.. code-block:: ipython

    In [4]: s = u'this_could_be_a_filename.txt'
    In [5]: s[:-4]
    Out[5]: u'this_could_be_a_filename'
    In [6]: s[-4:]
    Out[6]: u'.txt'


Why start from zero?
--------------------

Python indexing feels 'weird' to some folks -- particularly those that don't come with a background in the C family of languages.

Why is the "first" item indexed with zero?

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

    In [289]: string = u"a fairly long string"
    In [290]: string[0:15]
    Out[290]: u'a fairly long s'
    In [291]: string[0:15:2]
    Out[291]: u'afil ogs'
    In [292]: string[0:15:3]
    Out[292]: u'aallg'
    In [293]: string[::-1]
    Out[293]: u'gnirts gnol ylriaf a'


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

    In [20]: s = u"This is a long string"
    In [21]: u"long" in s
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

    In [25]: s1 = u"left"
    In [26]: s2 = u"right"
    In [27]: s1 + s2
    Out[27]: u'leftright'
    In [28]: (s1 + s2) * 3
    Out[28]: u'leftrightleftrightleftright'


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

    In [36]: s = u"how long is this, anyway?"
    In [37]: len(s)
    Out[37]: 25

Remember, Python sequences are zero-indexed, so the last index in a sequence is
``len(s) - 1``:

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

    In [42]: all_letters = u"thequickbrownfoxjumpedoverthelazydog"
    In [43]: min(all_letters)
    Out[43]: u'a'
    In [44]: max(all_letters)
    Out[44]: u'z'

Why are those the answers you get? (hint: ``ord(u'a')``)


.. nextslide:: Index

All sequences also support the ``index`` method, which returns the index of the
first occurence of an item in the sequence:

.. code-block:: ipython

    In [46]: all_letters.index(u'd')
    Out[46]: 21

This causes a ``ValueError`` if the item is not in the sequence:

.. code-block:: ipython

    In [47]: all_letters.index(u'A')
    ---------------------------------------------------------------------------
    ValueError                                Traceback (most recent call last)
    <ipython-input-47-2db728a46f78> in <module>()
    ----> 1 all_letters.index(u'A')

    ValueError: substring not found

.. nextslide:: Count

A sequence can also be queried for the number of times a particular item
appears:

.. code-block:: ipython

    In [52]: all_letters.count(u'o')
    Out[52]: 4
    In [53]: all_letters.count(u'the')
    Out[53]: 2

This does not raise an error if the item you seek is not present:

.. code-block:: ipython

    In [54]: all_letters.count(u'A')
    Out[54]: 0


Iteration
---------

.. rst-class:: center large

More on this in a while.


Lists, Tuples...
================

.. rst-class:: center large

The *other* sequence types.

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


.. nextslide:: List Elements

The elements contained in a list need not be of a single type.

Lists are *heterogenous*, *ordered* collections.

Each element in a list is a value, and can be in multiple lists and have
multiple names (or no name)

.. code-block:: ipython

    In [9]: name = u'Brian'
    In [10]: a = [1, 2, name]
    In [11]: b = [3, 4, name]
    In [12]: a[2]
    Out[12]: u'Brian'
    In [13]: b[2]
    Out[13]: u'Brian'
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
    In [158]: t = (3,)
    In [160]: type(t)
    Out[160]: tuple

.. nextslide:: Converting to Tuple

You can also use the ``tuple`` type object to convert any sequence into a
tuple:

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

    In [23]: name = u'Brian'
    In [24]: other = name
    In [25]: a = (1, 2, name)
    In [26]: b = (3, 4, other)
    In [27]: for i in range(3):
       ....:     print a[i] is b[i],
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

    In [28]: food = [u'spam', u'eggs', u'ham']
    In [29]: food
    Out[29]: [u'spam', u'eggs', u'ham']
    In [30]: food[1] = u'raspberries'
    In [31]: food
    Out[31]: [u'spam', u'raspberries', u'ham']


.. nextslide:: Tuples Are Not

And repeat the exercise with a Tuple:

.. code-block:: ipython

    In [32]: food = (u'spam', u'eggs', u'ham')
    In [33]: food
    Out[33]: (u'spam', u'eggs', u'ham')
    In [34]: food[1] = u'raspberries'
    ---------------------------------------------------------------------------
    TypeError                                 Traceback (most recent call last)
    <ipython-input-34-0c3401794933> in <module>()
    ----> 1 food[1] = u'raspberries'

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

    In [15]: words = [u'one', u'three', u'rough', u'sad', u'goof']

    In [16]: for word in words:
       ....:     bins[len(word)-1].append(word)
       ....:

So, what is going to be in ``bins`` now?

.. nextslide:: There is Only **One** Bin

.. code-block:: ipython

    In [65]: bins
    Out[65]:
    [[u'one', u'three', u'rough', u'sad', u'goof'],
     [u'one', u'three', u'rough', u'sad', u'goof'],
     [u'one', u'three', u'rough', u'sad', u'goof'],
     [u'one', u'three', u'rough', u'sad', u'goof'],
     [u'one', u'three', u'rough', u'sad', u'goof']]

We multiplied a sequence containing a single *mutable* object.

We got a list containing five pointers to a single *mutable* object.


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

http://www.python.org/2/library/stdtypes.html#mutable-sequence-types

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

    In [74]: food = [u'spam', u'eggs', u'ham']
    In [75]: food.append(u'sushi')
    In [76]: food
    Out[76]: [u'spam', u'eggs', u'ham', u'sushi']
    In [77]: food.insert(0, u'beans')
    In [78]: food
    Out[78]: [u'beans', u'spam', u'eggs', u'ham', u'sushi']
    In [79]: food.extend([u'bread', u'water'])
    In [80]: food
    Out[80]: [u'beans', u'spam', u'eggs', u'ham', u'sushi', u'bread', u'water']


.. nextslide:: More on Extend

You can pass any sequence to ``.extend()``:

.. code-block:: ipython

    In [85]: food
    Out[85]: [u'beans', u'spam', u'eggs', u'ham', u'sushi', u'bread', u'water']
    In [86]: food.extend(u'spaghetti')
    In [87]: food
    Out[87]:
    [u'beans', u'spam', u'eggs', u'ham', u'sushi', u'bread', u'water',
     u's', u'p', u'a', u'g', u'h', u'e', u't', u't', u'i']


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

This looks benign enough, but changing a list while you are iterating over it
can be the cause of some pernicious bugs.


.. nextslide:: The Problem

For example:

.. code-block:: ipython

    In [121]: list = range(10)
    In [122]: list
    Out[122]: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    In [123]: for x in list:
       .....:     list.remove(x)
       .....:
    In [124]: list
    Out[124]: [1, 3, 5, 7, 9]

Was that what you expected?

.. nextslide:: The Solution

Iterate over a copy, and mutate the original:

.. code-block:: ipython

    In [126]: list = range(10)
    In [127]: for x in list[:]:
       .....:     list.remove(x)
       .....:
    In [128]: list
    Out[128]: []


.. nextslide:: Just Say It, Already

Okay, so we've done this a bunch already, but let's state it out loud.

You can iterate over a sequence.

.. code-block:: python

    for element in sequence:
        do_something(element)


Again, we'll touch more on this in a short while, but first a few more words
about Lists and Tuples.


Miscellaneous List Methods
--------------------------


These methods change a list in place and are not available on immutable
sequence types.

``.reverse()``

.. code-block:: ipython

    In [129]: food = [u'spam', u'eggs', u'ham']
    In [130]: food.reverse()
    In [131]: food
    Out[131]: [u'ham', u'eggs', u'spam']

``.sort()``

.. code-block:: ipython

    In [132]: food.sort()
    In [133]: food
    Out[133]: [u'eggs', u'ham', u'spam']

Because these methods mutate the list in place, they have a return value of
``None``


.. nextslide:: Custom Sorting

``.sort()`` can take an optional ``key`` parameter.

It should be a function that takes one parameter (list items one at a time) and
returns something that can be used for sorting:

.. code-block:: ipython

    In [137]: def third_letter(string):
       .....:     return string[2]
       .....:
    In [138]: food.sort(key=third_letter)
    In [139]: food
    Out[139]: [u'spam', u'eggs', u'ham']



List Performance
----------------

.. rst-class:: build

* indexing is fast and constant time: O(1)
* x in s proportional to n: O(n)
* visiting all is proportional to n: O(n)
* operating on the end of list is fast and constant time: O(1) 

  * append(), pop()

* operating on the front (or middle) of the list depends on n: O(n)

  * pop(0), insert(0, v) 
  * But, reversing is fast. Also, collections.deque

 http://wiki.python.org/moin/TimeComplexity


Choosing Lists or Tuples
------------------------

Here are a few guidelines on when to choose a list or a tuple:

* If it needs to mutable: list

* If it needs to be immutable: tuple

  * (safety when passing to a function)

Otherwise ... taste and convention


.. nextslide:: Convention

Lists are Collections (homogeneous):
-- contain values of the same type 
-- simplifies iterating, sorting, etc

tuples are mixed types:
-- Group multiple values into one logical thing
-- Kind of like simple C structs.


.. nextslide:: Other Considerations

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

http://docs.python.org/2/library/stdtypes.html#mutable-sequence-types

(actually any mutable sequence....)


Iteration
=========

.. rst-class:: build

Repetition, Repetition, Repetition, Repe...


For Loops
---------

We've seen simple iteration over a sequence with ``for ... in``:

.. code-block:: ipython

    In [170]: for x in "a string":
       .....:         print x
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

    for(var i=0; i<arr.length; i++) {
        var value = arr[i];
        alert(i + ") " + value);

If you need an index, though you can use ``enumerate``:

.. code-block:: ipython

    In [140]: for idx, letter in enumerate(u'Python'):
       .....:     print idx, letter,
       .....:
    0 P 1 y 2 t 3 h 4 o 5 n


.. nextslide:: ``range`` and For Loops

The ``range`` builtin is useful for looping a known number of times:

.. code-block:: ipython

    In [171]: for i in range(5):
       .....:     print i
       .....:
    0
    1
    2
    3
    4

But you don't really need to do anything at all with ``i``


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
       .....:     print i
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
       .....:     print i,
       .....:
       25 26 27 28 29 ... 41 42 43 44 45 46 47 48 49 50

.. nextslide:: Else

For loops can also take an optional ``else`` block.

Executed only when the loop exits normally (not via break):

.. code-block:: ipython

    In [147]: for x in range(10):
       .....:     if x == 11:
       .....:         break
       .....: else:
       .....:     print 'finished'
    finished
    In [148]: for x in range(10):
       .....:     if x == 5:
       .....:         print x
       .....:         break
       .....: else:
       .....:     print 'finished'
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

-- you can always express ``for`` as ``while``,

but not always vice-versa.

``while``  is more error-prone -- requires some care to terminate

loop body must make progress, so condition can become ``False``

potential error -- infinite loops:

.. code-block:: python

    i = 0;
    while i < 5:
        print i


.. nextslide:: Terminating a while Loop

Use ``break``:

.. code-block:: ipython

    In [150]: while True:
       .....:     i += 1
       .....:     if i > 10:
       .....:         break
       .....:     print i
       .....:
    1 2 3 4 5 6 7 8 9 10

.. nextslide:: Terminating a while Loop

Set a flag:

.. code-block:: ipython

    In [156]: import random
    In [157]: keep_going = True
    In [158]: while keep_going:
       .....:     num = random.choice(range(5))
       .....:     print num
       .....:     if num == 3:
       .....:         keep_going = False
       .....:
    3

.. nextslide:: Terminating a While Loop

Use a condition:

.. code-block:: ipython

    In [161]: while i < 10:
       .....:     i += random.choice(range(4))
       .....:     print i
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
=================

.. rst-class:: center large

  Fun with Strings


Manipulations
-------------

``split`` and ``join``:

.. code-block:: ipython

    In [167]: csv = "comma, separated, values"
    In [168]: csv.split(', ')
    Out[168]: ['comma', 'separated', 'values']
    In [169]: psv = '|'.join(csv.split(', '))
    In [170]: psv
    Out[170]: 'comma|separated|values'


.. nextslide:: Case Switching

.. code-block:: ipython

    In [171]: sample = u'A long string of words'
    In [172]: sample.upper()
    Out[172]: u'A LONG STRING OF WORDS'
    In [173]: sample.lower()
    Out[173]: u'a long string of words'
    In [174]: sample.swapcase()
    Out[174]: u'a LONG STRING OF WORDS'
    In [175]: sample.title()
    Out[175]: u'A Long String Of Words'


.. nextslide:: Testing

.. code-block:: ipython

    In [181]: number = u"12345"
    In [182]: number.isnumeric()
    Out[182]: True
    In [183]: number.isalnum()
    Out[183]: True
    In [184]: number.isalpha()
    Out[184]: False
    In [185]: fancy = u"Th!$ $tr!ng h@$ $ymb0l$"
    In [186]: fancy.isalnum()
    Out[186]: False


Ordinal values
--------------

"ASCII" values: 1-127

"ANSI" values: 1-255

To get the value:

.. code-block:: ipython

    In [109]: for i in 'Chris':
       .....:     print ord(i),
    67 104 114 105 115
    In [110]: for i in (67,104,114,105,115):
       .....:     print chr(i),
    C h r i s


Building Strings
----------------

You can, but please don't do this:

.. code-block:: python

    'Hello ' + name + '!'

Do this instead:

.. code-block:: python

    'Hello %s!' % name

It's much faster and safer, and easier to modify as code gets complicated.

http://docs.python.org/library/stdtypes.html#string-formatting-operations


.. nextslide:: String Formatting

The string format operator: ``%``

.. code-block:: ipython

    In [261]: u"an integer is: %i" % 34
    Out[261]: u'an integer is: 34'
    In [262]: u"a floating point is: %f" % 34.5
    Out[262]: u'a floating point is: 34.500000'
    In [263]: u"a string is: %s" % u"anything"
    Out[263]: u'a string is: anything'

.. nextslide:: More Placeholders

Multiple placeholders:

.. code-block:: ipython

    In [264]: u"the number %s is %i" % (u'five', 5)
    Out[264]: u'the number five is 5'
    In [266]: u"the first 3 numbers are: %i, %i, %i" % (1,2,3)
    Out[266]: u'the first 3 numbers are: 1, 2, 3'

The counts must agree:

.. code-block:: ipython

    In [187]: u"string with %i formatting %s" % (1, )
    ---------------------------------------------------------------------------
    ...
    TypeError: not enough arguments for format string


.. nextslide::

Named placeholders:

.. code-block:: ipython

    In [191]: u"Hello, %(name)s, whaddaya know?" % {u'name': "Joe"}
    Out[191]: u'Hello, Joe, whaddaya know?'

You can use values more than once, and skip values:

.. code-block:: ipython

    In [193]: u"Hi, %(name)s. Howzit, %(name)s?" % {u'name': u"Bob", u'age': 27}
    Out[193]: u'Hi, Bob. Howzit, Bob?'


.. nextslide:: New Formatting

In more recent versions of Python (2.6+) this is `being phased out`_ in favor of the ``.format()`` method on strings.

.. code-block:: ipython

    In [194]: u"Hello, {}, how's your {}".format(u"Bob", u"wife")
    Out[194]: u"Hello, Bob, how's your wife"
    In [195]: u"Hi, {name}. How's your {relation}?".format(name=u'Bob', relation=u'wife')
    Out[195]: u"Hi, Bob. How's your wife?"


.. nextslide:: Complex Formatting

For both of these forms of string formatting, there is a complete syntax for
specifying all sorts of options.

It's well worth your while to spend some time getting to know this
`formatting language`_. You can accomplish a great deal just with this.

.. _formatting language: https://docs.python.org/2/library/string.html#format-specification-mini-language

.. _being phased out: https://docs.python.org/2/library/stdtypes.html#str.format


One Last Trick
==============

.. rst-class:: left

For some of your homework, you'll need to interact with a user at the
command line.

.. rst-class:: left

There's a nice builtin function to do this - ``raw_input``:

.. rst-class:: left

.. code-block:: python

    In [196]: fred = raw_input('type something-->')
    type something-->;alksdjf
    In [197]: fred
    Out[197]: ';alksdjf'

.. rst-class:: left

This will display a prompt to the user, allowing them to input text and
allowing you to bind that input to a symbol.


Homework
========

Task 1
------

List Lab (after http://www.upriss.org.uk/python/session5.html)

In your student folder, create a new file called ``list_lab.py``.

The file should be an executable python script. That is to say that one
should be able to run the script directly like so:

.. code-block:: bash

    $ ./list_lab.py

Add the file to your clone of the repository and commit changes frequently
while working on the following tasks. When you are done, push your changes to
GitHub and issue a pull request.

When the script is run, it should accomplish the following four series of
actions:

.. nextslide:: Series 1

- Create a list that contains "Apples", "Pears", "Oranges" and "Peaches".
- Display the list.
- Ask the user for another fruit and add it to the end of the list.
- Display the list.
- Ask the user for a number and display the number back to the user and the
  fruit corresponding to that number (on a 1-is-first basis).
- Add another fruit to the beginning of the list using "+" and display the
  list.
- Add another fruit to the beginning of the list using insert() and display the
  list.
- Display all the fruits that begin with "P", using a for loop.


.. nextslide:: Series 2

Using the list created in series 1 above:

- Display the list.
- Remove the last fruit from the list.
- Display the list.
- Ask the user for a fruit to delete and find it and delete it.
- (Bonus: Multiply the list times two. Keep asking until a match is found. Once
  found, delete all occurrences.)

.. nextslide:: Series 3

Again, using the list from series 1:

- Ask the user for input displaying a line like "Do you like apples?"
- for each fruit in the list (making the fruit all lowercase).
- For each "no", delete that fruit from the list.
- For any answer that is not "yes" or "no", prompt the user to answer with one
  of those two values (a while loop is good here):
- Display the list.

.. nextslide:: Series 4

Once more, using the list from series 1:

- Make a copy of the list and reverse the letters in each fruit in the copy.
- Delete the last item of the original list. Display the original list and the
  copy.


Task 2
------

ROT13

The ROT13 encryption scheme is a simple substitution cypher where each letter
in a text is replace by the letter 13 away from it (imagine the alphabet as a
circle, so it wraps around).

Add a python module named ``rot13.py`` to your student folder. This module
should provide at least one function called ``rot13`` that takes any amount of
text and returns that same text encrypted by ROT13.

This function should preserve whitespace, punctuation and capitalization.

Your module should include an ``if __name__ == '__main__':`` block with tests
that demonstrate that your ``rot13`` function and any helper functions you add
work properly.

.. nextslide:: A bit more

There is a "short-cut" available that will help you accomplish this task. Some
spelunking in `the documentation for strings`_ should help you to find it. If
you do find it, using it is completely fair game.

.. _the documentation for strings: https://docs.python.org/2/library/stdtypes.html#string-methods

As usual, add your new file to your local clone right away.  Make commits early and often and include commit messages that are descriptive and concise.

When you are done, push your changes to github and issue a pull request.


Task 3
------

"Mail Room"

You work in the mail room at a local charity. Part of your job is to write
incredibly boring, repetitive emails thanking your donors for their generous
gifts. You are tired of doing this over an over again, so you've decided to let Python help you out of a jam.

Write a small command-line script called ``mailroom.py``.  As with Task 1, This script should be executable. The script should accomplish the following goals:

* It should have a data structure that holds a list of your donors and a
  history of the amounts they have donated. This structure should be populated
  at first with at least five donors, with between 1 and 3 donations each
* The script should prompt the user (you) to choose from a menu of 2 actions:
  'Send a Thank You' or 'Create a Report'.

.. nextslide:: Sending a Thank You

* If the user (you) selects 'Send a Thank You', prompt for a Full Name.

  * If the user types 'list', show them a list of the donor names and re-prompt
  * If the user types a name not in the list, add that name to the data
    structure and use it.
  * If the user types a name in the list, use it.
  * Once a name has been selected, prompt for a donation amount.
  * Verify that the amount is in fact a number, and re-prompt if it isn't.
  * Once an amount has been given, add that amount to the donation history of
    the selected user.
  * Finally, use string formatting to compose an email thanking the donor for
    their generous donation. Print the email to the terminal and return to the
    original prompt.

**It is fine to forget new donors once the script quits running.**

.. nextslide:: Creating a Report

* If the user (you) selected 'Create a Report' Print a list of your donors,
  sorted by total historical donation amount.

  - Include Donor Name, total donated, number of donations and average donation
    amount as values in each row.
  - Using string formatting, format the output rows as nicely as possible.  The
    end result should be tabular (values in each column should align with those
    above and below)
  - After printing this report, return to the original prompt.

* At any point, the user should be able to quit their current task and return
  to the original prompt.

* From the original prompt, the user should be able to quit the script cleanly

.. nextslide:: Guidelines

First, factor your script into separate functions. Each of the above
tasks can be accomplished by a series of steps.  Write discreet functions
that accomplish individual steps and call them.

Second, use loops to control the logical flow of your program. Interactive
programs are a classic use-case for the ``while`` loop.

Put the functions you write into the script at the top.

Put your main interaction into an ``if __name__ == '__main__'`` block.

Finally, use only functions and the basic Python data types you've learned
about so far. There is no need to go any farther than that for this assignment.

.. nextslide:: Submission

As always, put the new file in your student directory in a ``session03``
directory, and add it to your clone early. Make frequent commits with
good, clear messages about what you are doing and why.

When you are done, push your changes and make a pull request.
