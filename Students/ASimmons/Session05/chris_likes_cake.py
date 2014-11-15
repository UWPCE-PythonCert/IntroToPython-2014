__author__ = 'asimmons'

# dictionary items
food_prefs = {"name": u"Chris",
              u"city": u"Seattle",
              u"cake": u"chocolate",
              u"fruit": u"mango",
              u"salad": u"greek",
              u"pasta": u"lasagna"}

# 1. Print the dict by passing it to a string format method

print("%(name)s is from %(city)s, and he likes %(cake)s cake, %(fruit)s fruit, %(salad)s salad, and %(pasta)s pasta!" % food_prefs)

## 2. Using a list comprehension, build a dictionary of numbers
## from zero to fifteen and the hexadecimal equivalent (string is fine).

# Displays the given dictionary
def iterateDict(a_dict):
    for key, value in a_dict.iteritems():
        print("{key} : {value}").format(key=key, value=value)

hexinums = [hex(x) for x in range(16)] # use 16 because it starts from 0
numsdic = dict(zip(range(16), hexinums))
print iterateDict(numsdic)

# 3. Do the same thing using dict comprehension

newdict = {i: hex(i) for i in range(16)}
iterateDict(newdict)

# 4. Using the dictionary from item 1: Make a dictionary using the same keys
# but with the number of a's in each value.
# Do this either by editing the dict in place, or making a new one.
# If you edit in place, make a copy first!

counta = {key: value.count('a') for key, value in food_prefs.iteritems()}

iterateDict(counta)

# 5a. Create sets s2, s3 and s4 that contain numbers from zero through twenty, divisible 2, 3 and 4.

s2 = set()

for i in range(21):
    if i % 2 == 0:
        s2.add(i)
print s2

s3 = set()

for i in range(21):
    if i % 3 == 0:
        s3.add(i)
print s3

s4 = set()

for i in range(21):
    if i % 4 == 0:
        s4.add(i)
print s4

#5b. make a sequence that holds all three sets, loop through the sequence

listofsets = [{sets for sets in range(21) if sets % (x+2) == 0} for x in range(3)]

print listofsets



