#!/usr/bin/python
def print_grid():

    #box_dimensions = input('How many characters wide do you want each quarter box?: ')
    box_dimensions = input('How many characters wide/tall do you want your box to be?: ')

    box_dimensions = int(box_dimensions)
    box_dimensions = (box_dimensions - 3) /2

    #print type(box_dimensions)

    print '+ ','- ' * box_dimensions,'+ ','- ' * box_dimensions,'+'

    for i in range(box_dimensions):

         print '| ','  ' * box_dimensions,'| ','  ' * box_dimensions,'| '

    print '+ ','- ' * box_dimensions,'+ ','- ' * box_dimensions,'+'

    for i in range(box_dimensions):

         print '| ','  ' * box_dimensions,'| ','  ' * box_dimensions,'| '

    print '+ ','- ' * box_dimensions,'+ ','- ' * box_dimensions,'+'
    
    return True

print_grid()
