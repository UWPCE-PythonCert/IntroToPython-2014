#! /usr/bin/env python3



l = ['Apples', 'Pears', 'Oranges', 'Peaches']

print(l)
r = input("Enter a fruit to add to the list: ")
l.append(r)
print(l)
n = input("Enter the number of fruits to display: ")
print(l[:int(n)])
l+=('Bananas',)
l.insert(0, 'Plums')
for f in l:
    if f.startswith('P'):
        print(f)
print(l)
l.pop()
print(l)
d = input("Which fruit would you like to remove: ")
l.remove(d)
print(l)
for f in l:
    yn = input("Do you like {}? ".format(f))
    while yn not in ('no','yes'):
        yn = input('yes or no? ')
    if yn == 'no':
        l.remove(f)
print(l)
l2 = l[:]
l.pop(-1)
print("Original: {}\nCopy: {}".format(l,l2))

            
        
