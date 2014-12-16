# sorting example

fruit = ['Apples', 'Pears', 'Oranges', 'Peaches']

numbers = range(4)

combined = zip(fruit, numbers)

def sort_func(item):
	return item[1]

combined.sort(key=sort_func)



# string formatting example

def print_me(nums):
	s = str(nums).strip('()')

	formatter = 'the first %d numbers are %s' 
	print 'formatter: ', formatter
	print formatter % (len(nums), s)

	return 

# dictionary examples

r = {
	1:'adlkf',
	2:';ajdf',
	3:'adfe',
	4: 1231
}

for k in r.keys():
	print k[r]



for k, v in r.items():
	print k, v


person = {
	'name':	'Jon Smith',
	'birthdate': ,	
}

# 'set()' example

s = set()
s.add(6)
s.add('2423')


# dictionary lab

Chris = {
	'name': 'Chris',
	'city': 'Seattle',
	'cake': 'Chocolate'
}

print Chris

Chris.pop('cake')

print Chris

Chris['fruit'] = 'Mango'

print Chris

print Chris.keys()
print Chris.values()

print 'cake' in Chris

print 'Mango' in Chris.values()



nums = range(16)
num_dict = {}

for n in nums:
	num_dict[n] = chr(n)



# date converter
from datetime import date

def convert_date(s='12/01/2014'):
	s = s.split('/')
	d = date(s[2],s[0],s[1]) # (yyyy,mm,dd)
	return d

# readline file
example = open('example.py','r')

for e in example:
	print e

# find all built-in errors
exp = [name for name in dir(__builtin__) else None]
print exp



# open files and counting the lines (of code, of course)
def line_count(file_path):
	file_path = open('example.py','r')
	file_path = file_path.read()
	return file_path.count('\n')






