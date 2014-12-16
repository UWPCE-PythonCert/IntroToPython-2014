##sum_double excercise
##given two int values return sum unless the two are == then double sum


def sum_double(x, y):
    if x == y:
        return 2 * (x + y)
    else:
        return x + y

x = 3
y = 3
z = sum_double(x, y)

print "Solution: %i"% z
