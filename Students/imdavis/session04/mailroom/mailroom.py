#!/usr/bin/env python2.7

from mailroomfunct import prompt1, whichdonor, newdonation, composemail, \
    formattable, print_donor_row

# Hardcoded original group of donors and donation amounts as a dictionary
donors = {}
donors.update({ "Robert Plant" : [15.00, 25.32, 100.50] })
donors.update({ "Sandra Bullock" : [12.50, 2.25] })
donors.update({ "Richard D. James" : [1500.34, 2349.99] })
donors.update({ "Slash" : [1.00, 10.99] })
donors.update({ "Jessica Alba" : [13.49] })

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
        donor = whichdonor(donors)
        # get the donation amount
        donation = newdonation(donor)
        # add the new donation amount to the appropriate donor
        donors[donor].append(donation)
        # update the user of who the donor is and their updated donation history
        print "Donor:", donor
        print "Donation History:", donors[donor]
        # compose the email message thanking the donor for their recent donation
        composemail(donor, donation)
    # create a report block
    elif(todo == "create a report"):
        # print a header for the report table
        formattable("Donor Name", "Total Donations", "Number of Donations", "Average Donation ($)")
        # print each row of the table for each donor
        for donor, donations in donors.items():
            print_donor_row(donor, donations)
