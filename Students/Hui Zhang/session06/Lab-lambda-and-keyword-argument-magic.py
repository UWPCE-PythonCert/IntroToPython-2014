

# Use a for loop, lambda, and a keyword argument
l = []

for i in range(5):
    l.append(lambda x, e = i: e + 5)


for f in l:
    print f(5)

#the output is below:
5
6
7
8
9

In [65]: 


# Do it with a list comprehension, instead of a for loop
l = []

for i in range(5):
    l.append(lambda x, e = i: e + 5)


for f in l:
    print f(5)

#the output is below:
5
6
7
8
9

In [65]: 