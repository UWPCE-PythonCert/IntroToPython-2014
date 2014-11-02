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


dict_comprehension = {k: hex(k) for k in range(16)}
