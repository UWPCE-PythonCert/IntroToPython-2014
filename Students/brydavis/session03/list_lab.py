#!/usr/bin/env python

# Create a list that contains fruit
fruit = ['Apples', 'Pears', 'Oranges', 'Peaches']

def series_one(fruit=fruit):

	print '\nFruit: Series One'
	print '================='

	# Display the list
	print '\nCurrent list: ', fruit

	# Ask the user for another fruit and add it to the end of the list
	fruit.append(raw_input('What\'s another fruit you like? '))

	# Display the list again
	print fruit

	# Ask the user for a number and display the number back to the user and the fruit corresponding to that number (on a 1-is-first basis)
	num_select = raw_input('\nType a number between 1 and 5: ')
	print 'You selected: ', fruit[int(num_select) - 1]

	# Add another fruit to the beginning of the list using '+' and display the list.
	fruit = [raw_input('\nHow about another fruit you like? ')] + fruit
	print 'Updated list: ', fruit
	
	# Add another fruit to the beginning of the list using insert() and display the list.
	fruit.insert(0, raw_input('\nAnd another fruit? '))
	print 'Updated list: ', fruit
	
	# Display all the fruits that begin with 'P', using a for loop.
	print '\nFruit starting with the letter\'P\':'
	for f in fruit:
		if f[0].lower() == 'p':
			print '\t', f

	return series_two(fruit)



def series_two(fruit=fruit):

	print '\nFruit: Series Two'
	print '================='

	# Display the list.
	print '\nCurrent list: ', fruit

	# Remove the last fruit from the list.
	print 'Removing the last fruit from the list.'
	gone = fruit.pop()

	# Display the list.
	print '\nNew list without %s: ' % gone, fruit
	
	# Ask the user for a fruit to delete and find it and delete it.
	bad_fruit = raw_input('What fruit would you remove from the list? ') 
	
	try:
		gone = fruit.remove(bad_fruit[0].upper() + bad_fruit[1:].lower())
		print '\nNew list without %s: ' % bad_fruit, fruit
	except:
		print '%s not found. No updates to list.' % bad_fruit

	# (Bonus: Multiply the list times two. Keep asking until a match is found. Once found, delete all occurrences.)
	# {{{{{{{{{{{{{{{{{{{{{{{here you are}}}}}}}}}}}}}}}}}}}}}}}

	return series_three(fruit)



def series_three(fruit=fruit):

	print '\nFruit: Series Three'
	print '==================='
	
	# Display the list.
	print '\nCurrent list: ', fruit

	fruit_copy = fruit[:]

	# Ask the user for input displaying a line like 'Do you like apples?'
	# for each fruit in the list (making the fruit all lowercase).
	for f in fruit_copy:
		def get_likes():
			return raw_input('Do you like %s? ' % f.lower())
		
		response = get_likes().lower()

		while response != 'no' and response != 'yes':
			print 'Please respond either\'yes\' or \'no\'.'
			response = get_likes().lower()

		if response == 'no':
			fruit.remove(f)
		else:
			pass
		
	# Display the list.
	print '\nRemaining list: ', fruit

	return series_four(fruit)



def series_four(fruit=fruit):

	print '\nFruit: Series Four'
	print '=================='


	# Make a copy of the list and reverse the letters in each fruit in the copy
	scrambled_fruit = fruit[:]

	# Display the original list sans the last element.
	print '\nCurrent list (sans the last value): ', fruit
	fruit.pop()
	print '\nCurrent list (sans the last value): ', fruit


	for i, f in enumerate(scrambled_fruit):
		scrambled_fruit[i] = f[::-1]
	
	# Delete the last item of the original list. Display the original list and the copy
	print 'A scrambled copy: ', scrambled_fruit

	return




if __name__ == '__main__':
	# When the script is run, it should run four series of actions:
	series_one()


# Q: use original 'fruit' list for each new series?
# Q: skipping entries in list?







