# -*- coding: utf-8 -*-
"""
Created on Sat Oct 18 15:38:30 2014

@author: Michel
"""

def initList(donorList):
    """
    Initiatilize list of donors with names and respective donation history
    returns pre-populated list with 5 donors and their donation activity
    donorList is a list of donors with donors names, list of amounts donated
    and the total amount given so far
    """
    Andrew = [['Andrew'], [25, 35, 15], [75]]
    Martha = [['Martha'], [15, 10], [25]]
    Johnny = [['Johnny'], [45, 50, 25], [120]]
    Emma   = [['Emma'  ], [20], [20]]
    George = [['George'], [30, 35], [65]]
    
    donorList = [Andrew, Martha, Johnny, Emma, George]
    
    return donorList
    
    
def updateTotals(donorList):
    """
    Compute and update total amount given by each donor in the donor list
    returns list of donor with updated total donation
    donorList is the list of donors with donations to be updated
    """
    for i in range(len(donorList)):
        total = 0
        for j in (donorList[i][1]):
            total += j
        donorList[i][2][0] = total
    return donorList
    
def thankYouMail(name, amount):
    """
    Write thank you email to donor name for amount given
    returns email body with inserted name and amount in a string
    name is a string with valid name of a donor 
    amount is integer with donation
    """
    emailBody = name + ", we wanted to thank you for your generous donation of "
    emailBody = emailBody + "$" + str(amount) + "\rThank you \rThe Team"
    return emailBody
    
    
def checkName(donorList, name):
    """
    Checks whether a name entered is in the list already 
    returns True if name is found else returns False
    """
    for i in range(len(donorList)):
        if donorList[i][0][0] == name:
            return True
    return False
    

def listDonors(donorList):
    """
    Prints list of all donors in database
    returns None
    """
    for i in range(len(donorList)):
        print donorList[i][0][0]
    return None    

    
def addDonor(donorList, name):
    """
    Add donor name to donorList
    returns updated donorList
    assumes name does not exist already in the list
    name is a string
    """
    newDonor = [[name], [], [0]]
    donorList = donorList.append(newDonor)
    return donorList


def addDonation(donorList, name, amount):
    """
    Add donation amount to list of donations for a given name 
    returns updated donorList
    assumes name already exists in the list
    name is a string and amount is an integer
    """
    for i in range(len(donorList)):
        if donorList[i][0][0] == name:
            donorList[i][1].append(amount)
            updateTotals(donorList)
            break
    return donorList
    
    
def thankYouPath(donorList, choice):
    """
    Handles production of thank you emails to donors
    returns choice of path and donorList
    choice is an interger
    if user wants to exit, returns choice = 3 for quit option
    """
    while choice == 1:
        print 'Enter "list" to get the list of donors'
        print 'Enter "9" to exit this activity'
        name = str(raw_input('Otherwise, please enter a name: '))
        if name == 'list':
            listDonors(donorList)
        elif name == '9':
            choice = 9
            break
        else:
            if not checkName(donorList, name):                
                addDonor(donorList, name)
            while True:
                amount = str(raw_input('Please, enter donation amount as a dollar number (no pennies): '))
                try:
                    amount = int(amount)
                    addDonation(donorList, name, amount)
                    print thankYouMail(name, amount)
                    break
                except:
                    print 'This is not a Dollar number'
    return donorList, choice


def sortDonorList(donorList):
    """
    Sorts  donor list by decreasing amount of donations
    returns sorted list of donors
    """
    donorList = sorted(donorList, key=lambda donorList: donorList[2], reverse=True)
    return donorList
    

def createReport(donorList):
    """
    Computes the number of donations and average donation per donor
    Displays the results of the computations in a report
    returns list of donors
    """
    donorList = sortDonorList(donorList)
    print 'Name', ' ' * 26, 
    print 'Total', ' ' * 5, 
    print 'Donations', ' ' * 7,
    print 'Average'
    print '-' * 69
    for i in range(len(donorList)):
        name = donorList[i][0][0]
        total = str(donorList[i][2][0])
        nbDonation = str(len(donorList[i][1]))
        average = str(round((float(total) / float(nbDonation)),2))
        print name, ' ' * (20-len(donorList[i][0][0])),
        print total.rjust(15),
        print nbDonation.rjust(15),
        print average.rjust(15)
    return donorList


def selectPath():
    """
    Offers user 3 choices: Write a thank you email, create a report, or quit
    returns choice
    choice is an integer between 1-3
    """
    choice = ''
    print 'Please, select an option: '
    print '1- Send a thank you email'
    print '2- Create a donation report'
    print '3- Quit the application'
    while True:
        choice = str(raw_input('Your Selection: '))
        if choice not in ['1','2','3']:
            print 'Please enter 1, 2, or 3'
        else:
            break
    return int(choice)
    
    
if __name__ == '__main__':
    currentList = []
    choice = 0
    currentList = initList(currentList)
    while choice != 3:
        choice = selectPath()
        if choice == 1:
            currentList, choice = thankYouPath(currentList, choice)  
        elif choice == 2:
            currentList = createReport(currentList)
        elif choice == 3:
            print 'Bye!'
            break

        
