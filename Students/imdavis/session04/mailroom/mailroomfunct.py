#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

from textwrap import dedent
import math

"""
    A set of functions which support the mailroom main program.
    Do:
        >>> print functname.__doc__
    for the docstring for each.

"""

def prompt1():
    """
    This function will prompt the user for one of the available actions:
    'send a thank you', 'create a report', or 'exit'. It will keep looping
    through until one of those options (or it's shortcut) is given.
    """
    request = None
    action1 = "send a thank you"
    action2 = "create a report"
    action3 = "exit"
    while ( (request != action1) and (request != action2) and (request != action3) ):
        orig_request = raw_input("'(S)end a thank you', '(C)reate a report', or '(E)xit' ?> ")
        # let us only deal with lower case versions of the actions to minimize testing.
        request = orig_request.lower()
        if(request == "s" or request == action1):
            print "Ok, let's", action1
            return action1
        elif(request == 'c' or request == action2):
            print "Ok, let's", action2
            return action2
        elif(request == 'e' or request == action3):
            print "Exiting"
            return action3
        else:
            # if the user doesn't enter an available action, let them know where they went astray.
            print "You entered: '", orig_request, "'"
            print "Please enter '(S)end a thank you' or '(C)reate a report', or '(E)xit'."

# def finddonorindex(donors, adonor):
#     """
#     This function takes the list of donors and the 'adonor' string, which is either an existing 
#     donor name or a new one. If 'adonor' is an existing donor name, return the index of that 
#     donor in our data structure. If the name doesn't exist in our list, add the name to the list of
#     donors (along with an empty list to populate with donations) and return the index of the new
#     entry.
#     """
#     indexcount = 0
#     for name, donations in donors:
#         if name == adonor:
#             return indexcount
#         indexcount += 1
#     print "Requested donor :'", adonor, "' not found in existing list."
#     print "Adding donor :'", adonor, "' to the list..."
#     donors.append((adonor, []))
#     return indexcount

def whichdonor(donors):
    """
    This function will prompt the user if they want a print out of the existing user list and if so,
    print it, or return the index of a given donor.

    This makes use of the 'finddonorindex' function above.
    """
    action1 = "list donor"
    donor = ""
    request = action1
    while ( request == action1 ):
        request = raw_input("Enter an existing donor name or select '(l)ist donor' to see a list of donors > ")
        if(request.lower() == "l" or request.lower() == action1):
            print "The existing donors are:"
            for name,donations in donors.items():
                print name
            request = action1
        elif(request in donors):
            donor = request
        else:
            print "Requested donor :'%s' not found in existing list."%request
            print "Adding donor :'%s' to the list..."%request
            donor = request
            donors.update({ donor : [] })
    return donor

def newdonation(donorname):
    """
    This function check that the new amount entered for a donor is a valid float.
    If so, it returns the amount, if not, it tells you so and asks again.

    This makes use of the 'is_number' function above.
    """
    message = "Enter a new donaton amount for donor '" + donorname + "' > "
    while (True):
        amount = raw_input(message)
        try:
            return float(amount)
        except ValueError:
            print "You entered: '%s' which is not a valid donation amount."%amount

def composemail(donorname, recentdonation):
    """ 
    Compose a message to the donor thanking them and rounding the donation amount to the penny.
    Uses string formatting.
    """
    message = dedent('''
        Dear {donor},

        Thank you very much for your most recent donation of ${donation:.2f}
        Please consider donating to our charity again in the future.

        Sincerely,
        Ian Davis

        '''.format(donor=donorname, donation=recentdonation))
    print message

    # write the message to a file also
    filename = donorname+"-mail.txt"
    try:
        mailfile = open(filename, 'w')
        mailfile.write(message)
        mailfile.close()
    except IOError:
        print "Sorry...couldn't open %s"%filename

def formattable(donor, total, ndonations, ave):
    print"{:^20}{:^20}{:^20}{:^20}".format(donor, total, ndonations, ave)

def print_donor_row(donorname, donationlist):
    """
    Simple function that gets passed the donor name and list of donations for that donor,
    and computes the total donation amount, the average donation, and prints a table.
    """
    total_donated = sum(donationlist)
    ave_donation = total_donated/len(donationlist)
    formattable(donorname, total_donated, len(donationlist), ave_donation)
