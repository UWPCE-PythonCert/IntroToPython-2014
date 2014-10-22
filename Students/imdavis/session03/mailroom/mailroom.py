#!/usr/bin/env python2.7

from mailroomfunct import *

# Hardcoded original group of donors and donation amounts
donors = []
donors.append(("Robert Plant", [15.00, 25.32, 100.50]))
donors.append(("Sandra Bullock", [12.50, 2.25]))
donors.append(("Richard D. James", [1500.34, 2349.99]))
donors.append(("Slash", [1.00, 10.99]))
donors.append(("Jessica Alba", [13.49]))

# Initial greeting at startup
print "Welcome to Mailrooom, buddy!"

# Call the prompt function to ask the user what they would like to do
todo = ""
# keep looping with prompts until the user says to exit
while (todo != "exit"):
    # send a thank you block
    todo = prompt1()
    if(todo == "send a thank you"):
        # get the index of existing or new donor
        indexofdonor = donorindex(donors)
        # get the donation amount
        donation = newdonation(donors[indexofdonor][0])
        # add the new donation amount to the appropriate donor
        donors[indexofdonor][1].append(donation)
        # update the user of who the donor is and their updated donation history
        print "Donor:", donors[indexofdonor][0]
        print "Donation History:", donors[indexofdonor][1]
        # compose the email message thanking the donor for their recent donation
        composemail(donors[indexofdonor][0], donors[indexofdonor][1][-1])
    # create a report block
    elif(todo == "create a report"):
        # print a header for the report table
        formattable("Donor Name", "Total Donations", "Number of Donations", "Average Donation ($)")
        # print each row of the table for each donor
        for i in range(len(donors)):
            print_donor_row(donors[i][0], donors[i][1])
