#!/usr/bin/env python2.7
fruits = ["Apples", "Pears", "Oranges", "Peaches"]

print "List of fruit: ", fruits

fruits.append(raw_input("Add another fruit: "))
print "Added your fruit to the list: ", fruits

fruit_num = int(raw_input("Give the number of your favorite fruit: "))

if(fruit_num <= 0 or fruit_num > len(fruits)):
    print "The fruit # you entered: ", fruit_num, "you entered is not in the list!"
else:
    print "Your favorite fruit is #:", fruit_num, ":", fruits[fruit_num - 1]

fruits = [raw_input("Add a fruit to the beginning of the list: ")] + fruits
print "Added your new fruit to the front of the list: ", fruits

fruits.insert(0, raw_input("Add another fruit to the beginning of the list in a different way: "))
print "Added your new fruit to the front of the list: ", fruits

print "All the fruits in the list that begin with 'P':"
aPfruit = False
for afruit in fruits:
    if ("P" in afruit):
        aPfruit = True
        print afruit
if (not aPfruit):
    print "None of the fruits start with 'P'"

print "Here is the current list of fruits:", fruits
print "Removing the last one from the list:", fruits.pop()
print fruits

fruits.remove(raw_input("What fruit would you like to delete from the list: "))
print fruits

# iterate over a copy, hence the "fruits[:]:"
fruits = ["Apples", "Pears", "Oranges", "Peaches"]
for fruit in fruits[:]:
    likefruit = ""
    afruit = fruit.lower()
    while (likefruit != "yes" and likefruit != "no"):
        likefruit = raw_input("Do you like " + afruit + "?: ")
        likefruit = likefruit.lower()
        if(likefruit != "yes" and likefruit != "no"):
            print "You entered: ", likefruit, "which is not valid"
            print "Please enter 'yes' or 'no'"
    if(likefruit == "no"):
        fruits.remove(fruit)
print fruits

# Make a shallow copy, and reverse the letters of each fruit in the copy
fruits = ["Apples", "Pears", "Oranges", "Peaches"]
fruits_copy = fruits[:]
for i, fruit in enumerate(fruits_copy):
    fruits_copy[i] = fruit[::-1]

# Delete the last item of the original list, and display the list and the copy
fruits.pop()
print fruits_copy, fruits