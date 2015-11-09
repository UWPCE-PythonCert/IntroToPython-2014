food_prefs = {"name": "Chris", "city": "Seattle", "cake": "chocolate",
              "fruit": "mango", "salad": "caesar", "pasta": "lasagna"}

print("{name} is from {city} he likes {cake} cake,\n{fruit} smoothies, extra dressing \
on his {salad}\nsalads and always asks for seconds of {pasta}.".format(**food_prefs))


#Using a list comprehension, build a dictionary of numbers from zero to fifteen and the hexadecimal
#equivalent (string is fine). (the hex() function gives you the hexidecimal representation of a number.)

numbs = [x for x in range(16)]
hex_numbs = [hex(x) for x in numbs]
print({x: y for x, y in zip(numbs, hex_numbs)})



# Do the previous entirely with a dict comprehension – should be a one-liner
print({i : hex(i) for i in range(16)})


# Using the dictionary from item 1: Make a dictionary using the same keys but
# with the number of ‘a’s in each value. You can do this either by editing the
# dict in place, or making a new one. If you edit in place, make a copy first!

food_prefs2 = {"name": "Chris", "city": "Seattle", "cake": "chocolate",
              "fruit": "mango", "salad": "caesar", "pasta": "lasagna"}

food_aa = {key: value.count("a") for key, value in food_prefs2.items()}
print(food_aa)

