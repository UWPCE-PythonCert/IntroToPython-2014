#!/usr/bin/env python3


d = {
    'name' : 'Chris',
    'city' : 'Seattle',
    'cake' : 'Chocolate',
}

print(d)
d.pop('cake')
print(d)
d['fruit'] = 'Mango'
for k in d.keys():    
    print(k)
for v in d.values():
    print(v)
if not 'cake' in d: print("no cake")
if 'Mango' in d.values(): print("have Mango")
    
