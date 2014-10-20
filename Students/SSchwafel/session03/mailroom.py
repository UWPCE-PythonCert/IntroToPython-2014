#!/usr/bin/python

donors = ['bruce wayne',[100000], 'clark kent',[50000], 'barry allen',['100'], 'diana prince',['1300'], 'wally west',['10034'],'hal jordan',['10000']]

def historical_amounts(x):

    """Displays a list of all the donations a user has contributed"""

    full_name = ''
    

    while full_name.isdigit() == False :

        full_name = raw_input('Please enter the full name of your donor:\n')

        if full_name in x:
            #figure out if donor is in the donors list
            #if so, print the index AFTER their name (the list of their donations)

            index_number = int(x.index(full_name)) + 1

            print x[index_number]
        elif full_name.lower() == 'list':
            #if name is list, print a list of donors with the amounts they've donated
            for i in donors:
                print i

def show_donors():
    """Returns a list of the donors in organized format"""
    #print '\n'.join(donors)
    for i in donors:
        print i

user_input = raw_input(

"""

Welcome to the Schuyler Inc. Mail Room App

What would you like to do? 

Send a Thank You

or 

Create a Report

""")

user_input = user_input.title()

if user_input == 'Send A Thank You':
    #do something
    print historical_amounts(donors)

#elif user_input == 'Create A Report':
#
#    #do something else
#    print 'I'm going to fix this later'

#else:


#print historical_amounts(donors)

    
#<Unused text>
#
#Type 'list' if you'd like to see a list of the donors
#
#Type the donor's name if you'd like to add them to the list (if they are already present in the list, they will not be re-added)
##
