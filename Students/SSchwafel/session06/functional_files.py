#!/usr/bin/python

import os
import sys

filename = sys.argv[1:]

def renamer(file_to_be_renamed):

    path = os.getcwd()

    files = os.listdir(path)

    if file_to_be_renamed in files:

        new_name = raw_input( "The current filename is {}, what would you like to call it instead? ".format(file_to_be_renamed))

        os.rename(file_to_be_renamed, new_name)
    
    else:
        print "It doesn't look like that file is present"

map(renamer,filename)


###UNUSED CODE FROM BEFORE I READ THE ASSIGNMENT ALL THE WAY###


#print filename

#path = os.getcwd()
#
#files = os.listdir(path)
#
#count = 1
#file_dict = {}
#while count<=len(files):
#
#    for i in files:
#        file_dict[count] = i
#        #print str(count) + ': '+ i
#        count = count + 1
#
#for key, value in file_dict.iteritems():
#    print key, value
#
#which_file = raw_input('\nWhich file would you like to rename? Please use the integer value. ')
#
#which_file = int(which_file)
#
#"print file_dict[which_file]
#
#file_to_be_renamed = file_dict[which_file]
#
#new_name = raw_input( "The current filename is {}, what would you like to call it instead? ".format(file_to_be_renamed))
#
#os.rename(file_to_be_renamed, new_name)
#
#
