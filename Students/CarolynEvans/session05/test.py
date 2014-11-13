from comps_tested import count_evens, print_food_prefs, hex_dict, count_a, mod_0_list

assert count_evens([2, 1, 2, 3, 4]) == 3
assert count_evens([2, 2, 0]) == 3
assert count_evens([1, 3, 5]) == 0



food_prefs = {"name": u"Chris",
              u"city": u"Seattle",
              u"cake": u"chocolate",
              u"fruit": u"mango",
              u"salad": u"greek",
              u"pasta": u"lasagna"}

assert print_food_prefs(food_prefs) == 'Chris is from Seattle, and he likes chocolate cake, mango fruit, greek salad, and lasagna pasta.'

assert str(hex_dict()) == "{0: '0x0', 1: '0x1', 2: '0x2', 3: '0x3', 4: '0x4', 5: '0x5', 6: '0x6', 7: '0x7', 8: '0x8', 9: '0x9', 10: '0xa', 11: '0xb', 12: '0xc', 13: '0xd', 14: '0xe', 15: '0xf'}"

assert str(count_a(food_prefs)) == "{u'city': 1, 'name': 0, u'salad': 0, u'cake': 1, u'fruit': 1, u'pasta': 3}"

assert str(mod_0_list(2, 3, 4, start=0, end=20))== "[[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20], [0, 3, 6, 9, 12, 15, 18], [0, 4, 8, 12, 16, 20]]"