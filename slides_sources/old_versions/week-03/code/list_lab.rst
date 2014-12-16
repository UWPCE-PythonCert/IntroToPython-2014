
List Lab
#############

Modeled after <http://www.upriss.org.uk/python/session5.html>


Examples
===================

    zoo = ["giraffe", "crow"]               # define a list

    zoo[0]                                  # a single element

    zoo[0] = "zebra"                        # change an element

    zoo.append("marmot")                    # add element at end of list

    zoo = ["cat"] + zoo                     # add element at beginning

    type(raw_input("Type a string: "))      # returns str

    type(    input("Type a number: "))      # returns int or float

    [x for x in zoo if len(x) > 4]          # list comprehension

    zoo2 = zoo[:]                           # create a list copy

    zoo.pop()                               # delete last element

    del zoo[0]                              # delete element by index

    zoo.remove('crow')                      # delete element by value

    "abc"[::-1]                             # reverse a string: "cba"
                                            # Unspecified range takes all; step value of -1 reverses.

Exercises
===============

1.
----
 - Create a list that contains "Apples", "Pears", "Oranges" and "Peaches".
 - Display the list.
 - Ask the user for another fruit and add it to the end of the list.
 - Display the list.
 - Ask the user for a number and display the number back to the user and the fruit corresponding to that number (on a 1-is-first basis).
 - Add another fruit to the beginning of the list using "+" and display the list.
 - Add another fruit to the beginning of the list using insert() and display the list.

 - Display all the fruits that begin with "P", using a for loop.


2. Using the list above:
-------------------------
 - Display the list.
 - Remove the last fruit from the list.
 - Display the list.
 - Ask the user for a fruit to delete and find it and delete it.
 - (Bonus: Multiply the list times two. Keep asking until a match is found. Once found, delete all occurrences.)


3. Using the list in item 1:
 - Ask the user for input displaying a line like "Do you like apples?"
 - for each fruit in the list (making the fruit all lowercase).
 - For each "no", delete that fruit from the list.
 - Display the list.


4. Using the list in item 1:
 - Make a copy of the list and reverse the letters in each fruit in the copy.
 - Delete the last item of the original list. Display the original list and the copy.
