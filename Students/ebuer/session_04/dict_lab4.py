"""
Dictonary Lab 4.1 -- fun with dictionaries
"""

practice_dict = {'name': 'Chris', "city": 'Seattle', "cake": 'Chocolate'}

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


# Part 4.2 -- a hexadecimal dictionary from a range

r = range(16)
h = []

for n in r:
    h.append(hex(n))

hex_dict = dict(zip(r, h))

# Part 4.3 Recode first dictionary to show number of 't's in each value

t_dict = {}

for vname, n in practice_dict.iteritems():
    n = vname.count('t')
    t_dict.update(vname=n)

for k, v in t_dict.iteritems():
    print "Key: {k}, number of t's: {v}".format(k=k, v=v)

# Part 4.4 working with sets

seed_nums = range(21)

s2 = []
s3 = []
s4 = []

for s in seed_nums:
    if s % 2 == 0:
        s2.append(s)
    if s % 3 == 0:
        s3.append(s)
    if s % 4 == 0:
        s4.append(s)

s2 = set(s2)
s3 = set(s3)
s4 = set(s4)

print '\n'
print s2.issubset(s3)
print s4.issubset(s2)

# part 4.5 python set
s5 = set()
temp = 'python'
for l in temp:
    s5.add(l)

s5.add('i')

temp = 'marathon'
s6 = []
for l in temp:
    s6.append(l)

s6 = frozenset(s6)

print "Here's the union: {setvar}".format(setvar=s5.union(s6))
print "Here's the intersection: {setvar:s}".format(setvar=s5.intersection(s6))
