"""
Mailroom 4.1
Create a better mailroom using dictionaries and exceptions

Some help is needed at around line 82 where printing the report
takes place.  This section of code seems inefficient and chunky.

"""

donors = ['Anne Askew',
          'Joan Bocher',
          'Jeremy Clarkson',
          'Matthew Hamont',
          'James May',
          'George van Paris']

donations = [[87.50, 100, 200],
             [25, 43.27],
             [10.03],
             [1000, 250, 5],
             [30, 75],
             [25, 35, 45]]

client_list = dict(zip(donors, donations))

# mailroom looping

from mailfuncs import \
    donation_func, print_thanks, print_intro, input_sanitize

from numpy import average

bored = True
print 'Welcome to the Mailroom timesaver!'

while bored:
    print_intro()
    report_opt = input_sanitize(raw_input('Please enter your choice: '))

    # sending a thank you
    if not report_opt:
        usr_name = raw_input('Please enter a name, m for menu,\
 or "list" for a list of donors: ')

        if usr_name == 'm':  # go back to menu
            continue

        if usr_name == 'list':
            temp = client_list.keys()
            temp.sort()  # sorting a list of keys, is there a better way?

            print '\n'
            for p in temp:
                print p
            print '\n'

            del temp
            continue

        else:
            if usr_name in client_list:
                new_val = donation_func()
                temp = client_list.get(usr_name)
                temp.append(new_val)
                client_list.update({usr_name: temp})
                del temp  # try to be tidy with vars
            else:
                new_val = donation_func()
                client_list.setdefault(usr_name, [new_val])

        print_thanks(usr_name, new_val)

    elif report_opt == 1:
        # print a report of all donors and donations

        templist = []
        # tempdict = dict()
        for person, l in client_list.iteritems():
            tempnum = len(l)
            tempsum = sum(l)
            tempavg = average(l)

            # tempdict.update({person: [tempnum, tempsum, tempavg]})

            templist.append((person, tempnum, tempsum, tempavg))

        templist = sorted(templist, key=lambda x: x[2], reverse=True)

        print '{: <20} {a: >10} {b: >10} {c: >10}'\
                .format('', a='Num', b='Sum', c='Avg')
        for t in templist:
            print '{name: ^20} {a: >10d} {b: >10.2f} {c: >10.2f}'\
                    .format(name=t[0], a=t[1], b=t[2], c=t[3])
        print '\n'

    elif report_opt == 2:
        bored = False

    else:
        print \
            "\nSorry, that isn't an option, please choose from 0 to 2.\n"
