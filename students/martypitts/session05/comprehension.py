feast = ['lambs', 'sloths', 'orangutans','breakfast cereals', 'fruit bats']
comprehension = [delicacy.capitalize() for delicacy in feast]

print ("comprehension[0]", comprehension[0])
print ("comprehension[1]", comprehension[1])

feast = ['spam', 'sloths', 'orangutans', 'breakfast cereals','fruit bats']
comp = [delicacy for delicacy in feast if len(delicacy) > 6]
print ("comp =", comp)
print ("feast =", len(feast))
print ("comp =", len(comp))

list_of_tuples = [(1, 'lumberjack'), (2, 'inquisition'), (4, 'spam')]
comprehension = [ skit * number for number, skit in list_of_tuples ]

print("comprehension =", comprehension)
print("comprehension length =", len(comprehension[2]))

eggs = ['poached egg', 'fried egg']
meats = ['lite spam', 'ham spam', 'fried spam']
comprehension = \
[ '{0} and {1}'.format(egg, meat) for egg in eggs for meat in meats]

print("comprehension length", len(comprehension))
print("comprehension ", (comprehension))
print ("comprehension[0]", comprehension[0])

comprehension = { x for x in 'aabbbcccc'}
print("comprehension ", (comprehension))

dict_of_weapons = {'first':'fear',
                   'second':'surprise',
		   'third':'ruthless efficiency',
		   'forth':'fanatical devotion',
		   'fifth': None}

dict_comprehension = { k.upper(): weapon for k, weapon in dict_of_weapons.iteritems() if weapon}

print("first", 'first' in dict_comprehension)
print("FIRST", 'FIRST' in dict_comprehension)
print("Dict Weapons", len(dict_of_weapons))

