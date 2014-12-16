# a function which takes on a single argument defining the size
# of a grid to draw

def print_grid(gridsize):
    # define the top and bottom portion of a single grid cell
    corner = "+"
    midtopbot = 4 * "-"

    # define the center of a single grid cell
    gridcenter = "|" + 4 * " "

    # define how to draw the complete top, bottom, and middle of the 
    # full grid in a single direction
    topbot = gridsize * (corner + midtopbot) + corner
    center = gridsize * gridcenter + "|"

    # build the grid in one direction
    onedirgrid = topbot + "\n"
    onedirgrid += 4 * (center + "\n")

    #build the full grid
    grid = gridsize * onedirgrid + topbot

    # now print the grid
    print grid

