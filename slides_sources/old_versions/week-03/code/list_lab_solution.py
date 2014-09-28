#!/usr/bin/env python

"""
list lab solution
"""

# Create a list that contains "Apples", "Pears", "Oranges" and "Peaches".
fruit = ["Apples", "Pears", "Oranges" and "Peaches"]

# Display the list.
print fruit

# Ask the user for another fruit and add it to the end of the list.
new_fruit = raw_input("type in a fruit name > ")

fruit.append(new_fruit)

# Display the list.
print fruit

# Ask the user for a number and display the number back to the user
# and the fruit corresponding to that number (on a 1-is-first basis).
number = input("give me a number between 1 and "+`len(fruit)`+" > ")

print "you picked:", number, "--", fruit[number-1]

# Add another fruit to the beginning of the list using "+".
fruit = ['Mangoes'] + fruit
print fruit

# Add another fruit to the beginning of the list using insert().
fruit.insert(0, 'Apricots')
print fruit





