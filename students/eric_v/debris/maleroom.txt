Fred_Flintstone = [1000, 500, 700]
Wilma_Flintstone = [500]
Barney_Rubble = [50]
Betty_Rubble = [2000, 1000]
Cary_Granite = [2500, 3000, 5000]
donor_list = ['Fred_Flintstone',len(Fred_Flintstone),Fred_Flintstone,'Wilma_Flintstone',len(Wilma_Flintstone),
Wilma_Flintstone,'Barney_Rubble',len(Barney_Rubble),Barney_Rubble,'Betty_Rubble',len(Betty_Rubble),
Betty_Rubble,'Cary_Granite',len(Cary_Granite),Cary_Granite]
# ann magrock, perry masonry,
if ('Wilma_Flintstone') in donor_list:
    donor_index = donor_list.index('Wilma_Flintstone')
    print (donor_index, donor_list)
else:
    print('nada')

def thankYou():
    name = input("Enter the full name of the recipient: ")
    return

def Greeting():
    print("Greetings",'\n',"Would you like to send a thank you or create a report?",'\n')
    print("Enter 1 to create a report or 2 to generate a thank you",'\n')
    response = int(input())
    print('value = ', response)
    type(response)
    if response == 1:
        #generate_report()
        return
    elif response == 2:
        #generate_thank_you()
        return
    else:
        print ("invalid input.  exiting program")
        return

def generate_report():
    print("Enter full name (first and last) of donor")
    donor_name = str(input())
    split_donor_name = donor_name.split()
    donor_firstName, donorlastName = split_donor_name[0],split_donor_name[1]
    #print(donor_firstName,'\n',donorlastName)
    s = "_";
    seq = (donor_firstName, donorlastName); # Make a list of donor name.
    donor_name_concat = s.join( seq)
    print(donor_name_concat)



#ValueError: '3' is not in list
#In [135]: foo = [1,2,3]

#In [136]: foo[0]
#Out[136]: 1

#In [137]: foo[0]='a'

#In [138]: foo
#Out[138]: ['a', 2, 3]

#In [139]: loc = foo.index('a')

#In [140]: print(loc)
#0

#In [141]: loc = foo.index('3')
#In [142]: loc = foo.index(3)

#In [143]: print(loc)
#2