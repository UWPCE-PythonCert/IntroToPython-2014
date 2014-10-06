#!/usr/bin/python



user_dimensions = input('How many characters wide/tall do you want your box to be?: ')


def print_grid(box_dimensions):

    #box_dimensions = input('How many characters wide do you want each quarter box?: ')

    box_dimensions = int(box_dimensions)

    box_dimensions = (box_dimensions - 3) /2

    if box_dimensions % 2 == 0:
    
        print '+ ','- ' * box_dimensions,'+ ','- ' * box_dimensions,'+'

        for i in range(box_dimensions):

             print '| ','  ' * box_dimensions,'| ','  ' * box_dimensions,'| '

        print '+ ','- ' * box_dimensions,'+ ','- ' * box_dimensions,'+'

        for i in range(box_dimensions):

             print '| ','  ' * box_dimensions,'| ','  ' * box_dimensions,'| '

        print '+ ','- ' * box_dimensions,'+ ','- ' * box_dimensions,'+'
        
        #return True

    else: 

        print "That's an even number, but the box must have an odd-numbered dimension"
        
        return


print_grid(user_dimensions)
