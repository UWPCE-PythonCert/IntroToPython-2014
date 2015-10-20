'''def grid_printer():
    top = ('+' + ('-' * 4)) * 2 + '+\n'
    side = ('|' + (' ' * 4)) * 2 + '|\n'
    return top + side * 4 + top + side * 4 + top
print(grid_printer())'''

def grid_printer(x,y,z): # x is width, y is height, z is number of columns
    top = ("+" + ("-" * x)) * z + "+\n"
    side = ("|" + (" " * x)) * z + "|\n"
    return top + side * y + top + side * y + top

print(grid_printer(5,3,3))


