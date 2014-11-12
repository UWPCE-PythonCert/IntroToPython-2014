# creating the food list
food_prefs = {"name": "Andrew", "city": "Bellevue", "cake": "rum", "fruit": "cherry", "salad": "caesar", "pasta": "ravioli"}

print "{name} is from {city}, and he likes {cake} cake, {fruit} fruit, {salad} salad, and {pasta} pasta.".format(**food_prefs)


#  building a hex dictionary with list comprehension
nums = range(16)

hex_list = [hex(num) for num in nums]

hex_zipped = dict(zip(nums, hex_list))

print hex_zipped


# building a hex dictionary with dict comprehension
hex_dict = {num: hex(num) for num in nums}

print hex_dict


# Using the dictionary from food_prefs: make a dictionary of 'a's and 'A's

a_dict = {}
for key, val in food_prefs.items():
    a_dict[key] = val.count('a') + val.count('A')
print a_dict


# creating sets s2, s3, s4

s2 = set()
s3 = set()
s4 = set()
for i in range(21):
    if not i%2:
        s2.add(i)
    if not i%3:
        s3.add(i)
    if not i%4:
        s4.add(i)

print s2
print s3
print s4


# creating sets s2, s3, s4 as set comprehensions

s2_set = {i for i in range(21) if not i%2}
s3_set = {i for i in range(21) if not i%3}
s4_set = {i for i in range(21) if not i%4}

print s2_set
print s3_set
print s4_set


# creating a sequence of all 3 sets

s2_new = set()
s3_new = set()
s4_new = set()

all_s_set = [[s2_new], [s3_new], [s4_new]]

for i in range(21):
	if not i%2:
		s2_new.add(i)
	if not i%3:
		s3_new.add(i)
	if not i%4:
		s4_new.add(i)

print all_s_set