#Mailroom 
'''
We have a list of donors and the amounts they have donated. The user will be prompted to enter a donor name or simply generate a list of current donors.  
If the name entered is not on the original list, then the user will enter that name and the amount donated, these values then being appended to the main donor list. 
There is also the option of sending a Thank You email to a particular donor.

'''

donors = { 
          ('John Galt': 0), 
          ('Sparkle Lestat': 10000), 
          ('Hef Bezos': 500, 500), 
          ('Gilliam Wates': 1000000, 1000000, 1000000) 
          }

#   a function to print the list of donors
def report():
    print(donors)

#   create a new donor (to be used if a given name is not already on the list of donors)
def create_New_Donor():
     new_Donor = []
     new_Name = input("Please enter the name of this new donor: ")    
     new_Donor.append(new_Name)
     donors.append(new_Donor)

#   create a function to record a new amount
def New_Amount():
    amount = input("Please enter ", new_Donor , "'s donation in numbers: ")
    if not amount.isnumeric():
        amount = ("Your donation amount was not the proper format.  Please re-enter.")             
    new_Name[0] = amount
    
#   create the Thank You email
def email():
    donor_to_thank = input("Please enter the name of the donor you wish to gush over: ")
    amt_to_gush = input("Now enter the amount you're gushing over: ")
    if create_New_Donor():
        print("Thank you {0} for your generous donation of {1} to our wondeful cause.  Hooray for exemptions.".format(donor_to_thank, amt_to_gush))
    

#   generate a Thank You for a donor 
def thank_You():
    name = input("Enter the full name of the recipient, or enter 'list' if you would like to review our list: ")
    if name == 'list' or 'List':
        report()
    elif donors[0] == name:
        print(name)
    #   append to the donors list if the name is not there by creating a new list and appending it to the original donors list  
    elif name not in donors[0]:
        New_Donor()  
        

#   main function 
def mail_Room():
    request = input("You may A) send a Thank You to our donor list or B) view a list of our donors.  What will it be? ")
    if request == "A" or "a":
        thank_You()
    else: 
        report()
    
        
mail_Room()
