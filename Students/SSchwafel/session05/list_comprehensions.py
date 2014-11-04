#!/usr/bin/python

feast = ['lambs', 'sloths', 'orangutans', 'breakfast cereals', 'fruit bats']
comprehension = [delicacy.capitalize() for delicacy in feast]

feast = ['spam', 'sloths', 'orangutans', 'breakfast cereals', 'fruit bats']

comprehension = [delicacy for delicacy in feast if len(delicacy) > 6]

len(feast)

len(comprehension)

list_of_tuples = [(1, 'lumberjack'), (2, 'inquisition'), (4, 'spam')]

comprehension = [ skit * number for number, skit in list_of_tuples ]

comprehension[0]

len(comprehension[2])

list_of_eggs = ['poached egg', 'fried egg']

list_of_meats = ['lite spam', 'ham spam', 'fried spam']

comprehension = [ '{0} and {1}'.format(egg, meat) for egg in list_of_eggs for meat in list_of_meats]

len(comprehension)

comprehension[0]

comprehension = { x for x in 'aabbbcccc'}

comprehension

dict_of_weapons = {'first': 'fear',
                       'second': 'surprise',
                       'third':'ruthless efficiency',
                       'forth':'fanatical devotion',
                       'fifth': None}

'first' in dict_comprehension

'FIRST' in dict_comprehension

len(dict_of_weapons)

len(dict_comprehension)

