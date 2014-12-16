


Dictionaries and Sets Lab
###############################

Examples
============== 

::

    d = {}                                  # define a dictionary
    d = {"item": "tea", "country": "China"} # define a dictionary
    d["price"] = 1                          # add an item
    del d["price"]                          # delete an item
    d.keys()                                # list of dictionary keys
    d.values()                              # list of dictionary values
    "tea" in ["tea", "China"]               # membership...
    "coffee" in ["tea", "China"]            # or lack thereof
    hex(x)                                  # hexadecimal string for x
    [(x, x + 1) for x in range(7)]          # list comprehension of two-item tuples
    dict([(x, x + 1) for x in range(7)])    # dictionary of the previous item
    "abc".count("a")                        # count the number of occurrences of a substring
    [x for x in range(51) if x % 5 == 0]    # list comprehension for multiples of 5 under 51
    set([1,2])                              # set of items in a list
    set("Hi!")                              # set of characters in a string
    frozenset("Hi!")                        # frozen set of characters in a string
    set("Hi!").issubset(set("Hi there!"))   # the first set a subset of the second? Returns True
    set("Hi!").union(set(" there"))         # union- Returns set(['!', ' ', 'e', 'i', 'H', 'r', 't', 'h'])
    set("Hi!").intersection(set(" there"))  # intersection- Returns set([])
    x = set("Hi")                           # x is set(['i', 'H'])
    x.add("!")                              # x is set(['i', 'H', '!'])

Exercises
==================

1.
----
Create a dictionary containing name, city, and cake for Chris from Seattle who likes Chocolate. Display the dictionary. Delete the entry for cake. Display the dictionary. Add an entry for fruit with "Mango" and display the dictionary. Display the dictionary keys. Display the dictionary values. Display whether or not cake is a key in the dictionary (i.e. False). Display whether or not "Mango" is a value in the dictionary.

2.
----
Using the dict constructor and zip, build a dictionary of numbers from zero to fifteen and the hexadecimal equivalent (string is fine).

3.
----
Using the dictionary from item 1: Make a dictionary using the same keys but with the number of 't's in each value.

4.
----
Create sets s2, s3 and s4 that contain numbers from zero through twenty divisible 2, 3 and 4. Display the sets. Display if s3 is a subset of s2 (False) and if s4 is a subset of s2 (True).

5.
----
Create a set with the letters in 'Python' and add 'i' to the set. Create a frozenset with the letters in 'marathon' and display the union and intersection of the two sets.



