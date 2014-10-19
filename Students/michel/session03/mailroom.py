# -*- coding: utf-8 -*-
"""
Created on Sat Oct 18 15:38:30 2014

@author: Michel
"""

def initList(donorList):
    """
    Initiatilize list of donors with names and respective donation history
    returns pre-populated list with 4 donors and their donation activity
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
        for j in range(len(donorList[i][1])):
            total = total + donorList[i][1][j]
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
    emailBody = emailBody + "$" + str(amount) + "The Team"
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
    
    
def addDonation(donorList, name, amount):
    """
    Add donation amount to list of donations from a given name 
    """
    return
    
    
def addDonorName(donorList, name):
    """
    Add donor name to donorList
    returns updated donorList
    """
    return
    
def sortDonorList(donorList):
    """
    Sorts  donor list by decreasing amount of donations
    returns sorted list of donors
    """
    donorList = sorted(donorList, key=lambda donorList: donorList[2], reverse=True)
    return donorList
    