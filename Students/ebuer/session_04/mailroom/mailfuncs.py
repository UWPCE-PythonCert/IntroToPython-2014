"""
@python: 2
functions for mailroom to call
"""


def donation_func():
    """Return float value from prompt

        Syntax: function takes no arguments
    """

    val_donation = False
    while not val_donation:
        usr_donation = raw_input('Please enter a donation: ')
        try:
            usr_donation = float(usr_donation)
            val_donation = True
        except ValueError:
            print "Sorry, that wasn't a valid donation.\n"
    return usr_donation


def print_thanks(p_name, amount):
    print "Dear {donor}, \n\n\
                Thank you for choosing to contribute the generous sum\n\
                of ${amount:,.2f} to the Midvale School for the Gifted.\n\
                We are confident you will be pleased with what your\n\
                ${amount:,.2f} will be used for since we are definitely\n\
                not laundering it in a complex scheme with Mr. Walter White.\n\n\
                All the best,\n\
                MSG\n\n\
                ".format(donor=p_name, amount=amount)


def print_intro():
    print 'Please choose an option:\n\
            0: Send a thank you\n\
            1: Create a report\n\
            2: Exit the timesaver\n'


def input_sanitize(i):
    try:
        return int(i)
    except (NameError, ValueError):
        return 'Invalid'
