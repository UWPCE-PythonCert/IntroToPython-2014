##1. Print the dict by passing it to a string format method, so that you get something like:

    “Chris is from Seattle, and he likes chocolate cake, mango fruit,
        greek salad, and lasagna pasta”

food_prefs = {u"name": u"Chris",
              u"city": u"Seattle",
              u"cake": u"chocolate",
              u"fruit": u"mango",
              u"salad": u"greek",
              u"pasta": u"lasagna"}

u"{name} is from {city}, and he likes {cake} cake, {fruit} fruit, {salad} salad,and {pasta} pasta".format(**food_prefs)

#2. Using a list comprehension, build a dictionary of numbers from zero to fifteen and the hexadecimal equivalent (string is fine).              
comb_dict={}
list1=range(0,16)

for i in list1:
    h= hex(i)
    list2.append(h)

comb_list = zip(list1, list2)

for num1, hexnum1 in comb_list:
    comb_dict[num1] = hexnum1

#3. Do the previous entirely with a dict comprehension – should be a one-liner
comb_dict={}
list1=range(0,16)

for i in list1:
    h= hex(i)
    list2.append(h)
comb_dict2 = dict(zip(num1, hexnum1))

#4. Using the dictionary from item 1: Make a dictionary using the same keys but with the number of ‘a’s in each value. 
#You can do this either by editing the dict in place,or making a new one. If you edit in place, make a copy first!
comb_dict={}
list1=range(0,16)

for i in list1:
    h= "a"*i
    list2.append(h)
comb_list = zip(list1, list2)
for num1, hexnum1 in comb_list:
    comb_dict[num1] = hexnum1

#5. Create sets s2, s3 and s4 that contain numbers from zero through twenty, divisible 2, 3 and 4.
#Do this with one set comprehension for each set.

s_0 = set(range(21))
set_2 = []
set_3 = []
set_4 = []

set_2 = {i for i in s_0 if i % 2 == 0 }
set_3 = {i for i in s_0 if i % 3 == 0 }
set_4 = {i for i in s_0 if i % 4 == 0 }

