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

    +string.capitalize
    +list.extend(new_sentence)

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

f( *pos, h = 7)
```

f( *position, **size)

positional arguments are a tuple
keyword arguments are a dictionary

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




