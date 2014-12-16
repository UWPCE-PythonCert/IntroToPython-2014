#!/usr/bin/python

fruit_list = ['apples','pears','oranges','peaches']

print fruit_list

add_fruit = str(raw_input("Give me another fruit to add! "))

fruit_list.append(add_fruit)

print fruit_list

user_index = int(raw_input("Give me an int and I'll give you the corresponding fruit! "))

print "You entered: " + str(user_index)

user_index = user_index-1

print fruit_list[user_index]

another_fruit = [raw_input("Gimme another fruit! ")]

fruit_list =  another_fruit + fruit_list

print 'OK, I added it\n'

yet_another_fruit = raw_input('Give me one last fruit! ')

fruit_list.insert(0,yet_another_fruit)

###FINISH THIS LAST THING
print fruit_list.sort(P)


