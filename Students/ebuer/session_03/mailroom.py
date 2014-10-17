#mailroom program to break the monotony

#this may be a bad idea but we will see
#a list of tuples for donors and donations
client_list = [
    (('Askew', 'Anne'), (87.50, 100, 200)),
    (('Bocher', 'Joan'), (25, 43.27)),
    (('Clarkson', 'Jeremy'), (10.03)),
    (('Hamont', 'Matthew'), (1000, 250, 5)),
    (('May', 'James'), (30, 75)),
    (('Parris', 'George van'), (25, 35, 45))]

#make a name list and a money list
def list_maker(client_list):
    donors = []
    donations = []
    for person in client_list:
        donors.append(person[0])
        donations.append(person[1])
    return donors, donations

donors, donations = list_maker(client_list)

#take a name and check the list
def client_check(nme, donors):
    fname, lname = nme.split(' ')
    if (lname, fname) in donors:
        print '{f:s} {l} is a previous donor.'.format(f=fname, l=lname)
        return True
    else:
        print '{f:s} {l} is a not a previous donor.'.format(f=fname, l=lname)
        return False

res=client_check('Anne Askew', donors)


#mailroom control looping
bored = True

while bored:
    print 'Welcome to the Mailroom timesaver! Please choose an option:\n\
            0: Send a thank you\n\
            1: Create a report\n'

    report_opt = int(raw_input('Please enter your choice: '))

    if report_opt == 0 : ## sending a thank you
        usr_name = raw_input('Please enter a name: ')
        
        if client_check(usr_name, donors):
            usr_donation = raw_input('Please enter a donation: ')
        else:
            fname, lname = usr_name.split(' ')
            client_list.append(((lname, fname), (None)))





