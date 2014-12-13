"""
String lab 4.1
"""

# write the first 3 number are %i, %i, %i for an arbitrary number of values

rand_list = [1, 3, 5, 7, 13, 25.4]

v1 = len(rand_list)
print 'The first {v1:d} numbers are:'.format(v1=v1),

for i, n in enumerate(rand_list):
    if i != v1 - 1:
        print '{n_value:d}, '.format(n_value=int(n)),
    else:
        print '{n_value:d}.'.format(n_value=int(n)),
