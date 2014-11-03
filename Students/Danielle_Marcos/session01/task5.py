def print_grid(size):
	number = 2
	box_size = int((size-1) // 2)
print "box_size", box_size

    top = ('+' + '-' * box_size) * number + '+' + '\\n'
    middle = ('|' + ' ' * 2 * box_size) * number + '|' + '\\n'

    row = top + middle*box_size

    grid = row*number + top

    print_grid()