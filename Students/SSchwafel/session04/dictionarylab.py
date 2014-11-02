#!/usr/bin/python
# -*- coding: utf-8 -*-
#Create a dictionary containing “name”, “city”, and “cake” for “Chris” from “Seattle” who likes “Chocolate”.
dictionary = {}

dictionary['name'] = 'Chris'
dictionary['city'] = 'Seattle'
dictionary['cake'] = 'chocolate'

#Display the dictionary.
print dictionary

#Delete the entry for “cake”.
del dictionary['cake']

#Display the dictionary.
print dictionary
#Add an entry for “fruit” with “Mango” and display the dictionary.

dictionary['fruit'] = 'mango'
print dictionary

#Display the dictionary keys.
print dictionary.keys()

#Display the dictionary values.
print dictionary.values()

#Display whether or not “cake” is a key in the dictionary (i.e. False).
print 'cake' in dictionary
#Display whether or not “Mango” is a value in the dictionary (i.e. True).
print 'mango' in dictionary
#Using the dict constructor and zip, build a dictionary of numbers from zero to fifteen and the hexadecimal equivalent (string is fine).
numbers = range(15)
#numbers = dict(numbers)
hexnumbers = []

for i in numbers:

    hexnumbers.append(hex(i))

zipped_dict = zip(numbers, hexnumbers)

print zipped_dict

#Using the dictionary from item 1: Make a dictionary using the same keys but with the number of ‘t’s in each value.
dictionary_values =  dictionary.values()
dictionary_values =  str(", ".join(dictionary_values))
dictionary_values =  dictionary_values.lower()

print "\nThere are %i %s's in this dictionary:\n" % (dictionary_values.count('t'),'t')

for i in dictionary:
    print dictionary[i]
    dictionary[i] = dictionary[i].count('t')

print dictionary.values()
#Create sets s2, s3 and s4 that contain numbers from zero through twenty, divisible 2, 3 and 4.

s2 = set(range(21))
s2_copy = s2.copy()

s3 = set(range(21))
s3_copy = s3.copy()

s4 = set(range(21))
s4_copy = s4.copy()

#Remove those in s2 not divisible by 2
for i in s2_copy:
    if i % 2 != 0 or i == 0:
        s2.remove(i)

#Remove those in s3 not divisible by 3
for i in s3_copy:
    if i % 3 != 0 or i == 0:
        s3.remove(i)


#Remove those in s4 not divisible by 4
for i in s4_copy:
    if i % 4 != 0 or i == 0:
        s4.remove(i)

#Display the sets.

print s2
print s3
print s4

#Display if s3 is a subset of s2 (False)
print s3.issubset(s2)

#and if s4 is a subset of s2 (True).
print s4.issubset(s2)


#Create a set with the letters in ‘Python’ and add ‘i’ to the set.
p = set('Python')
p.add('i')

print p

#Create a frozenset with the letters in ‘marathon’
m = frozenset('marathon')
print m
#display the union and intersection of the two sets.
print p.union(m)
print p.intersection(m)
