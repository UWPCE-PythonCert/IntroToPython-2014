#!/usr/bin/python


donors = [('bruce wayne',[100000]), ('clark kent',[50000]), ('barry allen',[100]), ('diana prince',[1300]), ('wally west',[10034]),('hal jordan',[10000])] 

def send_a_thank_you(x):

    """Displays a list of all the donations a user has contributed"""

    full_name = ''

    while full_name.isdigit() == False :

        full_name = raw_input("Please enter the full name of your donor:\n\n")
        full_name = full_name.lower()
        
        if is_name_present(full_name, donors) == True:

            print 'It looks like in the past, ' + full_name.title() + ' donated: $' + str(donation_amount(full_name,donors)).strip("[]")

            query_new_donation = raw_input('Would you like to add a new donation for this donor? \n\n(yes/no)\n\n')

            if query_new_donation.lower() == 'yes':

                add_donation(full_name)

            elif query_new_donation.lower() == 'no':

                a = raw_input('Would you like to send a Thank You note?\n\n(yes/no)\n\n')

                if a.lower() == 'yes':

                    send_email(full_name)
                    break
                else:
                    break

        elif full_name == 'list': 
            print donors
        
        elif full_name == '': 
            print 'It looks like you entered an empty value'
        elif full_name == 'back': 
            break            
        else: 

            print "\n(You can enter 'back' to return to the previous prompt)\n"

            query_add_donor = raw_input("It doesn't look like that donor exists in the database yet, would you like to add this person? \n\n(yes/no)\n\n")

            if query_add_donor.lower() == 'yes':
                donors.append(add_donor(full_name))
                break

            elif query_add_donor.lower() == 'no':
                break
            else:
                break


def create_a_report():

    temp_list = []

    sorted_donors = sorted(donors, key=lambda tup: tup[1])

    for i in sorted_donors:

        for x in i[1]:

            #donor_name = i[0]
            #sorting_key = i[1]

            total_amount_of_donations = (sum(i[1])/len(i[1]))

            temp_list.append((i[0],len(i[1]),i[1]))
            
            #temp_list.append(str())


    #sorted_donors = '\n'.join(map(str, sorted_donors))

    #temp_list = '\n'.join(map(str, temp_list))

    for i in temp_list:

        print '%s %s %s' % (i[0],i[1],i[2])

    print temp_list 

    #sorted_donors =  str(sorted_donors)

    #return "  Donor        Donations\n\n%s\n\n" % (sorted_donors)



def add_donor(x):
    """Prompts for donor's name, the initial donation amount, then adds them as (x,[y])"""
    #donor_name = raw_input("Please enter the donor's full name ")
    donor_name = x
    donor_name = donor_name.lower()

    new_donor_initial_donation = raw_input("What was this donor's initial contribution? ")
    new_donor_initial_donation = int(new_donor_initial_donation)

    return (donor_name,[new_donor_initial_donation])



def is_name_present(x,y):
    """Checks to see if x is present in y. Must iterate to check nested tuples"""
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
    """Adds donation to nested list associated with donor"""

    new_donation = raw_input("What is the latest donation amount from this donor? ")

    if new_donation.isdigit() == True:
        return 'Please try again with an int'        

    new_donation = int(new_donation)

    for i in donors:
        
        if i == i[0]:
            i[1].append(new_donation)
    return 

def send_email(x): 
    """Sends prints a message to standard out thanking the user for their donation and summing their donation history. """
    #x = the list element of our donor

    donation = donation_amount(x, donors)

    print "\n\n\nHello %s,\n\nIt looks like in the past you donated $%i to our organization!\n\nThank you for your contribution, it's people like you who are making a difference.\n\nThank You,\n\nSchuyler INC. Staff\n\n\n" %(x.title(), int(sum(donation)))

count = 1
while count > 0:
    #count must be present so list will run until it breaks 
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

    elif user_input.upper() == 'B':

        print create_a_report()

    #    print 'I'm going to fix this later'

    elif user_input.upper() == 'BB':

       donor_name = raw_input('To which donor would you like to send an email? ') 
       send_email(donor_name) 


    elif user_input.upper() == 'C' or 'Q':

        print 'Exiting...'
        break
