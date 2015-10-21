def print_grid():
	top =  ('+ ' + '- ' * 4) * 2 + '+\n'
	sides = ('| ' + '  ' * 4) * 2 + '|\n'
	return (top + sides * 4) * 2 + top

print(print_grid())


def one_var(n):

	size = int(n/2)

	top =  ('+ ' + '- ' * size) * 2 + '+\n'
	sides = ('| ' + ' ' * 2 * size) * 2 + '|\n'

	row = top + sides * size

	grid = (row * 2 + top)

	print(grid)


one_var(11)


def two_vars(w, h):
	size = int(w/2)

	top =  ('+ ' + '- ' * size) * 2 + '+\n'
	sides = ('| ' + ' ' * 2 * size) * 2 + '|\n'

	row = top + sides * size

	grid = (row * h + top)

	print (grid)

two_vars(11, 7)


