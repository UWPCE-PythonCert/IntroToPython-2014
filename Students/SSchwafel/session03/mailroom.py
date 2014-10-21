#!/usr/bin/python


donors = [('bruce wayne',[100000]), ('clark kent',[50000]), ('barry allen',[100]), ('diana prince',[1300]), ('wally west',[10034]),('hal jordan',[10000])] 

def send_a_thank_you(x):

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

        elif full_name == 'list': 
            print donors

        elif full_name == '': 
            print 'It looks like you entered an empty value'
        elif full_name == 'back': 
            break            
        else: 

            query_add_donor = raw_input("It doesn't look like that donor exists in the database yet, would you like to add this person? \n\n(yes/no)\n\n")

            if query_add_donor.lower() == 'yes':
                donors.append(add_donor())
                break
            elif query_add_donor.lower() == 'no':
                break
            else:
                break




def add_donor():

    donor_name = raw_input("Please enter the donor's full name ")
    donor_name = donor_name.lower()

    new_donor_initial_donation = raw_input("What was this donor's initial contribution? ")
    new_donor_initial_donation = int(new_donor_initial_donation)

    return (donor_name,[new_donor_initial_donation])



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

    while x > 1:

        new_donation = raw_input("What is the latest donation amount from this donor? (you will be re-promted if you don't use an integer value) ")

        if new_donation.isdigit() == True:
            break

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

def send_email(x): 
    #x = the list element of our donor

    donation = donation_amount(x, donors)

    print "Hello %s,\n it looks like in the past you donated %i" %(x, int(sum(donation)))

count = 1
while count > 0:
        
    user_input = raw_input(


"""Welcome to the Schuyler Inc. Mail Room App

What would you like to do? 

(A) Send a Thank You

or 

(B) Create a Report

(C) Exit the Mail Room App

""")

    if user_input.upper() == 'A':

        print send_a_thank_you(donors)
        #donors.append(add_donor())
        print donors

    elif user_input == 'B':

        print ''

    #    print 'I'm going to fix this later'

    elif user_input == 'BB':

       donor_name = raw_input('To which donor would you like to send an email? ') 
       send_email(donor_name) 


    elif user_input == 'C':

        print 'Exiting...'

