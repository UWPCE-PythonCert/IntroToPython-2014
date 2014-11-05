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

def cigar_party(cigars, is_weekend):
    