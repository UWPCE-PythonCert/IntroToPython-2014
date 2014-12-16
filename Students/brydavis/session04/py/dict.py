#!/usr/bin/env python
# Dictionaries and Sets lab

def Person(name='Chris',city='Seattle',cake='Chocolate'):
	# Create a dictionary containing "name", "city", and "cake" for "Chris" from "Seattle" who likes "Chocolate".
	Chris = {
		'name': name,
		'city': city,
		'cake': cake
	}

	# Display the dictionary.
	print 'create new person: ', Chris

	# Delete the entry for "cake".
	Chris.pop('cake')

	# Display the dictionary.
	print 'delete \'cake\' entry: ', Chris

	# Add an entry for "fruit" with "Mango" and display the dictionary.
	Chris['fruit'] = 'Mango'
	print 'add "Mango" as "fruit": ', Chris

	# Display the dictionary keys.
	print 'display keys: ', Chris.keys()

	# Display the dictionary values.
	print 'display values: ', Chris.values()

	# Display whether or not "cake" is a key in the dictionary (i.e. False) (now).
	print 'does "cake" key exist: ', 'cake' in Chris

	# Display whether or not "Mango" is a value in the dictionary (i.e. True).
	print 'does "Mango" value exist: ', 'Mango' in Chris.values()

	# Using the dict constructor and zip, build a dictionary of numbers from zero to fifteen and the hexadecimal equivalent (string is fine).
	numex = dict()
	for x in range(0,160):
		numex[x] = hex(x)[2:]

	return


def count_t(name='Chris',city='Seattle',cake='Chocolate'):
	# Using the dictionary from item 1: Make a dictionary using the same keys but with the number of 't's in each value.
	Chris = {
		'name': name,
		'city': city,
		'cake': cake
	}

	print 'Original: ', Chris
	for i in Chris:
		Chris[i] = Chris[i].count('t')
	print 'Number of \'t\'s in each value: ', Chris
	return


def number_sets(cb=None):
	# Create sets s2, s3 and s4 that contain numbers from zero through twenty, divisible 2, 3 and 4.
	s2, s3, s4 = set(), set(), set()

	for i in range(21):
		if i%2 == 0: s2.add(i)
		if i%3 == 0: s3.add(i)
		if i%4 == 0: s4.add(i)

	# Display the sets.
	print 's2: ', s2
	print 's3: ', s3
	print 's4: ', s4

	# Display if s3 is a subset of s2 (False)
	print 's3 a subset of s2: ', s3.issubset(s2)

	# and if s4 is a subset of s2 (True).
	print 's4 a subset of s2: ', s4.issubset(s2)

	if cb: return cb()


def py_set(cb=None):

	# Create a set with the letters in 'Python' and add 'i' to the set.
	p = set('python')
	p.add('i')
	print 'set one: %s' % p

	# Create a frozenset with the letters in 'marathon'
	m = frozenset('marathon')
	print 'set two: %s' % m

	# display the union and intersection of the two sets.
	union = m.union(p)
	print 'union: %s' % union

	intersect = m.intersection(p)
	print 'interset: %s' % intersect 
	
	if cb: return cb()
