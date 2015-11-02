#This structure should be populated at first with at least five donors
# with between 1 and 3 donations each
donorNames = {
    'Apple White': [30, 10, 20],
    'Raven Queen': [40, 50],
    'Madeline Hatter':[10, 60],
    'Briar Beauty': [90, 70],
    'Darling Charming':[25, 20]
    }

#add more donors
#newAmount['Madeline Hatter'] = 10
#newAmount['Darling Charming'] = 10

#original prompt:
# type 1 for 'Send a Thank You'
tORr = int(input("Select '1' to send a Thank You, '2' to create a report, '3' to exit the program:"))
#if they select 1, prompt for a Full Name
while tORr == 1:
    fullName = input("Please provide donor's full name or if you would like to exit the program, please enter 'break': ")
    #if they type 'list'
    if fullName == 'list':
    #show them a list of the donor names
       print (list(donorNames.keys()))
    #if the amount isn't int, re-prompt it
    elif fullName in donorNames:
        amount =input("Please provide a donation amount:")
        try:
            amount = int(amount)
            donorNames[fullName].append(amount)
            #call string formatting function to compose a thank you email
            print ("Dear " + fullName + ": \n" +"Thank you so much for dontating " + str(amount) + " dollars, we really appreicate your donation.")
        except ValueError:
            amount =input("Please provide an interger for donation amount:")
        #add the amount to the donation history of the selected user
    elif fullName == 'break':
        break
    elif fullName not in donorNames:
        amount =input("Please provide a donation amount:")
        try:
            amount = int(amount)
            donorNames[fullName] = amount
            #call string formatting function to compose a thank you email
            print ("Dear " + fullName + ": \n" +"Thank you so much for dontating " + str(amount) + " dollars, we really appreicate your donation.")
        except ValueError:
            amount =input("Please provide an interger for donation amount:")

        #re-promt for a full name
        #if the user types a name
# type 2 for ' Create a Report'
#sorted by total historical donation amount
if tORr == 2:
    newList = [ ]
    for key, value in donorNames.items():
        newList.append([key, sum(value), len(value), sum(value)/len(value)])
    sorted(newList, key = lambda donor: donor [1])
        #print (sorted(donorNames.items()))

elif tORr ==3:
    print ('The program ended')


'''
x = {'test': (5,6)}
x.keys()
dict_keys(['test'])
sum(x['test'])
11

for key, value in x.items():
    print key, value

for key, value in x.items():
    print(key, sum(value))
'''





