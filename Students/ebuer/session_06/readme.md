#Session 6

###Notes from last week

If you use the dict.viewkeys() or dict.viewitems() to get access to parts of a dictionary the variable created is linked to the dictionary and will update as the dictionary updates without risking changing the dictionary.  Can be very useful.

```python
def f(*args, **kwargs):
    print args
    print kwargs

f(1,2,3, fred = 45, john = 32)
```

####os.path.join() using tuple *args
```python
import os
os.path.join()  # joins strings as a path
os.path.join('this', 'that', 'other')

```

note for evaluations, you can always convert a numerical to boolean using the bool(value) function

####Rich comparisons:

```python
import numpy as np
arr = np.arange(4)

arr == 2 #retuns an array

a2 = arr == 2 # a2 is now an array of true/false values
```

Binary mode for files:
    infile = open(infilename, 'rb')  # this opens in binary mode via -b flag
    outfile = open(outfile, 'wb')   # writes using binary format

This is really important when you're working with files that are not text since there is incompatibility between unix and windows binary files and the way they are written

####List comprehensions can be used for compact looping

```python
for i, st in zip(list1, list2):
    # do stuff here
```

**Collections Module**

+ defalutdict -- does dict.setdefault() for you
+ namedtuple
+ deque -- double ended que
+ counter

This will create an empty list in the dictionary by default:

```python
from collections import defaultdict
trigrams = defaultdict(list) # note list without parens is just the list object
trigrams[pair].append(follower)
```

Use a counter to ensure unique values as you tabulate

__If your code is difficult to write tests for, then it probably isn't very good code and you should rethink your life__

Test driven development often works particularly well with refactoring -- the code is currently working and you start moving things around and changing variables to be more efficient/cleaner/etc

####lambda functions

In python a function is an object, it can be called by name and passed around as needed

```python
f = lambda x, y: x+y  #here the function has already been assigned a name: f

l= [lambda x, y = x + y]
type(l[0])

# equivalent to the above:
def fun(x,y):
    return x + y
l = [fun]

l = []
for i in range(3):
    l.append(lambda x, e=i: x ** e)

for f in l:
    print f
```

lambda can also take keyword arguments, note that the keyword argument is evaluated when the function is created

####Applications of lambda: map() and filter()
Map applies a function to each element in a sequence then returns the resulting new list -- very useful!

```python
l = [2, 5, 7, 9, 11, 13]
map(lambda x: x * 2 + 10, l)

filter(lambda x:not x % 2, l)

filter(None)  # returns all the items that evaluate to True
```

Content can only be an expression, not a statement

Expression: always evaluates to a value and returns one

Statement: does not necessarily return a value e.g 'print' statement

Note about functional programming: you're not supposed to change lists in place, each process or operation should return a new list

####Applications of lambda: reduce()

```python
l = [2, 5, 7, 9, 11, 13]
reduce(lambda x, y: x * y + 10, l)
```

**Note:** lambda and list comprehensions frequently can both be used to achieve the same results, **except** for reduce()

map-reduce is a big concept in parallel processing of big data in NoSQL databases.  Therefore just a good concept to be aware of.

```python
l = [(45,1), (4, 5), (2, 3), (1, 2)]
# function takes list element and returns element[1]
l.sort(key= lambda t: t[1])

#reverse through use of keyword
l.sort(key= lambda t: t[1], reverse = True)
```

