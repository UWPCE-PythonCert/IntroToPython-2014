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

s1 = set()
s2 = set()
s3 = set()
for k in range(20):
    if k % 2 == 0:
        s1.update([k])
    if k % 3 == 0:
        s2.update([k])
    if k % 4 == 0:
        s3.update([k])
print s1
print s2
print s3