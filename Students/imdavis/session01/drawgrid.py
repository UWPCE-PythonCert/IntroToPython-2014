# draws a grid using the buildgrid function after prompting the
# user for the size of the grid

import buildgrid

try:
    size = int(raw_input("What size grid would you like to build? "))
    buildgrid.print_grid(size)
except ValueError:
    print "Please enter an integer!"