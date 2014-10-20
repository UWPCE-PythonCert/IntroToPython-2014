#!/usr/bin/python

donors = ['bruce wayne',[100000], 'clark kent',[50000], 'barry allen',['100'], 'diana prince',['1300'], 'wally west',['10034'],'hal jordan',['10000']]

user_input = raw_input(

"""

Welcome to the Schuyler Inc. Mail Room App

What would you like to do? 

Type 'list' if you'd like to see a list of the donors

Type the donor's name if you'd like to add them to the list (if they are already present in the list, they will not be re-added)


""")

user_input = user_input.title()

def historical_amounts(x):
    """Displays a list of all the donations a user has contributed"""
    donations = x.strip 


def show_donors():
    """Returns a list of the donors in organized format"""
    #print '\n'.join(donors)
    for i in donors:
        print i

#def add_donor():
#    
#def donation_amount():
#    
#def send_email(x):
#    
#

#if user_input == 'List':

if user_input == 'List':
   show_donors() 
#elif user_input in donors:
    
