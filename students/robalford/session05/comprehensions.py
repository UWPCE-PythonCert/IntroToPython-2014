# 1

food_prefs = {"name": u"Chris",
              u"city": u"Seattle",
              u"cake": u"chocolate",
              u"fruit": u"mango",
              u"salad": u"greek",
              u"pasta": u"lasagna"}

# Is this the preferred (Pythonic) style for wrapping long lines of text?
person_likes_food = ('{name} is from {city}, '
                     'and he likes {cake} cake, '
                     '{fruit} fruit, {salad} salad '
                     'and {pasta} pasta.').format(**food_prefs)

# 2

hex_numbers = {}

hexes = [hex(number) for number in range(1, 16)]

for counter, value in enumerate(hexes):
    hex_numbers[counter+1] = value

# 3

hex_numbers_2 = {number: hex(number) for number in range(1, 16)}

# 4

new_dict = food_prefs.copy()

a_counter = {key: value.count('a') for key, value in new_dict.items()}

# 5

# s2 = {number for number in range(21) if number % 2 == 0}
# s3 = {number for number in range(21) if number % 3 == 0}
# s4 = {number for number in range(21) if number % 4 == 0}

# sets = []

# for num in range(2, 5):
#     sets.append({number for number in range(21) if number % num == 0})

sets = [{number for number in range(21) if number % num == 0} for num in range(2, 5)]
