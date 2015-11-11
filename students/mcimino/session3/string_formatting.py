print("'file_00{}:\t {:.2f}, {:.0e}'".format(2, 123.4567, 10000))

# solution one
def print_n(n):
    str = 'the first {} numbers are: '.format(n)
    for i in range(n):
        str += '{}'.format(i+1)
        if i == n - 1:
            break
        str += ', '
    print(str)

for i in range(20):
    print_n(i+1)


# solution 2
def print_n(n):
    t = tuple(range(n))
    str = 'the first {} numbers are: '.format(n)
    str += '{}, ' * (n-1)
    str += '{}'

    print(str.format(*t))

print_n(7)
