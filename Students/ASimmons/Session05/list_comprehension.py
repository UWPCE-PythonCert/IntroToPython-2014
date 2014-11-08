__author__ = 'asimmons'

feast = ['lambs', 'sloths', 'orangutans', 'breakfast cereals', 'fruit bats']
comprehension = [delicacy.capitalize() for delicacy in feast]

# >>> comprehension[0]
#'Lambs'
#>>> comprehension[2]
#'Orangutans'


feast2 = ['spam', 'sloths', 'orangutans', 'breakfast cereals', 'fruit bats']
comprehension2 = [delicacy for delicacy in feast if len(delicacy) > 6]

# >>> print comprehension2
# >>> ['orangutans', 'breakfast cereals', 'fruit bats']

#>>> len(feast2)
#5
#>>> len(comprehension2)
#3

list_of_tuples = [(1, 'lumberjack'), (2, 'inquisition'), (4, 'spam')]
comprehension3 = [ skit * number for number, skit in list_of_tuples ]

#>>> comprehension3[0]
#'lumberjack'
#>>> len(comprehension[2])
#10

list_of_eggs = ['poached egg', 'fried egg']
list_of_meats = ['lite spam', 'ham spam', 'fried spam']
comprehension4 = [ '{0} and {1}'.format(egg, meat) for egg in list_of_eggs for meat in list_of_meats]

#>>> len(comprehension4)
#6
#>>> comprehension4[0]
#'poached egg and lite spam'

comprehension5 = { x for x in 'aabbbcccc'}
#>>> set(['a', 'c', 'b'])

dict_of_weapons = {'first': 'fear', 'second': 'surprise', 'third':'ruthless efficiency', 'forth':'fanatical devotion', 'fifth': None}
dict_comprehension = \
{ k.upper(): weapon for k, weapon in dict_of_weapons.iteritems() if weapon}

#>>> 'first' in dict_comprehension
#False
#>>> 'FIRST' in dict_comprehension
#True

#>>> len(dict_of_weapons)
#5
#>>> len(dict_comprehension)
#4