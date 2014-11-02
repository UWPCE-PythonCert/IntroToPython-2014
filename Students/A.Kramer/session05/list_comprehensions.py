'''
Created on Oct 30, 2014

@author: db345c
'''

# 1.
feast = ['lambs', 'sloths', 'orangutans', 'breakfast cereals', 'fruit bats']
comprehension = [delicacy.capitalize() for delicacy in feast]
# Guessed: Lambs and Oranges
print comprehension[0]
print comprehension[2]

# 2.
feast = ['spam', 'sloths', 'orangutans', 'breakfast cereals', 'fruit bats']
comprehension = [delicacy for delicacy in feast if len(delicacy) > 6]
# Guessed: 5 and 3
print len(feast)
print len(comprehension)

# 3.
list_of_tuples = [(1, 'lumberjack'), (2, 'inquisition'), (4, 'spam')]
comprehension = [ skit * number for number, skit in list_of_tuples ]
# Guessed: lumberjeck and spamspamspamspam -> 16
print comprehension[0]
print comprehension[2]
print len(comprehension[2])

# 4.
list_of_eggs = ['poached egg', 'fried egg']
list_of_meats = ['lite spam', 'ham spam', 'fried spam']
# Guessed: 6, poached eggs and little spam
comprehension = [ '{0} and {1}'.format(egg, meat) for egg in list_of_eggs for meat in list_of_meats]
print len(comprehension)
print comprehension[0]

#5.
comprehension = { x for x in 'aabbbcccc'}
# Guessed: wrong!!!
print comprehension

# 6.
dict_of_weapons = {'first': 'fear', 'second': 'surprise', 'third':'ruthless efficiency',
                       'forth':'fanatical devotion', 'fifth': None}
dict_comprehension = { k.upper(): weapon for k, weapon in dict_of_weapons.iteritems() if weapon}
# Guessed: FIRST, 5 and 4
print 'first' in dict_comprehension
print 'FIRST' in dict_comprehension
print len(dict_of_weapons)
print len(dict_comprehension)

# 7.
# Returning the number of even ints
arr = [2, 1, 2, 3, 4]
arr = (x for x in arr if x % 2 == 0)
print "The number of even ints in the [2, 1, 2, 3, 4] list is:", len(list(arr))

arr = [2, 2, 0]
arr = (x for x in arr if x % 2 == 0)
print "The number of even ints in the [2, 2, 0] list is:", len(list(arr))

arr = [1, 3, 5]
arr = (x for x in arr if x % 2 == 0)
print "The number of even ints in the [1, 3, 5] list is:", len(list(arr))

# The same as above but with function
def count_events(nums):
    print "The number of even ints in the", nums, "is:",
    arr = (x for x in nums if x % 2 == 0)
    print len(list(arr))
              
if __name__ == "__main__":
    count_events([2, 1, 2, 3, 4])

