__author__ = 'Ari'

#!/usr/bin/env python
from textwrap import dedent
import math

# In memory representation of the donor database
# using a tuple for each donor
# -- kind of like a record in a database table
donor_db = []
donor_db.append( ("William Gates, III", [653772.32, 12.17]) )
donor_db.append( ("Jeff Bezos", [877.33]) )
donor_db.append( ("Paul Allen", [663.23, 43.87, 1.32]) )
donor_db.append( ("Mark Zuckerberg", [1663.23, 4300.87, 10432.0]) )

def print_donors():
    print "Donor list:\n"
    for donor in donor_db:
       print donor[0]

def find_donor(name):
    """
    find a donor in the donor db
   :param: the name of the donor
   :returns: The donor data structure -- None if not in the donor_db
    """
    for donor in donor_db:
    # do an non-capitalized compare
       if name.strip().lower() == donor[0].lower():
          return donor
    return None

def main_menu_selection():
    """
    Print out the main application menu and then read the user input.
    """
    input = raw_input(dedent('''
    Choose an action:
    1 - Send a Thank You
    2 - Create a Report
    3 - Quit
    > '''))
    return input.strip()

def gen_letter(donor):
    """
    Generate a thank you letter for the donor
    :param: donor tuple
    :returns: string with letter
    """
    return dedent('''
        Dear %s
            Thank you for your very kind donation of %.2f.
            It will be put to very good use.
                Sincerely,
        -The Team
        ''' % (donor[0], donor[1][-1]) )

def send_thank_you():
    """
    Execute the logic to record a donation and generate a thank you message.
    """
    # Read a valid donor to send a thank you from, handling special commands to
    # let the user navigate as defined.
    while True:
        name = raw_input("Enter a donor's name (or list to see all donors or 'menu' to exit)> ").strip()
        if name == "list":
            print_donors()
        elif name == "menu":
            return
        else:
            break
    # Now prompt the user for a donation amount to apply. Since this is also an exit
    # point to the main menu, we want to make sure this is done before mutating the db
    # list object.
    while True:
        amount_str = raw_input("Enter a donation amount (or 'menu' to exit)> ").strip()
        if amount_str == "menu":
            return
    # Make sure amount is a valid amount before leaving the input loop
        amount = float(amount_str)
        if math.isnan(amount) or math.isinf(amount) or round(amount, 2) == 0.00:
            print "error: donation amount is invalid\n"
        else:
            break
    # If this is a new user, ensure that the database has the necessary data structure.
    donor = find_donor(name)
    if donor is None:
        donor = (name, [])
        donor_db.append( donor )
    # Record the donation
    donor[1].append(amount)
    print gen_letter(donor)

def sort_key(item):
    return item[1]

def print_donor_report():
    """
    Generate the report of the donors and amounts donated.
    """
    # First, reduce the raw data into a summary list view
    report_rows = []
    for (name, gifts) in donor_db:
        total_gifts = sum(gifts)
        num_gifts = len(gifts)
        avg_gift = total_gifts / num_gifts
        report_rows.append( (name, total_gifts, num_gifts, avg_gift) )
    #sort the report data
    report_rows.sort(key=sort_key)
    print "%25s | %11s | %9s | %12s"%("Donor Name","Total Given","Num Gifts","Average Gift")
    print "-"*66
    for row in report_rows:
        print "%25s %11.2f %9i %12.2f"%row

if __name__ == "__main__":
    running = True
    while running:
        selection = main_menu_selection()
    if selection is "1":
        send_thank_you()
    elif selection is "2":
        print_donor_report()
    elif selection is "3":
        running = False
    else:
        print "error: menu selection is invalid!"