# mailroom program to break the monotony

# this may be a bad idea but we will see
# a list of tuples for donors and donations
client_list = [
    (('Askew', 'Anne'), (87.50, 100, 200)),
    (('Bocher', 'Joan'), (25, 43.27)),
    (('Clarkson', 'Jeremy'), (10.03,)),
    (('Hamont', 'Matthew'), (1000, 250, 5)),
    (('May', 'James'), (30, 75)),
    (('Parris', 'George van'), (25, 35, 45))]

# length of person name for printing


def person_len(person):
    l = 0
    for p in person:
        l += len(p)
    return l


# make a name list and a money list
def list_maker(client_list):
    donors = []
    donations = []
    for person in client_list:
        donors.append(person[0])
        donations.append(person[1])
    return donors, donations

donors, donations = list_maker(client_list)


# make standard name format for handling
def name_split(nme):
    fname, lname = nme.split(' ')
    return (lname, fname)


# take a name and check the list, return true where present, else false
def client_check(nme, donors):
    fname, lname = nme.split(' ')
    if (lname, fname) in donors:
        print '{f} {l} is a previous donor.'.format(f=fname, l=lname)
        return True
    else:
        print '{f} {l} is a not a previous donor.'.format(f=fname, l=lname)
        return False


# function takes no arguments, prompts for value then
        # validates and returns float

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

# test block prior to starting mailroom
if __name__ is '__main__':
    assert person_len(('Archer', 'Sterling')) == 14

    l, f = name_split('Sterling Archer')
    assert l == 'Archer'
    assert f == 'Sterling'

    print 'Initial tests pass.\n'


# mailroom looping we will used bored for flow control since that
# was the genesis of this brilliant program


bored = True
print 'Welcome to the Mailroom timesaver!'

while bored:
    print 'Please choose an option:\n\
            0: Send a thank you\n\
            1: Create a report\n\
            2: Exit the timesaver\n'

    report_opt = int(raw_input('Please enter your choice: '))

    # sending a thank you
    if not report_opt:
        usr_name = raw_input('Please enter a name, m for menu, or "list" for a list of donors: ')

        if usr_name == 'm':
            continue

        if usr_name == 'list':
            print '\n'
            for person in donors:
                print '{first} {last}'.format(last=person[0], first=person[1])
            print '\n'
            continue

        # existing name, scan records and insert new donation
        if client_check(usr_name, donors):
            usr_donation = donation_func()

            for person in client_list:
                # need to get correct record
                if name_split(usr_name) in person:
                    new_record = (name_split(usr_name),
                                  (person[1] + (usr_donation,)))
                    client_list[client_list.index(person)] = new_record

        # new donor, just append the name and donation to the end of the list
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
        # print a report of all donors and donations

        client_list.sort()
        donors, donations = list_maker(client_list)

        # find max name length
        name_length_value = 0
        for d in donors:
            if person_len(d) > name_length_value:
                name_length_value = person_len(d)

        name_length_value += 5   # need to add some space after the name

        print '{0: >{l}}'.format(' ', l=name_length_value),
        print '{a: >8}  {b: >8}  {c: >8}    {d: >8}'\
              .format(a='Num', b='Total', c='Avg', d='Donations')

        for person in donors:
            i = donors.index(person)

            l = len(donations[i])
            avg_d = 0
            tot_d = 0
            d_list = []     # d-listed, hilarious
            c_list = []

            for d in donations[i]:
                avg_d += d / l
                tot_d += d
                d_list.append(d)

                cwidth = 10 - len(str(d))
                c_list.append(cwidth)

            name_str = '{first} {last}'.format(first=person[1], last=person[0])
            print '{name_str: <{l}}'.format(name_str=name_str, l=name_length_value),
            print '{l: >8d}  {tot_d: >8.2f}  {avg_d: >8.2f}  '\
                .format(l=l, tot_d=tot_d, avg_d=avg_d),

            d_list.sort(reverse=True)

            for d in d_list:
                print '{d: >8.2f}'.format(d=d),

            print '\n'

    elif report_opt == 2:
        bored = False

    else:
        print \
            "\nSorry, that isn't an option, please choose from 0 to 2.\n"
