#Mailroom 




#define the donor list
def donor_List():
        
        JohnGalt = [0]
        sparklyLestat = [10000]
        BiffBezos = [500, 500]
        GilliamWates = [1000000, 1000000, 1000000]
        donors = [JohnGalt, sparklyLestat, BiffBezos, GilliamWates ]
# a function to print the list of donors
def report():
    print(donors)

#generate a Thank You for a donor 
def thank_You():
        name = input("Enter the full name of the recipient, or enter 'list' if you would like to review our list: ")
        if name == 'list' or 'List':
            report()
        elif name not in donors:
            new_Donor = input("Please enter the name of this new donor.")
            new_Amount
            donors.append(name)
        

    
#main function 
def mail_Room(request):
    request = input("You may A) send a Thank You to our donor list or B) view a list of our donors.  What will it be?")

    if request == "A" or "a":
        thank_You()
    else: 
        report()
    
        
        
