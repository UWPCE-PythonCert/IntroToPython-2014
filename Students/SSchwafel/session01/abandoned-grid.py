#!/usr/bin/python



#characters_wide_tall = input('How many characters wide/tall do you want your box to be?: ')

##
## This code Works! - Commented to debug
##
#def print_grid(box_dimensions):
#
#    box_dimensions = int(box_dimensions)
#
#    box_dimensions = (box_dimensions - 3)/2
#
#    print box_dimensions
#
#    if box_dimensions % 2 == 0 and box_dimensions != 2:
#    
#        print '+ ','- ' * box_dimensions,'+ ','- ' * box_dimensions,'+'
#
#        for i in range(box_dimensions):
#
#             print '| ','  ' * box_dimensions,'| ','  ' * box_dimensions,'| '
#
#        print '+ ','- ' * box_dimensions,'+ ','- ' * box_dimensions,'+'
#
#        for i in range(box_dimensions):
#
#             print '| ','  ' * box_dimensions,'| ','  ' * box_dimensions,'| '
#
#        print '+ ','- ' * box_dimensions,'+ ','- ' * box_dimensions,'+'
#        
#        #return True
#
#    else: 
#
#        print "That's an even number, but the box must have an odd-numbered dimension"
#        
#        return
#
#</ End working chunk>
#
#

how_many_boxes = input("Please enter how many boxes wide you'd like your grid: ")

def print_3x3_grid(how_many_boxes):

    how_many_boxes = int(how_many_boxes)

    for i in range(how_many_boxes):

        print '+ ',
        print '- ', 
        print '- ', 
        print '- ', 
        print '- ', 
        print '- ', 
        print '+'

    
        for i in range(5):
            print '| ','  ' * 7 ,'|'

        print '+ ',
        print '- ', 
        print '- ', 
        print '- ', 
        print '- ', 
        print '- ', 
        print '+'

print_3x3_grid(how_many_boxes)
