

"""
    Part #1
    Create a dictionary containing “name”, “city”, and “cake” for “Chris” from “Seattle” who likes “Chocolate”.
    Display the dictionary.
    Delete the entry for “cake”.
    Display the dictionary.
    Add an entry for “fruit” with “Mango” and display the dictionary.
        Display the dictionary keys.
        Display the dictionary values.
        Display whether or not “cake” is a key in the dictionary (i.e. False) (now).
        Display whether or not “Mango” is a value in the dictionary (i.e. True).
"""

dict1 = {'name': 'Chris', 'city': 'Seatle', 'cake': 'Chocolate'}
print dict1
dict1.pop('cake')
print dict1
dict1['fruit'] = 'Mango'
print dict1.keys()
print dict1.values()
'cake' in dict1
'Mango' in dict1.values()




"""
   Part #2
   Using the dict constructor and zip, build a dictionary of numbers from zero to fifteen and the hexadecimal
   equivalent (string is fine).
"""

list1 = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15']
list2 = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
dict12 =  dict(zip(list1, list2))
print dict12




"""
   Part #3
   Using the dictionary from item 1: Make a dictionary using the same keys but with the number of ‘t’s in each
   value.
"""
dict1 = {'name': 'Chris', 'city': 'Seatle', 'cake': 'Chocolate'}
print dict1
dict1['name'] = 'ttt'
dict1['city'] = 'tttt'
dict1['cake'] = 'tt'
print dict1




"""
    Part #4
    Create sets s2, s3 and s4 that contain numbers from zero through twenty, divisible 2, 3 and 4.
    Display the sets.
    Display if s3 is a subset of s2 (False)
    and if s4 is a subset of s2 (True).
"""
 s2 = set([2, 3, 4, 8, 9, 12, 15, 18])
 s3 = set([3, 6, 10])
 s4 = set([2, 4, 8])
 s3.issubset(s2)
 s4.issubset(s2)



"""
    Part #5
    Create a set with the letters in ‘Python’ and add ‘i’ to the set.
    Create a frozenset with the letters in ‘marathon’
    display the union and intersection of the two sets.
"""








