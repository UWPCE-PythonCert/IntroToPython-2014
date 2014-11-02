__author__ = 'Robert W. Perkins'


food_prefs = {"name": u"Chris",
              u"city": u"Seattle",
              u"cake": u"chocolate",
              u"fruit": u"mango",
              u"salad": u"greek",
              u"pasta": u"lasagna"}

formatter = '{f_name} is from {f_city}, and he likes {f_cake} cake, {f_fruit} fruit, {f_salad} salad, and' \
            ' {f_pasta} pasta'

print formatter.format(f_name=food_prefs['name'], f_city=food_prefs['city'], f_cake=food_prefs['cake'],
                       f_fruit=food_prefs['fruit'], f_salad=food_prefs['salad'], f_pasta=food_prefs['pasta'])

num_list = [(i, hex(i)) for i in range(16)]
hex_dict = dict(num_list)
print hex_dict

dict_comprehension = {k: hex(k) for k in range(16)}
print dict_comprehension

food_letters = {food_key: food_prefs[food_key].count('a') for food_key in food_prefs}
print food_letters

s2 = {z for z in range(21) if z % 2 == 0}
s3 = {z for z in range(21) if z % 3 == 0}
s4 = {z for z in range(21) if z % 4 == 0}
print s2
print s3
print s4

set_seq = [set(), set(), set()]
for n in range(21):
    if n % 2 == 0:
        set_seq[0].update([n])
    if n % 3 == 0:
        set_seq[1].update([n])
    if n % 4 == 0:
        set_seq[2].update([n])
print set_seq

ec_list = [{n for n in range(21) if n % (s+2) == 0} for s in range(3)]
print ec_list