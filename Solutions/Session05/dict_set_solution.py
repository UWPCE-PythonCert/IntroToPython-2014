#!/usr/bin/env python

"""
dict/set lab solutions: Chris' version.
"""

food_prefs = {"name": "Chris",
              "city": "Seattle",
              "cake": "chocolate",
              "fruit": "mango",
              "salad": "greek",
              "pasta": "lasagna"}

# 1. Print the dict by passing it to a string format method, so that you
# get something like:

print("{name} is from Seattle, and he likes {cake} cake, {fruit} fruit,"
      "{salad} salad, and {pasta} pasta".format(**food_prefs))

# 2. Using a list comprehension, build a dictionary of numbers from zero
# to fifteen and the hexadecimal equivalent (string is fine).

print(dict([(i, hex(i)) for i in range(16)]))

# 3. Do the previous entirely with a dict comprehension -- should be a one-liner

print({i: hex(i) for i in range(16)})

# 4. Using the dictionary from item 1: Make a dictionary using the same
# keys but with the number of 'a's in each value. You can do this either
# by editing the dict in place, or making a new one. If you edit in place,
# make a copy first!

print({key: val.count('a') for key, val in food_prefs.items()})


# 5. Create sets s2, s3 and s4 that contain numbers from zero through twenty,
# divisible 2, 3 and 4.

#     a. Do this with one set comprehension for each set.
s2 = {i for i in range(21) if not i % 2}
s3 = {i for i in range(21) if not i % 3}
s4 = {i for i in range(21) if not i % 4}

print("\nHere are the three sets:")
print(s2)
print(s3)
print(s4)

#     b. What if you had a lot more than 3? -- Don't Repeat Yourself (DRY)
#        - create a sequence that holds all three sets
#        - loop through that sequence to build the sets up -- so no repeated code.

n = 5
divisors = range(2, n + 1)
# create a list of empty sets
sets = [set() for i in divisors]

# fill up the sets
for i, st in zip(divisors, sets):
    [st.add(j) for j in range(21) if not j % i]

print("\nHere are all the sets:\n", sets)


# c. Extra credit:  do it all as a one-liner by nesting a set comprehension
#    inside a list comprehension. (OK, that may be getting carried away!)

sets = [{i for i in range(21) if not i % j} for j in range(2, n + 1)]

print("\nHere are all the sets from the one liner:\n", sets)
