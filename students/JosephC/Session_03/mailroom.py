#Mailroom 
'''
We have a list of donors and the amounts they have donated. The user will be prompted to enter a donor name or simply generate a list of current donors.  
If the name entered is not on the original list, then the user will enter that name and the amount donated, these values then being appended to the main donor list. 
There is also the option of sending a Thank You email to a particular donor.

'''
#   define the donor list
def donor_List():
        
        JohnGalt = [0]
        sparklyLestat = [10000]
        BiffBezos = [500, 500]
        GilliamWates = [1000000, 1000000, 1000000]
        donors = [JohnGalt, sparklyLestat, BiffBezos, GilliamWates ]
#   a function to print the list of donors
def report():
    print(donors)
#   create a new donor (to be used if a given name is not already on the list of donors)
def create_New_Donor():
     new_Donor = []
     new_Name = input("Please enter the name of this new donor.")    
     new_Donor.append(new_Name)
     donors.append(new_Donor)

#   create a function to record a new amount
def New_Amount():
    new_Amount = input("Please enter ", new_Donor , "'s donation in numbers.")
    if not new_Amount.isnumeric():
        new_Amount = ("Your donation amount was not the proper format.  Please re-enter.")             
    new_Name[0] = new_Amount
    
#   create the Thank You email
def email():
    if create_New_Donor():
        
    

#   generate a Thank You for a donor 
def thank_You():
    name = input("Enter the full name of the recipient, or enter 'list' if you would like to review our list: ")
    if name == 'list' or 'List':
        report()
    #   append to the donors list if the name is not there by creating a new list and appending it to the original donors list  
    elif name not in donors:
        New_Donor()       

    
#   main function 
def mail_Room():
    request = input("You may A) send a Thank You to our donor list or B) view a list of our donors.  What will it be?")

    if request == "A" or "a":
        thank_You()
    else: 
        report()
    
        
mail_Room()
