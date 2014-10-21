"""
Dictonary Lab 4.1 -- fun with dictionaries
"""

practice_dict = {'name': 'Chris', "city": 'Seattle', "cake": 'Chocolate'}

# print practice_dict.keys()
# print practice_dict.values()

print 'Original dict:'
for k, v in practice_dict.items():
    print '{key}: {item}'.format(key=k, item=v)

practice_dict.pop('cake')

print '\nRevised dict:'
for k, v in practice_dict.items():
    print '{key}: {item}'.format(key=k, item=v)

practice_dict.setdefault('fruit', 'mango')

print '\nAdded dict:'
for k, v in practice_dict.items():
    print '{key}: {item}'.format(key=k, item=v)

print '\nDict Keys and values:'
for i, j in zip(practice_dict.keys(), practice_dict.values()):
    print 'Key: {key: <15} Value: {val: <15}'.format(key=i, val=j)

# using view items to check for membership
cake_var = 'cake' in practice_dict.viewkeys()
mango_var = 'mango' in practice_dict.viewvalues()

print '\nCake in dict: {cake}\nMango in dict: {mango}'\
    .format(cake=cake_var, mango=mango_var)


"""
Part 4.2 -- a hexadecimal dictionary from a range
"""

r = range(16)
h = []

for n in r:
    h.append(hex(n))

hex_dict = dict(zip(r, h))

"""
Part 4.3 Recode first dictionary to show number of 't's in each value
"""

new_keys = practice_dict.keys()
new_values = []

for vname in practice_dict.itervalues():
    n = 0
    for l in vname:
        if l == 't':
            n += 1
    new_values.append(n)

t_dict = dict(zip(new_keys, new_values))

for k, v in t_dict.iteritems():
    print 'Key: {k}, number of ts: {v}'.format(k=k, v=v)

# Part 4.4 working with sets

