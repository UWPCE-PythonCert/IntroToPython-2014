#!/Library/Frameworks/Python.framework/Versions/2.7/bin/python

from textwrap import dedent


def create_donation_list():
    """Build inital list of donors."""
    d_list = [['Salim Hamed', [100, 900, 1500]],
              ['Iris Marlin', [300]],
              ['John Doe', [200, 1904343]],
              ['Terry Smith', [850]],
              ['Bill Williams', [450, 894]],
              ['Richard Sherman', [500, 900, 50000]]]
    return d_list


def inital_prompt():
    """Display inital prompt and return user response."""
    prompt = dedent("""
        Hello, what would you like to do?

        1 <- Send a Thank You Letter
        2 <- Create a Donation Report
        q <- Quit

    """)
    return raw_input(prompt)


def thank_you(donor_list):
    """Prompt for name and add donation amount to history."""

    # prompt user for donor name
    name_prompt = dedent("""
        Enter donor's name.
        ('b' to go back or 'l' for donor list)
    """)
    response = raw_input(name_prompt)

    # remember if donor is in list
    donor_in_list = in_list(response, donor_list)

    # evaluate user responses
    if response.lower() == 'b':
        return

    elif response.lower() == 'l':
        list_doners(donor_list)

    else:
        # ask user for donation amount
        while True:
            amount_prompt = dedent("""
                How much money was donated?
                ('b' to go back)
            """)
            amount = raw_input(amount_prompt)

            # exit function if user wants to go back
            if amount.lower() == 'b':
                return

            # convert entry to float
            try:
                amount = float(amount)
            except ValueError:
                print '\nInvalid Entry!  Please Try Again.'
            else:
                break

        # add donation to history
        if donor_in_list:
            send_mail(response, amount)
            add_existing_donor_to_list(response, amount, donor_list)
            return
        else:
            send_mail(response, amount)
            add_new_donor_to_list(response, amount, donor_list)
            return


def send_mail(name, amount):
    """Print thank you letter for donation."""
    email = dedent("""
        Dear {:s},

        Thank you very much for your generous donation of ${:,.2f}. We
        appreciate your thoughtfullness and we will make sure your donation
        goes to the right cause.

        Kind Regards,
        Donation Team
    """)
    print email.format(name, amount)


def list_doners(d_list):
    """Print the current list of donors."""
    for doner in d_list:
        print doner[0]


def in_list(name, d_list):
    """Return True if donor is in donation list."""
    for item in d_list:
        if str(item[0]).lower() == name.lower():
            return True
    return False


def add_existing_donor_to_list(name, amount, donor_list):
    """Add donation amount to list of historical dontations."""
    for donor, donations in donor_list:
        if donor.lower() == name.lower():
            donations.append(amount)
    return donor_list


def add_new_donor_to_list(name, amount, donor_list):
    """Add new donor and donation amount to list of historical dontations."""
    return donor_list.append([name, [amount]])


def display_report(d_list):
    """Print Donation Report."""
    # create report header
    header = '\n| {:<30s} | {:>21s} |'.format('Donor Name', 'Total Donation')
    border = '=' * 58

    # print header
    print header
    print border

    # print lines
    for name, donations in d_list:
        line = '| {:<30s} | ${:20,.2f} |'.format(name, sum(donations))
        print line

    # print final board below lines
    print border


if __name__ == '__main__':
    # get donation list
    donation_list = create_donation_list()

    while True:
        # capture user response from inital prompt
        response = inital_prompt()

        # exit program if user enters 'q'
        if response.lower() == 'q':
            break
        # send thank you letter
        elif response == '1':
            thank_you(donation_list)
        # create a donation report
        elif response == '2':
            display_report(donation_list)
        else:
            print 'Invalid Entry!  Please Try Again.'
