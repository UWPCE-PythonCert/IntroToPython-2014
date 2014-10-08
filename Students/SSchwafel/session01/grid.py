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

user_dimensions = raw_input("Please enter how many characters wide you'd like your 3x3 grid: ")

def print_3x3_grid(box_dimensions):

    box_dimensions = int(user_dimensions)

    box_dimensions = box_dimensions

    print box_dimensions

    if box_dimensions % 3 == 0 and box_dimensions != 3:
    
        box_dimensions = (box_dimensions - 1) / 3

        print '+ ','- ' * box_dimensions,'+ ','- ' * box_dimensions,'+','- ' * box_dimensions,'+'

        for i in range(box_dimensions):

             print '| ','  ' * box_dimensions,'| ','  ' * box_dimensions,'| ','  ' * box_dimensions,'| '

        print '+ ','- ' * box_dimensions,'+ ','- ' * box_dimensions,'+','- ' * box_dimensions,'+'

        for i in range(box_dimensions):

             print '| ','  ' * box_dimensions,'| ','  ' * box_dimensions,'| ','  ' * box_dimensions,'| '

        print '+ ','- ' * box_dimensions,'+ ','- ' * box_dimensions,'+','- ' * box_dimensions,'+'

        for i in range(box_dimensions):

             print '| ','  ' * box_dimensions,'| ','  ' * box_dimensions,'| ','  ' * box_dimensions,'| '

        print '+ ','- ' * box_dimensions,'+ ','- ' * box_dimensions,'+','- ' * box_dimensions,'+'

print_3x3_grid(user_dimensions)

