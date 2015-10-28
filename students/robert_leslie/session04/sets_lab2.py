#! /usr/bin/env python3

s = set()

for c in 'Python':
    s.update(c)
    
s.update('i')


s2 = frozenset(('M','a','r','a','t','h','o','n'))

    
print(s.union(s2))
print(s.intersection(s2))