#!/usr/bin/env python3

d = {'name':'Chris', 'city':'Seattle', 'cake':'chocolate'}
print(d)
d.pop('cake')
print(d)
d['fruit'] = 'mango'
print(d)
print(d.keys())
print(d.values())
print('cake' in d)
print('fruit' in d)
e= d.copy()
print('new e dict',e)
for k, v in e.items():
    e[k] = v.count('t')
print(e)