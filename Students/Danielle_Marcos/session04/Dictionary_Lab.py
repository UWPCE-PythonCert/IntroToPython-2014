mydict = {'name': 'Chris', 'city': 'Seattle', 'cake': 'Chocolate'}
print mydict

mydict.pop('cake')
print mydict

mydict['fruit'] = 'Mango'
print mydict

print mydict.keys()
print mydict.values()

if 'cake' in mydict.keys():
	print True
else: 
	print False

if 'Mango' in mydict.values():
	print True
else:
	print False

list1 = range(15)
list2 = []

for i in list1:
	print i
	print hex(i)
	list2.append(hex(i))
	print list2

myzip = zip (list1,list2)
print myzip

mydict2 = dict(myzip)
print mydict2

mydict3 = mydict.keys()
print mydict3


for i in mydict.values():
	print i
	if 't' in i:
		print i
		print i.count('t')

s2 = set([2,4,6,8,10,12,14,16,18,20])
s3 = set([3,6,9,12,15,18])
s4 = set([4,8,12,16,20])

print s2
print s3
print s4

print s3.issubset(s2) 
print s4.issubset(s2)

s5 = set(['P','y','t','h','o','n'])
print s5
s5.add('i')
print s5

fs = frozenset(('m','a','r','a','t','h','o','n'))
print fs

print s5.union(fs,)
print s5.intersection(fs,)





