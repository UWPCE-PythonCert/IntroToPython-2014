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


#make standard name format for handling
def name_split(nme):
    fname, lname = nme.split(' ')
    return (lname, fname)


#take a name and check the list, return true where present, else false
def client_check(nme, donors):
    fname, lname = nme.split(' ')
    if (lname, fname) in donors:
        print '{f:s} {l} is a previous donor.'.format(f=fname, l=lname)
        return True
    else:
        print '{f:s} {l} is a not a previous donor.'.format(f=fname, l=lname)
        return False


#function takes no arguments, prompts for value then validates and returns float
def donation_func():
    val_donation = False
    while not val_donation:
        usr_donation = raw_input('Please enter a donation: ')
        try:
            usr_donation = float(usr_donation)
            val_donation = True
        except ValueError:
            print "Sorry, that wasn't a valid donation.\n"
    return usr_donation


#mailroom control looping we will used bored for flow control since that
#was the genesis of this brillian program


bored = True
print 'Welcome to the Mailroom timesaver!'

while bored:
    print 'Please choose an option:\n\
            0: Send a thank you\n\
            1: Create a report\n\
            2: Exit the timesaver\n'

    report_opt = int(raw_input('Please enter your choice: '))

    ## sending a thank you
    if not report_opt:
        usr_name = raw_input('Please enter a name: ')

        #existing name, scan records and insert new donation
        if client_check(usr_name, donors):
            usr_donation = donation_func()

            for person in client_list:
                if name_split(usr_name) in person:  #need to get correct record
                    new_record = (name_split(usr_name), (person[1] + (usr_donation,)))
                    client_list[client_list.index(person)] = new_record

        #new donor, just append the name and donation to the end of the list
        else:
            usr_donation = donation_func()
            new_record = ((name_split(usr_name)), (usr_donation,))
            client_list.append(new_record)

        print "Dear {donor}, \n\n\
                Thank you for choosing to contribute the generous sum\n\
                of ${amount:.2f} to the Midvale School for the Gifted.\n\
                We are confident you will be pleased with what your\n\
                ${amount:.2f} will be used for since we are definitely\n\
                not laundering it in a complex scheme with Mr. Walter White.\n\n\
                All the best,\n\
                MSG\n\n\
                ".format(donor=usr_name, amount=usr_donation)

    elif report_opt == 1:
        pass

    elif report_opt == 2:
        bored = False

    else:
        print "\nSorry, that isn't an option, please choose from 0 to 2.\n"


