#!/usr/bin/env python

"""
Chris' solutions to the list lab

A couple take-home concepts:

If you need to delete stuff from the list when looping through it,
make a copy ([:]) first.

You almost never want to loop through a sequence by doing:

for i in range(len(seq)):
    ...
if you don't need the index, simply do:

for item in seq:
    ...
If you need both the item and the index, use enumerate():

for i, item in enumerate(seq):
    ...

If you need to loop through more than one list at once, use zip():

for item1, item2 in zip(list1, list2):
    ...

"""

# Task 1
fruits = ["Apples", "Pears", "Oranges", "Peaches"]

print(fruits)

new = input("type a fruit to add> ")

fruits.append(new)

print(fruits)

ind = int(input("give me an index> "))

print("you selected fruit number: %i, which is %s" % (ind, fruits[ind-1]))
print()
print("All the fruit:\n", fruits)
print()

fruits.insert(0, 'Kiwi')

print("Added a kiwi:\n", fruits)

print("All the P fruits")
for fruit in fruits:
    if fruit[0].lower() == 'p':
        print(fruit)
print()

# make a new list with duplicated entries - to test removal
d_fruits = fruits * 2

print("All the fruits are:", fruits)
ans = input("Which fruit would you like to delete? ")
while ans in d_fruits:
    d_fruits.remove(ans)

print("with fruit deleted:\n", d_fruits)

# another way to do that:
#     This one only requires looping through list once
d_fruits = []
for fruit in fruits * 2:
    if fruit != ans:
        d_fruits.append(fruit)

print("With fruit deleted another way:\n", d_fruits)
print()

# keep a copy around for next step
orig_fruits = fruits[:]

for fruit in fruits[:]:  # loop through a copy!
    ans = input("Do you like: %s? " % fruit)
    if ans[0].lower() == 'n':  # so they could answer y or Y or yes or Yes...
        while fruit in fruits:  # just in case there are duplicates
            fruits.remove(fruit)
    elif ans[0].lower() == 'y':
        pass
    else:
        print("please answer yes or no next time!")
        # Note: I could be smarter about re-asking here,
        #       but that's not the point of this excercise...

print("here they are with only the ones you like")
print(fruits)
print()

fruits = orig_fruits[:]  # makes a copy

# option 1: build up a copy one by one:
r_fruits = []
for fruit in fruits:
    r_fruits.append(fruit[::-1])

print("here they are reversed")
print(r_fruits)

# option 2: make a copy, then modify in place:
r_fruits = fruits[:]
for i, fruit in enumerate(r_fruits):
    r_fruits[i] = fruit[::-1]

print(r_fruits)
