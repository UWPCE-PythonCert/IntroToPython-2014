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

mydict2 = {"0"}
