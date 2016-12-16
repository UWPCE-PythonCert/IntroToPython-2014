#!/usr/bin/env python3

# getting an arbitrary item from a dictionary

"""
in class, we spend a bi tof time figureing out how to get an arbitrary
item from a dictionary without removing it: dict.popitem() gets you an
arbitrary item, but it removes it also. In this case, we didn't want to
remove it

In this case, we only needed and arbitrary key, but the principle is
the same if you want the whole item.

"""

import random

# make a tiny little dict to test with:
tiny = {'that': 2, 'this': 3, 'the other': 56}

# One simple solution is to take advantage of popitem() and then put it back:
item = tiny.popitem()
print("An arbitrary key")
print(item[0])
# put it back:
tiny.update((item,))
# it's still the same
print(tiny)

# but this is pretty ugly:
#  - we only want a key but we got the entire item, so we need to pull the key out of that
#  - even worse, we have to save the entire item and put it back
#  So this is pretty unsatisfactory


# solution we used in class:
print("An arbitrary key")
print(list(tiny.keys())[0])

# This works fine -- the list of the keys is in arbitrary order, so
# grabbing the first one gets you an arbitrary key
#
# This also has the advantage that you could easily adapt it to give you a ransom key instead:
print("a random key")
print(random.choice(list(tiny.keys())))

# However -- the downside of this is that you are making an entire list of all the keys,
# just to toss it away afterward. Computers are fast and have lots of memory, so probably
# not a big deal, but it is good to think it terms of efficient algorithms, if they don't
# complicate your code. This is why dict.keys() does not return a list (in py3):
print("type of keys():", type(tiny.keys()))

# the dict_Keys type is an "iterable" -- something you can iterate through with a for loop:
for key in tiny.keys():
    print(key)

# The dict_keys object "gives" the for loop each key, one at a time, without ever making
# a full copy of them all.

# So we could take advantage of this to get an arbitrary key without making an entire list
# first:

for key in tiny.keys():
    print("An arbitrary key")
    print(key)
    break
# (notice that it's the SAME arbitrary key as the first item of the list method --
# it IS the first item off the list.

# So this leads us to the solution we ALMOST got to in class:
#
# for loops use the "iterator protocol". You can use that directly if you want to control how
# things are iterated over.
#
# We'll get into this in detail later in the class, but the (very) short version is that the
# next() function returns the next item from an iterator. So if you call it only once, you get
# the first item:

print("An arbitrary key")
print(next(iter(tiny.keys())))

# Wait! what is that `iter()` call? the `iter()` function takes a "iterable" and returns and
# "iterator" from it.  An "iterable" is something you can iterate over -- an "iterator" is the
# actual object that saves state and returns the actual items.
# You can't call next() on an iterable:

next(tiny.keys())

# you get a type error:
# TypeError: 'dict_keys' object is not an iterator


# So what should one do in this case? Isn't part of Python's Philosophy:
#   There is only one way to do it?
#
# This is why, in class, I thought there should be a quick and easy way to do this.
#
# However, on further thought, this is pretty unusual thing to need to do:
#  .popitems() makes sense -- you sometimes need to pull out a item from a dict one by one, and
# do something with it, and want it removed from the dict. you are likeley to do
# this over an over again until the dict is empty.
# but not caring which item you get, but wanting the dict to remain unaltered is a pretty rare use case.
#
# so that's why there isn't one obvious way to do it

# I think that:
#
#  next(iter(tiny.keys()))
#
#  is probably the most "pythonic" way to do it -- compact and efficient
#  However, it does require fairly advanced understanding of iterables and iterators.
#  So:
#
#  list(tiny.keys())[0]
#
#  is a fine option. And leaves the door open for using random.choice, too.


