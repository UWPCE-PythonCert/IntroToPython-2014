1. Creating lists with list comprehensions
==========================================
	>>> feast = ['lambs', 'sloths', 'orangutans', 'breakfast cereals', 
				'fruit bats']

	>>> comprehension = [delicacy.capitalize() for delicacy in feast]

What is the output of:
----------------------
	>>> comprehension[0]
	???

	>>> comprehension[2]
	???

2. Filtering lists with list comprehensions
===========================================
	>>> feast = ['spam', 'sloths', 'orangutans', 'breakfast cereals',
	            'fruit bats']

	>>> comprehension = [delicacy for delicacy in feast if len(delicacy) > 6]

What is the output of:
----------------------
	>>> len(feast)
	???

	>>> len(comprehension)
	???


3. Unpacking tuples in list comprehensions
==========================================
	>>> list_of_tuples = [(1, 'lumberjack'), (2, 'inquisition'), (4, 'spam')]

	>>> comprehension = [ skit * number for number, skit in list_of_tuples ]

What is the output of:
----------------------
	>>> comprehension[0]
	???

	>>> len(comprehension[2])
	???

4. Double list comprehension
============================
	>>> list_of_eggs = ['poached egg', 'fried egg']

	>>> list_of_meats = ['lite spam', 'ham spam', 'fried spam']

	>>> comprehension = [ '{0} and {1}'.format(egg, meat) for egg in list_of_eggs for meat in list_of_meats]

What is the output of:
----------------------
	>>> len(comprehension)
	???

	>>> comprehension[0]

5. Creating a set with set comprehension
========================================
	>>> comprehension = { x for x in 'aabbbcccc'}

What is the output of:
----------------------

	>>> comprehension
	???

6. Creating a dictionary with dictionary comprehension
======================================================
	>>> dict_of_weapons = {'first': 'fear', 'second': 'surprise',
	            'third':'ruthless efficiency', 'forth':'fanatical devotion',
	            'fifth': None}

	>>> dict_comprehension = { k.upper(): weapon for k, weapon in dict_of_weapons.iteritems() if weapon}

What is the output of:
----------------------
>>> 'first' in dict_comprehension
	???

	>>> 'FIRST' in dict_comprehension
	???

	>>> len(dict_of_weapons)
	???

	>>> len(dict_comprehension)
	???


See also:  https://github.com/gregmalcolm/python_koans
https://github.com/gregmalcolm/python_koans/blob/master/python2/koans/about_comprehension.py


7. Count even numbers
=====================
This is from CodingBat "count_evens" (http://codingbat.com/prob/p189616)

*Using list comprehension*, return the number of even ints in the given array. Note: the % "mod" operator computes the remainder, e.g. 5 % 2 is 1. 

    count_evens([2, 1, 2, 3, 4]) → 3
    
    count_evens([2, 2, 0]) → 3
    
    count_evens([1, 3, 5]) → 0
    

    def count_evens(nums):

