#! /usr/bin/env python3

d = {
    'name' : 'Chris',
    'city' : 'Seattle',
    'cake' : 'Chocolate',
}

nd = {
    
}


for k, v in d.items():
    t = 0
    if 't' in v:
        for c in v:
            if c == 't':
                t = t +1
    nd[k] = t
    
print(nd)