import collections


def count_t(v):
    c = collections.Counter(v)
    return c['t']

d = {'name': 'Chris', 'city': 'Seattle', 'cake': 'chocolate'}
print(d)
del d['cake']
print(d)
d['fruit'] = 'Mango'
print (d)

print(d.keys())
print(d.values())
'cake' in d
'Mango' in d

d2 = {}
for k, v in d.items():
    d2[k] = count_t(v)

print(d2)


s2 = set()
s3 = set()
s4 = set()

s2.update([i for i in range(21) if i % 2 == 0])
s3.update([i for i in range(21) if i % 3 == 0])
s4.update([i for i in range(21) if i % 4 == 0])

print(s2)
print(s3)
print(s4)

if s3.issubset(s2):
    print("s3 is a subset of s2")
else:
    print("s3 is not a subset of s2")

if s4.issubset(s2):
    print("s4 is a subset of s2")
else:
    print("s4 is not a subset of s2")

p = set()
l = []
l += 'python'
p.update(l)
p.update(['i'])

l = []
l += 'marathon'
m = frozenset(l)

print(p.union(m))
print(p.intersection(m))
