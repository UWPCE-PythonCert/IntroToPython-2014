#!/usr/bin/env python


# #############################Lesson 1##############################

# create dict
d1 = {'name': 'Chris', 'city': 'Seattle', 'cake': 'Chocolate'}
print d1

# delete entry for cake
del d1['cake']
print d1

# add an entry to the dict
d1['fruit'] = 'Mango'
print d1

# display the values
d1.values()

# display the keys
d1.keys()

# is 'cake' a key in the dict?
'cake' in d1

# is 'Mango' a value in the dict?
'Mango' in d1.values()


# #############################Lesson 2##############################

# create list from 0 to 15
l2 = range(16)

# create list with hex representation
s2 = []
for item in l2:
    s2.append(hex(item))

# zip lists into dict
d2 = dict(zip(l2, s2))


# #############################Lesson 3##############################

# use d1 to create a new dict with same keys but number of 't's in values
d3 = {}
for key, value in d1.iteritems():
    d3[key] = value.count('t')


# #############################Lesson 4##############################

# make three sets
s2 = set(range(0, 20, 2))
s3 = set(range(0, 20, 3))
s4 = set(range(0, 20, 4))

# print the sets
print s2
print s3
print s4

# check sets
s3.issubset(s2)
s4.issubset(s2)


# #############################Lesson 4##############################

a_set = set('Python')
a_set.add('i')

b_set = frozenset('marathon')

u_set = a_set.union(b_set)
i_set = a_set.intersection(b_set)

print u_set
print i_set
