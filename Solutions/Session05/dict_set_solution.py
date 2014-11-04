#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
dict/set lab solutions: Chris' version.
"""

# Create a dictionary containing "name", "city", and "cake" for
# "Chris" from "Seattle" who likes "Chocolate".


d = {u"name": u"Chris",
     u"city": u"Seattle",
     u"cake": u"chocolate"}

# Display the dictionary.
print d

#or something fancier, like:
print u"{name} is from {city}, and likes {cake} cake.".format(**d)


# Delete the entry for "cake".
# Display the dictionary.

print u"with cake"
print d
#del d[u"cake"]
d.pop(u"cake")

print u"without cake"
print d

# Add an entry for "fruit" with "Mango" and display the dictionary.

d[u'fruit'] = u'Mango'

print d

# Display the dictionary keys.

print d.keys()

# Display the dictionary values.

print d.values()

# Display whether or not "cake" is a key in the dictionary (i.e. False) (now).

print u'cake' in d

# Display whether or not "Mango" is a value in the dictionary.

print u"Mango" in d.values()

# Using the dict constructor and zip, build a dictionary of numbers
# from zero to fifteen and the hexadecimal equivalent (string is fine).

nums = range(16)
hexes = []
for num in nums:
    hexes.append(hex(num))

hex_dict = dict(zip(nums, hexes))

print hex_dict

## fancy with a list comprehension:

nums = range(16)
hexes = [hex(i) for i in nums]
hex_dict = dict(zip(nums, hexes))
print hex_dict

## even fancier with a dict comprehension:
hex_dict = { i: hex(i) for i in range(16) }
print hex_dict


# Using the dictionary from item 1: Make a dictionary using the same keys
# but with the number of 'a's in each value.

a_dict = {}
for key, val in d.items():
    a_dict[key] = val.count(u'a')
print a_dict

# or the fancy dict comprehension method:

a_dict = { key:val.count(u't') for key,val in d.items()}

print a_dict

# replacing the values:

for key, val in d.items():
    d[key] = val.count(u'a')
print d

# Create sets s2, s3 and s4 that contain numbers from zero through twenty,
#   divisible 2, 3 and 4.
# Display the sets.

s2 = set()
s3 = set()
s4 = set()
for i in range(21):
    if not i%2:
        s2.add(i)
    if not i%3:
        s3.add(i)
    if not i%4:
        s4.add(i)

print s2
print s3
print s4

#or a bit trickier:
s2, s3, s4 = sets = (set(), set(), set())
for i, st in zip( (2,3,4), sets):
    for j in range(21):
        if not j%i:
            st.add(j)
print s2
print s3
print s4


# or the set comprehension way:
s2 = { i for i in range(21) if not i%2}
s3 = { i for i in range(21) if not i%3}
s4 = { i for i in range(21) if not i%4}

print s2
print s3
print s4

# combine those:
# or is that getting too carried away?
s2, s3, s4 = [ { i for i in range(21) if not i%j} for j in range(2,5) ]

print s2
print s3
print s4


# Display if s3 is a subset of s2 (False)

print s3.issubset(s2)

# and if s4 is a subset of s2 (True).

print s4.issubset(s2)

# Create a set with the letters in ‘Python’ and add ‘i’ to the set.

s = set(u'Python')
s.add('i')

print s

# maybe:
s = set(u'Python'.lower()) # that wasn't specified...
s.add('i')

# Create a frozenset with the letters in ‘marathon’

fs = frozenset(u'marathon')

# display the union and intersection of the two sets.

print u"union:", s.union(fs)
print u"intersection:", s.intersection(fs)

## not that order doesn't matter for these:

print u"union:", fs.union(s)
print u"intersection:", fs.intersection(s)




