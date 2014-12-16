__author__ = 'Robert W. Perkins'


d = {'name': 'Chris', 'city': 'Seattle', 'cake': 'Chocolate'}
print d
d.pop('cake')
print d
d['fruit'] = 'Mango'
print d
print d.keys()
print d.values()
print 'cake' in d
print 'Mango' in d.values()

int_list = []
hex_list = []
for i in range(16):
    int_list.append(i)
    hex_list.append(hex(i))

h_ex={}
for k, l in zip(int_list, hex_list):
    h_ex[k] = l
print h_ex

d_prime = {}
for k, v in d.items():
    d_prime[k] = v.count('t')
print d_prime

s2 = set()
s3 = set()
s4 = set()
for k in range(20):
    if k % 2 == 0:
        s2.update([k])
    if k % 3 == 0:
        s3.update([k])
    if k % 4 == 0:
        s4.update([k])
print s2
print s3
print s4
print s3.issubset(s2)
print s4.issubset(s2)

p_set = {'P', 'y', 't', 'h', 'o', 'n'}
p_set.update(['i'])
m_set = frozenset(('m', 'a', 'r', 'a', 't', 'h', 'o', 'n'))
print p_set.union(m_set)
print p_set.intersection(m_set)
