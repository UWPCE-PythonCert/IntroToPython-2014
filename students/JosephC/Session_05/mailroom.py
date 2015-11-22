#Mailroom 
'''
We have a list of donors and the amounts they have donated. The user will be prompted to enter a donor name or simply generate a list of current donors.  
If the name entered is not on the original list, then the user will enter that name and the amount donated, these values then being appended to the main donor list. 
There is also the option of sending a Thank You email to a particular donor.

'''


#   define the list of donors
donors = { 
          'John Galt': [], 
          'Sparkle Lestat': [10000], 
          'Hef Bezos': [500, 500], 
          'Gilliam Wates': [1000000, 1000000, 1000000] 
          }

name  = input("Please enter a name to search our list of donors, or type 'list' to generate a list of current donors: ")

#    prompt the user to enter a donor name or generate a list
def new_Donor():
    new_name = input("That name is not in our database.  Please enter name: ")
    new_amt = input("Please enter the donations for this donor.")
    donors[new_name] = new_amt

def Prompt():
    if name in donors:
        print(name, donors[name])
    elif name == 'list' or 'List':
        print(donors)
    #elif email_to == 
    if name not in donors and (name  != 'list' and name != 'List'):
        new_Donor()

def Email():
    email_to = input("Want to send an email to a fav donor?  Type their name: ")
    if email_to in donors:
        print("Thank you {} for your generous donation of {}.".format(email_to, donors[email_to]))
     

def Main():
    Prompt() 
    Email()
Main()
