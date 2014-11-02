Session 5
----

More Dictionaries and functions
----

```python
    import collections
        collections.OrderedDict?  # module has added collections / dict tools
        d = collections.OrderedDict()
```

Sorted function takes an iterable object and a key, a sorted object is returned

```python
    for key in sorted(d):
        print key

    punctuation = string.punctuation
```

random module choice method  -- pretty much any module you can find is fair game now

random.randint(2,10)

each sentence was constructed as a list for easy indexing of the words, use of several string tools to format the list:

+ string.capitalize
+ list.extend(new_sentence)

Look further at the solution for details. Basic construction matches what has already been solved: dictionary for values, printing uses a list.

Advanced Argument Passing
----

When defining a function you can specify only what you need, the order is up to you.

A common idiom:
```python
def fun(x, y=None):
    do your work here

def(x, y, w=0, h=0):
    print "position: %s, %s, -- %s, %s" %(x, y, w, h)

pos = (5, 6)

f(*pos, h = 7)
```

f(*position, **size)

**positional arguments** (args) are a tuple
**keyword arguments** (kwargs) are a dictionary

```python
def f(*args, **kwargs):
    print 'the positional arguments are: ', args
    print 'the keyword arguments are: ', kwargs
```

os.path.join will take any number of file and directory names and stitch them together into a path -- an example of a limitless number of args

.format also takes an unlimited number of arguments

```python
formatter = "My name is {first} {last}"  # note keyword arguments are unspecified
person = {'first': 'chris', 'last': 'Barker'}
formatter.format(**person)  # passing the whole dictionary!

formatter = 'Myname is {1} {0}'
formatter.format('Barker', 'Chris')

person = ('Barker', 'Chris')
formatter.format(*person)  # passing tuple argument, position corresponds to numbers


```

**Dont' forget** about the type() tool, which allows inspection of variable types

*args and **kwargs are very important

for the mailroom think about using a dictionary of information that just is passed directly into the letter

###The Copy Module

most objects have a copy method, but shallow copies remained linked to the original source

list1 = ['a', 'b', 'c']

list2 = copy.deepcopy(list1) # creates a copy of each element that is independent of the original

if a function is created with a mutable as a default value

```python
def run(x, a=[]):
    a.append(x)
    return a
```

The list that is defined by the function remains in the environment.  Calling the function several times will continue to use the 'a' list in this case

This is avoided by __never__ using a mutable as the default variable.

```python
def run(x, a = None):
    if a is None:
        a = []
    a.append(x)
    return a
```

oceanpython.org

##List Comprehension

```python
[i for i in range(5)] # basic loop

new_list = [expression for var in a_list for var2 in a_list2] # nested loop, outer product

l = ['this', 'that', 'the', 'other']

l2 = [s.upper() for s in l]

[(i, j) for i in range(3) for j in range(4, 6)] #same as nested for loop

```

Usually we want to apply a conditional as well:

```python
[s.upper() for s in l if s.startswith('t')]
```

Comprehensions can also be applied to sets {a, b, c}, and dicts.  The syntax appears to be very similar
```python

new_dict = { key:value for variable in a_sequence}

new_dict = {}
for key in a_list:
    new_dict[key] = value


s = 'a not very long string'
vowels = set('aeiou')
{let for let in s if let in vowels}
```

**Note** searching sets offers two advantages over lists.

1. Sets enforce only unique values
2. Sets are hashable and therefore can be searched much faster than lists

##Testing

using unittest

```python
import unittest
class MyTests(unittest.TestCase):
    check slides
```

####Testing Modules

    + unittest  comes with all versions of python
    + Nose
    + pytest -- chosen class module for unit testing

