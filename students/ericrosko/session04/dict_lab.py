'''
Eric Rosko
Nov. 17, 2015
Session04 
LAB: Dictionaries and Sets lab
'''
from collections import KeysView
from collections import ValuesView

d = {'name':'Chris','city':'Seattle','cake':'Chocolate'}
print(d)

del d['cake']
print(d)

d['fruit']='Mango'
print(d)

assert isinstance(d.keys(),KeysView)
print(d.keys())

assert isinstance(d.values(), ValuesView)
print(d.values())

print("Cake is Key in Dictionary: {}".format('cake' in d.keys() ) )
print("Mango is Value in Dictionary: {}".format('Mango' in d.values() ) )

d2 = dict()
for item in d.keys():
	count=0
	for n in d[item]:
		if n=='t':
			count+=1
	d2[item]=count

print(d2) #{'name': 0, 'city': 2, 'fruit': 0}

s2=set()
s3=set()
s4=set()

for x in range(0,21):
	if x%2==0:
		s2.add(x)
	if x%3==0:
		s3.add(x)
	if x%4==0:
		s4.add(x)

print("s2: {}".format(s2))
print("s3: {}".format(s3))
print("s4: {}".format(s4))
print("Is s3 a subset of s2?: {}".format(s3.issubset(s2)))
print("Is s4 a subset of s2?: {}".format(s4.issubset(s2)))

ipython=set()
for n in 'ipython':
	ipython.add(n)

frozen = frozenset('marathon')
print()
print("set1: {}\nset2: {}".format(ipython,frozen))
print('intersection: {}'.format(ipython.intersection(frozen)))
print('union: {}'.format(ipython.union(frozen)))


