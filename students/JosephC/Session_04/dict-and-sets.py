#Dictionaries and sets lab

"""
Playing with dictionaries and sets

"""

#   Create a dictionary containing “name”, “city”, and “cake” for “Chris” from “Seattle” who likes “Chocolate”.

foo = {'name':'Chris', 'city': 'Seattle', 'cake': 'Chocolate'}

#   Display the dictionary

print(foo)

#   Delete the entry for “cake”.

foo.pop('cake')

#   Display the dictionary.

print(foo)

#   Add an entry for “fruit” with “Mango” and display the dictionary.
foo['fruit'] = 'mango'
#   Display the dictionary keys
print("Dictionary keys: " , foo.keys())
#   Display the dictionary values.
print("Dictionary values: ", foo.values())
#  Display whether or not “cake” is a key in the dictionary (i.e. False) (now).
'cake' in foo
#   Display whether or not “Mango” is a value in the dictionary (i.e. True).
foo.values == 'mango'
print(foo)
#   Using the dict constructor and zip, build a dictionary of numbers from zero to fifteen and the hexadecimal equivalent (string is fine).

binary = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
hex = [1,2,3,4,5,6,7,8,9, 'A', 'B', 'C', 'D', 'E', 'F']
for x, y in zip(binary, hex):  print("binary: {} = hexadecimcal: {}".format(x,y)) 

#    Using the dictionary from item 1: Make a dictionary using the same keys but with the sum of ‘t’s in each value.
#   
newFoo = {}
for key, value in foo.items():
    newFoo[key] = value.count('t')    

#   Create sets s2, s3 and s4 that contain numbers from zero through twenty, divisible 2, 3 and 4.
s2 = set([2,4,6,8,10,12,14,16,18, 20])
s3 = set([3,6,9,12,15,18])
s4 = set([4,8,12,16,20])
#   Display the sets.
print(s2, s3,s4)
    #Display if s3 is a subset of s2 (False)
s3.issubset(s2)
    #and if s4 is a subset of s2 (True).
s4.issubset(s2)

#   Create a set with the letters in ‘Python’ and add ‘i’ to the set.
p = set('Python')
p.update('i')
print(p)
#   Create a frozenset with the letters in ‘marathon’
fs = frozenset('marathon')
print(fs)
#   display the union and intersection of the two sets
print(p.union(fs))
print(p.intersection(fs))





