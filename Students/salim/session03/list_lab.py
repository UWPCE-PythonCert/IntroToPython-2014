#!/usr/bin/env python

a_list = ['Apples', 'Pears', 'Oranges', 'Peaches']

print a_list


print 'Please provide another fruit:'
user_input = raw_input()

a_list.append(user_input)
print a_list

print 'Please provide a number:'
user_number = int(raw_input())
print 'This number is %d, which matches fruit %s.' % (user_number, a_list[user_number - 1])

a_list = ['Bananna'] + a_list
print a_list

a_list.insert(0, 'Avacado')
print a_list


p_list = []
for fruit in a_list:
    if fruit[0].lower() == 'p':
        p_list.append(fruit)

print p_list
