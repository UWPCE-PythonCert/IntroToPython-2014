#!/usr/bin/python

dictionary = {}

dictionary['name'] = 'Chris'
dictionary['city'] = 'Seattle'
dictionary['cake'] = 'chocolate'

print dictionary

del dictionary['cake']

print dictionary

dictionary['fruit'] = 'mango'
dictionary['fruit'] = 'ttttt'

print dictionary.keys()
print dictionary.values()

print 'cake' in dictionary
print 'mango' in dictionary

numbers = range(15)
#numbers = dict(numbers)
hexnumbers = []

for i in numbers:

    hexnumbers.append(hex(i))

print numbers
print hexnumbers

zipped_dict = zip(numbers, hexnumbers)

print zipped_dict

dictionary_values =  dictionary.values()
dictionary_values =  str(", ".join(dictionary_values))
dictionary_values =  dictionary_values.lower()

print "\nThere are %i %s's in this dictionary:\n" % (dictionary_values.count('t'),'t')

dictionary_keys =  dictionary.keys()
print dictionary_keys
