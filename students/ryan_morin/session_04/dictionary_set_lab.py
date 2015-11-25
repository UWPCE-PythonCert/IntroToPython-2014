__author__ = 'Ryan'

#Question#1
food = dict()
food['name'] = 'Chris'
food['city'] = 'Seattle'
food['cake'] = 'Chocolate'

print(food)

del food['cake']
print (food)

food['fruit'] = 'mango'
print (food.keys())
print (food.values())


def key_exist(d):
    if 'cake' in food.keys():
        return True
    else:
        return ('Not there')

def key_exist2(d):
    if 'mango' in food.values():
        return True
    else:
        return ('Not there')

print (key_exist(food))
print (key_exist2(food))

#Question#2
counter = 0
for i in food:
    counter += 1
    t_accum = ('t' * counter)
    food[i] = t_accum
print (food)

#Question#3
e = {i for i in range(21)}
s2 = e.copy()
s3 = e.copy()
s4 = e.copy()

s2 = {i for i in e if i%2 == 0}
s3 = {i for i in e if i%3 == 0}
s4 = {i for i in e if i%4 == 0}

print(s2,s3,s4)

def subs_2_4():
    if s4.issubset(s2):
        return True
    else:
        return False

def subs_3_2():
    if s3.issubset(s2):
        return True
    else:
        return False

print (subs_2_4())
print (subs_3_2())

#Question#4
outpt = [i for i in 'python']
py_set = set(outpt)
py_set.add('i')
print (py_set)

f = frozenset('marathon')
print(f.union(py_set))
print(f.intersection(py_set))