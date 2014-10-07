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

box_dimensions = input("Please enter how many characters wide you'd like your grid: ")

def print_3x3_grid(box_dimensions):

    box_dimensions = int(box_dimensions)

# check to see if entered value is odd/even
# If entry is ODD, there are an even number of boxes, if entry is EVEN, there are an odd number of boxes

    if box_dimensions % 2 == 0:
        
        print '\nbox_dimensions is even'
        
    #Figure out how big each box will be 

        print 
        print

        individual_box_size = box_dimensions/2

        print individual_box_size

        print 
        print

        #this line figures out how many -- to print ( and subtracts +)

        dashes_in_boxes = individual_box_size - 2

        for i in range(box_dimensions):

            print '+ ',

            for i in range(dashes_in_boxes - 1):
            
                print '- ' * dashes_in_boxes,

                print '+ ',
            

            print '+ '

    if box_dimensions % 2 != 0:

        print "box_dimensions is odd" 

    rows_and_grids  = box_dimensions

    #box_dimensions = (box_dimensions - 3)/2

    #print box_dimensions
    
    #print rows_and_grids

    #if box_dimensions % 2 == 0 and box_dimensions != 2:
    
   # for i in range(box_dimensions):
    
   #     print '+ ',
   #     print '- ' * box_dimensions,

   # for i in range(box_dimensions):

   #      print '| ','  ' * box_dimensions,'| ','  ' * box_dimensions,'| '

   # print '+ ','- ' * box_dimensions,'+ ','- ' * box_dimensions,'+'

   # for i in range(box_dimensions):

#         print '| ','  ' * box_dimensions,'| ','  ' * box_dimensions,'| '
#
#    print '+ ','- ' * box_dimensions,'+ ','- ' * box_dimensions,'+'
#        
#        #return True
#
#    else: 
#
#        print "That's an even number, but the box must have an odd-numbered dimension"
#        
#        return
#
#print_grid(characters_wide_tall)

print_3x3_grid(box_dimensions)
