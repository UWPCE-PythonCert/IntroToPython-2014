#!/usr/bin/env python


# print original list
a_list = ['Apples', 'Pears', 'Oranges', 'Peaches']
print a_list

# ask user to add a fruit
user_input = raw_input('Please provide another fruit: ')

# add the fruit to the list and print the new list
a_list.append(user_input)
print a_list

# ask user for a number and print the corresponding fruit
user_number = int(raw_input('Please provide a number: '))
print 'This number is %d, which matches fruit %s.' % (user_number, a_list[user_number - 1])

# add another fruit to the start of list using "+"
a_list = ['Bananna'] + a_list
print a_list

# add another fruit to the start of list using "insert"
a_list.insert(0, 'Avacado')
print a_list

# display all fruits that start with "P"
p_list = []
for fruit in a_list:
    if fruit[0].lower() == 'p':
        p_list.append(fruit)
print p_list

# remove last fruit from list
del a_list[-1]
print a_list

# ask user for fruit to delete, then delete
user_delete = raw_input('Type a Fruit to delete: ')
a_list.remove(user_delete)

# loop through and ask the user if they like each fruit
for fruit in a_list:
    user_delete = raw_input('Do you like %s? ' % fruit.lower())

    # correct the entry if it's not yes or no
    while not (user_delete.lower() == 'yes' or user_delete.lower() == 'no'):
        user_delete = raw_input('Please enter "Yes" or "No". Try again.')

    # delete the fruit from the list if answered "No"
    if user_delete.lower() == 'no':
        a_list.remove(fruit)

print a_list

# make a copy of the list
copy_list = a_list[:]

# reverse letters
for idx, fruit in enumerate(copy_list):
    copy_list[idx] = fruit[::-1]

# delete last item of original list
del a_list[-1]

# print both lists
print 'Original List: %s' % a_list
print 'Copy List: %s' % copy_list
