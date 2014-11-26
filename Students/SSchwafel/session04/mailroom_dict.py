#!/usr/bin/python

donors = {
'bruce wayne':[100000],
'clark kent':[50000],
'barry allen':[100],
'diana prince':[1300],
'wally west':[10034],
'hal jordan':[10000]
} 


def send_a_thank_you(x):

    """Displays a list of all the donations a user has contributed"""

    full_name = ''

    while True:

        full_name = raw_input("Please enter the full name of your donor (you can type 'back' to return to the previous prompt):\n\n")
        full_name = full_name.lower()
    

        if is_name_present(full_name) == True:

            print 'It looks like in the past, ' + full_name.title() + ' donated: $' + str(donors[full_name]).strip("[]")

            query_new_donation = raw_input('Would you like to add a new donation for this donor? \n\n(yes/no)\n\n')

            if query_new_donation.lower() == 'yes':

                add_donation(full_name)

            elif query_new_donation.lower() == 'no':

                    a = raw_input('Would you like to send a Thank You note?\n\n(yes/no)\n\n')

                    if a.lower() == 'yes':

                        print send_email(full_name)
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

                add_donor(full_name)

            elif query_add_donor.lower() == 'no':
                break
            else:
                break

def create_a_report():
    """Creates a structured output of all donors and donations"""
    sorted_donors = []
    temp_list = []

    for i in donors:
        
        each_index = (i,donors[i])
        temp_list.append(each_index)

    sorted_donors = sorted(temp_list, key=lambda tup: tup[1])

    print '\n{:<12}{:^12}{:>12}'.format('Donor Name','Donations','Total Donations')

    for i in sorted_donors:

        total_amount_of_donations = (sum(i[1])/len(i[1]))

        temp_list.append((i[0],len(i[1]),i[1]))
            
        print '\n{:<12}{:^12}{:>12}'.format(i[0],len(i[1]),sum(i[1]))

def add_donor(x):
    """Prompts for donor's name, the initial donation amount, then adds them as (x,[y])"""
    donor_name = x
    donor_name = donor_name.lower()

    new_donor_initial_donation = raw_input("What was this donor's initial contribution? ")

    try:
	new_donor_initial_donation = int(new_donor_initial_donation)
	donors[x] = [new_donor_initial_donation]

    except ValueError:
	print "\nPlease try again with an int."

def is_name_present(x):
    """Checks to see if x is present in y. Must iterate to check nested tuples"""
    if x in donors.keys():
        return True
    else:

        return False     
            
def donation_amount(x):
    """Queries donation amount for donor x"""
    #x = full_name
    #y = donors

    return donors[x]    
def add_donation(x):
    """Adds donation to list associated with donor"""

    new_donation = raw_input("What is the latest donation amount from this donor? ")

    try:

        new_donation = int(new_donation)

        donors[x].append(new_donation)
        print donors[x]

    except ValueError:
	print "\nPlease try again with an int."


#    for i in y:
#        
#        for item in i:
#            if x == item:
#                print '\n\n' + "Adding a donation of " + str(new_donation) + " to the record for " + str(x).title() + '\n\n'
#                i[1].append(new_donation)
#        print i
#        #if x == i[0]:
#        #    return i[1].append(new_donation)
    return 

def send_email(x): 
    """Sends prints a message to standard out thanking the user for their donation and summing their donation history. """
    #x = the list element of our donor

    donation = donation_amount(x)

    return "\n\n\nHello %s,\n\nIt looks like in the past you donated $%i to our organization!\n\nThank you for your contribution, it's people like you who are making a difference.\n\nThank You,\n\nSchuyler INC. Staff\n\n\n" %(x.title(), int(sum(donors[x])))


count = 1
while count > 0:
    #count must be present so list will run until it breaks 
    user_input = raw_input(


"""Welcome to the Schuyler Inc. Mail Room App

What would you like to do? 

(A) Send a Thank You

or 

(B) Create a Report

(C) Print a letter for everyone in the database

(D) Exit the Mail Room App

""")

    if user_input.upper() == 'A':

        print send_a_thank_you(donors)
        print donors

    elif user_input.upper() == 'B':

        print create_a_report()

    elif user_input.upper() == 'C':

        for i in donors:

            outfile = open('%s.txt'%i.replace(' ',''),'w' )

            print i

            outfile.write(send_email(i))
    
    elif user_input.upper() == 'D' or 'Q':

        print 'Exiting...'
        break
