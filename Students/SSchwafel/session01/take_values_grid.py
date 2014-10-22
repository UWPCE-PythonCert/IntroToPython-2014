#!/usr/bin/python




#how_many_boxes_tall = raw_input("How many boxes tall do you want your grid? ")

def print_grid():

    width = raw_input("Please enter how many characters wide you'd like your boxes: ")
    width = int(width)

    height = raw_input("Please enter how tall you'd like your boxes ")
    height = int(height)

    how_many_boxes_wide = raw_input("How many boxes wide do you want your grid? ")
    how_many_boxes_wide = int(how_many_boxes_wide)

    for i in range(how_many_boxes_wide):

        print '\n+ ','- ' * width,'+ '

        for i in range(height):

            print '| ','  ' * width,'| '

        print '+ ','- ' * width,'+ '

print_grid()

