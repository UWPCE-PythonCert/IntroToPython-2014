#!/usr/bin/python

food_prefs = {"name": u"Chris",
              u"city": u"Seattle",
              u"cake": u"chocolate",
              u"fruit": u"mango",
              u"salad": u"greek",
              u"pasta": u"lasagna"}

#Print the dict by passing it to a string format method
print [i.upper() for i in food_prefs]

#Using a list comprehension, build a dictionary of numbers from zero to fifteen and the hexadecimal equivalent (string is fine).
print "This uses a list \n"
print [(i, hex(i)) for i in range(16)]

#Same thing but with dict. comp
print "This one uses a dict \n"
print [{i : hex(i)} for i in range(16)]

#copy list
food_prefs_count_a = food_prefs

#Number of A's in each value
food_prefs_count_a = [{i: i.count('a')} for i in food_prefs]

print food_prefs_count_a

#Create sets that contain numbers 0 - 20 divisible by 2,3,4
s2 = set([i for i in range(21) if i % 2 == 0])
print s2

s3 = set([i for i in range(21) if i % 3 == 0])
print s3

s4 = set([i for i in range(21) if i % 4 == 0])
print s4


sets = []

def set_divisibility_generator(number):

    [sets.append(i) for i in range(21) if i % number == 0]

    print sets

while True:
    
    x = int(raw_input('What numbers would you like 20 to be divided by? '))
    set_divisibility_generator(x)
