def listcomp():
	# output guesses are
	# in trailing comments

	# Exercise one
	feast = ['lambs', 'sloths', 'orangutans', 'breakfast cereals', 'fruit bats']
	comprehension = [delicacy.capitalize() for delicacy in feast]

	# Exercise one
	print comprehension[0] # 'Lambs'
	print comprehension[2] # 'Orangutans'
	print

	# Exercise two
	feast = ['spam', 'sloths', 'orangutans', 'breakfast cereals','fruit bats']
	comprehension = [delicacy for delicacy in feast if len(delicacy) > 6]

	# Exercise two
	print len(feast) # 5
	print len(comprehension) # 3
	print


	# Exercise three
	list_of_tuples = [(1, 'lumberjack'), (2, 'inquisition'), (4, 'spam')]
	comprehension = [ skit * number for number, skit in list_of_tuples ]

	# Exercise three
	print comprehension[0] # lumberjack
	print len(comprehension[2]) # 16
	print

	# Exercise four
	list_of_eggs = ['poached egg', 'fried egg']
	list_of_meats = ['lite spam', 'ham spam', 'fried spam']
	# generates all permutations of the combined list
	comprehension = [ '{0} and {1}'.format(egg, meat) for egg in list_of_eggs for meat in list_of_meats]

	# Exercise four
	print len(comprehension) # 2
	print comprehension[0] # 'poached egg and lite spam'
	print

	# Exercise five
	comprehension = { x for x in 'aabbbcccc'}

	print comprehension # {'a','a','b','b','b','c','c','c','c'} ?

	# Exercise SIX
	dict_of_weapons = {
		'first': 'fear',
		'second': 'surprise',
		'third':'ruthless efficiency',
		'forth':'fanatical devotion',
		'fifth': None
		}

	dict_comprehension = { k.upper(): weapon for k, weapon in dict_of_weapons.iteritems() if weapon}
		# {
			# 'FIRST': 'fear',
			# 'SECOND': 'surprise',
			# 'THIRD':'ruthless efficiency',
			# 'FORTH':'fanatical devotion',
		# }

	print 'first' in dict_comprehension # False
	print 'FIRST' in dict_comprehension # True
	print len(dict_of_weapons) # 5
	print len(dict_comprehension) # 4
	print

	return True


if __name__ == '__main__':
	assert listcomp() # throws error unless return truthy










