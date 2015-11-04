#Create a dictionary containing “name”, “city”, and “cake” 
#for “Chris” from “Seattle” who likes “Chocolate”.
cake_dict = {'name': 'Chris', 'city': 'Seattle', 'cake': 'Chocolate'}
print (cake_dict)
#Delete the entry for “cake”
cake_dict.pop('cake')
#Add an entry for “fruit” with “Mango” and display the dictionary
cake_dict['fruit'] = 'mango'
#Display whether or not “cake” is a key in the dictionary
'cake' in cake_dict
#Display whether or not “Mango” is a value in the dictionary
'mango' in cake_dict.values()

#Using the dictionary from item 1: 
#Make a dictionary using the same keys but with the number of ‘t’s 
#in each value.
new_dict = cake_dict.copy()
for key, item in new_dict.items():
    #if item.contains('t'):
    new_dict[key] = (item.count('t'))
    #print (key, item.count('t'))

#sets1
"""
    Create sets s2, s3 and s4 that contain numbers from zero through twenty
    divisible 2, 3 and 4.
    Display the sets.
    Display if s3 is a subset of s2 (False)
    and if s4 is a subset of s2 (True).
"""
set2 = set([])
for n in range (0 ,20):
    if n % 2 == 0:
        #print (n)
        set2.add(n)
print (set2)

set3 = set([])
for n in range (0 ,20):
    if n % 3 == 0:
        #print (n)
        set3.add(n)
print (set3)

set4 = set([])
for n in range (0 ,20):
    if n % 4 == 0:
        #print (n)
        set4.add(n)
print (set4)

#Display if s3 is a subset of s2 (False)
set3.issubset(set2)
#and if s4 is a subset of s2 (True).
set4.issubset(set2)
#sets 2
#Create a set with the letters in ‘Python’ and add ‘i’ to the set.
myset = set(['p','y','t','h','o','n'])
myset.add('i')
#Create a frozenset with the letters in ‘marathon’
fs = frozenset(['m','a','r','a','t','h','o','n'])
#display the union and intersection of the two sets.
unionset = myset.union(fs)
unionset
interset = myset.intersection(fs)

#File Reading and Writing Lab
"""
you will find the list I generated of all the students in the class, 
and what programming languages they have used in the past.
Write a little script that reads that file, 
and generates a list of all the languages that have been used.
"""
f = open('students.txt')
student_data = f.read()
list = student_data.split('\n')
#print (list)

for i in list:
    print (i.rpartition(':')[-1])
f.close()



