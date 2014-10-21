#!/usr/bin/python

donors = [('bruce wayne',[100000]), ('clark kent',[50000]), ('barry allen',[100]), ('diana prince',[1300]), ('wally west',[10034]),('hal jordan',[10000])] 
def historical_amounts(x):

    """Displays a list of all the donations a user has contributed"""

    full_name = ''

    while full_name.isdigit() == False :

        full_name = raw_input('Please enter the full name of your donor:\n')
        full_name = full_name.lower()
        
        if is_name_present(full_name, donors) == True:

            print 'It looks like in the past, ' + full_name.title() + ' donated: $' + str(donation_amount(full_name,donors)).strip("[]")

            query_new_donation = raw_input('Would you like to add a new donation for this donor? \n\n(yes/no)\n\n')

            if query_new_donation.lower() == 'yes':
                add_donation(full_name)
                print donors
        else: 

            query_add_donor = raw_input("It doesn't look like that donor exists in the database yet, would you like to add this person? \n\n(yes/no)\n\n")

            if query_add_donor.lower() == 'yes':
                add_donor(full_name)
            else:
                full_name = 1




def add_donor():

    donor_name = raw_input("Please enter the donor's full name ")
    donor_name = donor_name.lower()

    new_donor_initial_donation = raw_input("What was this donor's initial contribution? ")
    new_donor_initial_donation = int(new_donor_initial_donation)

    return (donor_name,[new_donor_initial_donation])



#            new_donor = raw_input( "Please enter the donor's first and last name:\n")
#
#            if add_donor.lower() == 'yes':
#
#                new_donation_amount = '' 
#
#                while new_donation_amount.isdigit() == False:
#                    #keeps prompting while until use gives a digit amount
#
#                    
#                    new_donation_amount = str(add_donation())
#                    #new_donation_amount = raw_input('How much did this person donate? (Please use a whole number without commas) ')
#                    donors.append(new_donor)
#                    donors.append([new_donation_amount])
#        
#                print donors
#
#            else:
#                
#                #changes full_name to a digit value, killing the while loop
#                full_name = str(1)
#

def is_name_present(x,y):

    for i in y:

        if x == i[0]:
            return True
        
    return False     
            
def donation_amount(x,y):
    """Queries donation amount for donor x"""
    #x = full_name
    #y = donors

    for i in y:

        if x == i[0]:
            return i[1]
        
def add_donation(x):

    new_donation = raw_input('What is the latest donation amount from this donor? ')
    new_donation = int(new_donation)

    for i in donors:

        if x == i[0]:
            i[1].append(new_donation)

    return i[1]

def show_donors():
    """Returns a list of the donors in organized format"""
    #print '\n'.join(donors)
    for i in donors:
        print i

user_input = raw_input(

"""

Welcome to the Schuyler Inc. Mail Room App

What would you like to do? 

(A) Send a Thank You

or 

(B) Create a Report

""")

user_input = user_input.title()

if user_input.upper() == 'A':

    #print historical_amounts(donors)
    donors.append(add_donor())
    print donors
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
