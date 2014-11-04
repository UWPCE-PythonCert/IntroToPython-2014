#!/usr/bin/env python2.7

newlist = [ x+y for x in range(3) for y in range(5, 7) ]
print newlist

feast = ['lambs', 'sloths', 'orangutans', 'breakfast cereals', 'fruit bats']
comprehension = [delicacy.capitalize() for delicacy in feast]
print comprehension

print comprehension[0]
print comprehension[2]

comprehension = [ delicacy for delicacy in feast if len(delicacy) > 6 ]
print comprehension

print len(feast)
print len(comprehension)

list_of_tuples = [ (1, 'lumberjack'), (2, 'inquisition'), (4, 'spam') ]
comprehension = [ skit * number for number, skit in list_of_tuples ]
print comprehension
print comprehension[0]
print len(comprehension[2])

list_of_eggs = ['poached egg', 'fried egg']
list_of_meats = ['lite spam', 'ham spam', 'fried spam']
comprehension = [ '{0} and {1}'.format(egg, meat) for egg in list_of_eggs for meat in list_of_meats ]
print comprehension
print len(comprehension)
print comprehension[0]

comprehension = { x for x in 'aabbbcccc' }
print comprehension

dict_of_weapons = { 'first'  : 'fear',
                    'second' : 'surprise',
                    'third'  : 'ruthless efficiency',
                    'forth'  : 'fanatical devotion',
                    'fifth'  : None }
dict_comprehension = \
{ k.upper(): weapon for k, weapon in dict_of_weapons.iteritems() if weapon }
print dict_comprehension
print 'first' in dict_comprehension
print 'FIRST' in dict_comprehension
print len(dict_of_weapons)
print len(dict_comprehension)

def count_evens(nums):
    print len([evens for evens in nums if evens%2==0])

numberlist = [2, 1, 2, 3, 4, 6, 8, 11, 13]
numberlist2 = [2, 2, 0]
numberlist3 = [1, 3, 5]
count_evens(numberlist)
count_evens(numberlist2)
count_evens(numberlist3)

food_prefs = { "name"  : "Chris",
               "city"  : "Seattle",
               "cake"  : "chocolate",
               "fruit" : "mango",
               "salad" : "greek",
               "pasta" : "lasagna" }
print "{name} is from {city} and likes {cake} cake, {fruit} fruit, {salad} salad, and {pasta} pasta.".format(**food_prefs)

hexequiv = [ hex(i) for i in range(16) ]
hexdict = dict( zip(range(16), hexequiv) )
print hexdict

hexdict = dict( zip(range(16), [hex(i) for i in range(16)]) )
print hexdict

food_prefs_a = {  k : weapon.count("a") for k, weapon in dict_of_weapons.iteritems() if weapon }
print food_prefs_a

s2 = { i for i in range(21) if i%2==0 }
s3 = { i for i in range(21) if i%3==0 }
s4 = { i for i in range(21) if i%4==0 }

print "s2 = ", s2
print "s3 = ", s3
print "s4 = ", s4

dividers = (2, 3, 4)
dict_of_dividers = {}
for d in dividers:
    dict_of_dividers.update({ d: {i for i in range(21) if i%d == 0} })

print "s2 = ", dict_of_dividers[2]
print "s3 = ", dict_of_dividers[3]
print "s4 = ", dict_of_dividers[4]
