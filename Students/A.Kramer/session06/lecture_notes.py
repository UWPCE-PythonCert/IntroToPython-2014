'''
Created on Nov 5, 2014

@author: Aleksey Kramer
'''
# lambda usage
f = lambda x, y: x + y

print f(2,3)

# Each element in the list is a function
l = [lambda x, y: x + y]
print type(l[0])
print l[0](3,3)

# the same as above but using def: declaration
def fun(x, y):
    return x + y

l = [fun]
print type(l[0])
print l[0](3,3)

# Functional Programming

# map function
l = [2,5,7,12,6,4]
def fun1(x):
    return x*2 + 10
print map(fun1, l)

# or the same as above, but with lambda
print map(lambda x: x*2 + 10, l)

# filter function
l = [2, 5, 7, 12, 6, 4]
print filter(lambda x: not x%2, l)

l = [1, 0, 2.3, 0.0, 'text', '', [1,2], [], False, True, None ]
print filter(None, l)

# reduce function
# to sum all the items with reduce
l = [2, 5, 7, 12, 6, 4]
print reduce(lambda x,y: x+y, l)

# to multiply all the items with reduce
print reduce(lambda x,y: x*y, l)
# or
import operator
print reduce(operator.mul, l)

# more about lambda - loading lambda functions in the list
# and using the list later on
l = []
for i in range(3):
    l.append(lambda x, e=i: x**e)
for f in l:
    print f(3)


# 




if __name__ == "__main__":
    pass