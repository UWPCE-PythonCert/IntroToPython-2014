>>> feast = ['lambs', 'sloths', 'orangutans', 'breakfast cereals', 'fruit bats']

>>> comprehension = [delicacy.capitalize() for delicacy in feast]

# What is the output of:

>>> comprehension[0]
'Lambs'

>>> comprehension[2]
'Orangutans'


# On to next set

>>> feast = ['spam', 'sloths', 'orangutans', 'breakfast cereals', 'fruit bats']

>>> comprehension = [delicacy for delicacy in feast if len(delicacy) > 6]

# What is the output of:

>>> len(feast)
5

>>> len(comprehension)
3 # Only orangutans, breakfast cereals, and fruit bats


# On to the next one

>>> list_of_tuples = [(1, 'lumberjack'), (2, 'inquisition'), (4, 'spam')]

>>> comprehension = [ skit * number for number, skit in list_of_tuples ]

# What is the output of:

>>> comprehension[0]
'lumberjack'

>>> len(comprehension[2])
11 # I'm not sure about this one, length of 'inquisition'?


# Onward we go

>>> list_of_eggs = ['poached egg', 'fried egg']

>>> list_of_meats = ['lite spam', 'ham spam', 'fried spam']

>>> comprehension = [ '{0} and {1}'.format(egg, meat) for egg in list_of_eggs for meat in list_of_meats]

# What is the output of:

>>> len(comprehension)
6 # Because there are 6 different permutations for this set

>>> comprehension[0]
'poached egg and lite spam' # 0th item in each list


# Moving along

>>> comprehension = { x for x in 'aabbbcccc'}

# What is the output of:

>>> comprehension
'a', 'b', 'c' # I think...


# Now for the final one

>>> dict_of_weapons = {'first': 'fear',
                       'second': 'surprise',
                       'third': 'ruthless efficiency',
                       'fourth': 'fanatical devotion',
                       'fifth': None}
>>> dict_comprehension = \
{ k.upper(): weapon for k, weapon in dict_of_weapons.iteritems() if weapon}

# What is the output of:

>>> 'first' in dict_comprehension
False # because 'first' should be capitalized due to the iteration
>>> 'FIRST' in dict_comprehension
True
>>> len(dict_of_weapons)
5 # got to include None in there
>>> len(dict_comprehension)
4 # doesn't iterate through None so no fifth weapon