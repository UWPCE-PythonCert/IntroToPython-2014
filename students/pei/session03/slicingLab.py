# Ex1:
s = "this is to test sequence slicing"

"""
    return a sequence with the first and last items exchanged
"""
def slice(str):
    if len(str) <=1:
        return str
    else:   
        return str [-1] + str [1: (len(str) -1)] + str [0]
# test
print (slice(s))

# Ex2:
tup1 = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10);

"""
    return a sequence with every other item removed
"""
def skip1(tuple):
    return tuple[ 0 : : 2 ]
# test
print (skip1(tup1))

# Ex3:
"""
    return a sequence with the first and last 4 items 
    removed, and every other item in between
"""
def ex3(tuple):
    return tuple[ 4 :-4: 2 ]
# test
print (ex3(tup1))

#Ex4:
"""
    return a sequence reversed (just with slicing)
"""
def eeversed(tuple):
    return tuple[ : : -1 ]
# test
print (reversed(tup1))

#Ex5:
"""
    return a sequence with the middle third, 
    then last third, then the first third in the new order
"""
def third(tuple):
    i = len(tuple)//3
    return tuple[i:-i] + tuple [-i:] + tuple [:i]
# test
print (third(tup1))

