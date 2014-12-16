##gridprinter python script
##written by EB 2014-10-04


def print_grid():
    separator = 2 * ('+' + 4 * ' -' + ' ') + '+' + '\n'
    walls = 2 * (('|' + 4 * '  ') + ' ') + '|' + '\n'

    print 2 * (separator + 4 * walls) + separator

print_grid()


def scale_grid(n):
    separator = 2 * ('+' + n * ' -' + ' ') + '+' + '\n'
    walls = n * (2 * (('|' + n * '  ') + ' ') + '|' + '\n')
    print 2 * (separator + walls) + separator

scale_grid(9)


def expand_grid(num_rows, scale_factor):
    separator = num_rows * ('+' + scale_factor * ' -' + ' ') + '+' + '\n'
    walls = scale_factor * (num_rows * (('|' + scale_factor * '  ')
                            + ' ') + '|' + '\n')
    print (num_rows * (separator + walls) + separator)

expand_grid(3, 4)
