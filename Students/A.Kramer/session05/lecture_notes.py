'''
Created on Oct 28, 2014

@author: Aleksey
'''

# Review
d = {}
d[1] = "that"
d[2] = "this"
print d
    
for key in sorted(d.keys()):
    print key, d[key]
print
    
# Advanced arguments passing
def f(x, y, w=0, h=0):
    print "position: %s, %s --shape: %s, %s" %(x, y, w, h)

f (3, 4, h=7)

shape = {'w':40, 'h':60}

# positional arguments followed by the dictionary
f(3, 4, **shape)

def f1(*args, **kwargs):
    print "the positional arguments are:", args
    print "the keyword arguments are:", kwargs

# Returns empty tulpe for *args and empty dictionary for *kwargs
f1()
    
formatter = "My name is {first} {last}"

person = {'first':'Chris', 'last':'Baker'}
print formatter.format(2, 1, **person)

print 

g = {}
g["fore_color"]="white"
g["back_color"]="green"
g["link_color"]="blue"
g["visited_color"]="maroon"

def colors1(**kwargs):
    print "the colors are %s, %s, %s, %s" %(tuple(kwargs.values()))
    
colors1(**g)

print

# Print unknowun number of arguments
def print_everything(*args):
    for count, thing in enumerate(args):
        print '{0}. {1}'.format(count, thing)
print_everything('apple', 'banana', 'cabbage')

print

# print unknown number of items
def table_things(**kwargs):
    for name, value in kwargs.items():
        print '{0} = {1}'.format(name, value)
table_things(apple='fruit', cabbage='vegetable')

# Print whole dictionary
table_things(**g)

print

def my_d(**kwargs):
    for name, value in kwargs.items():
        print "The {0} is {1}".format(name, value)
my_d(**g)

print

def print_three_things(a, b, c):
    print 'a = {0}, b = {1}, c = {2}'.format(a,b,c)
mylist = ['aardvark', 'baboon', 'cat']
print_three_things(*mylist)

lst = [i for i in range(5)]
print lst

lst1 = [i * 4 for i in range(5)]
print lst1

lst2 = ['first', 'that', 'the', 'other']
lst3 = [s.upper() for s in lst2]
print lst3

lst4 = [ (i, j) for i in range(3) for j in range(4,6)]
print lst4

lst5 = [s.upper() for s in lst2 if s.startswith('t')]
print lst5

lst6 = [name for name in dir(__builtins__) if "Error" in name]
for l in lst6:
    print l

print

# List Comprehension
feast = ['lambs', "sloths", "orangutans", "breakfast cereals", "fruit bats"]
comprehansion = [delicacy.capitalize() for delicacy in feast]
print comprehansion[0]
print comprehansion[2]
print
comprehension = [delicacy for delicacy in feast if len(delicacy) > 6]
print comprehension
print len(feast)
print len(comprehension)
print
list_of_tuples = [(1, 'lumberjack'), (2, 'inquisition'), (4, 'spam')]
comprehension = [ skit * number for number, skit in list_of_tuples ]
print comprehension[0]
print comprehension[2]
print
list_of_eggs = ['poached egg', 'fried egg']
list_of_meats = ['lite spam', 'ham spam', 'fried spam']
comprehension = [ '{0} and {1}'.format(egg, meat) for egg in list_of_eggs for meat in list_of_meats]
print len(comprehension)
for i in comprehension:
    print i
print 
comprehension = { x for x in 'aabbbcccc'}
print comprehension
print
dict_of_weapons = {'first': 'fear', 'second': 'surprise', 'third':'ruthless efficiency', 'forth':'fanatical devotion', 'fifth': None}
dict_comprehension = { k.upper(): weapon for k, weapon in dict_of_weapons.iteritems() if weapon}
print 'first' in dict_comprehension
print 'FIRST' in dict_comprehension
print len(dict_of_weapons)
print len(dict_comprehension)
