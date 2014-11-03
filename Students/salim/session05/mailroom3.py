#!/usr/local/bin/python

from textwrap import dedent
import pathlib


def create_donation_list():
    """Build inital list of donors."""
    d_list = {'salim hamed': [100, 900, 1500],
              'iris marlin': [300],
              'john doe': [200, 1904343],
              'terry smith': [850],
              'bill williams': [450, 894],
              'richard sherman': [500, 900, 50000]}
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

    # evaluate user responses
    if response.lower() == 'b':
        return

    elif response.lower() == 'l':
        print list_doners(donor_list)

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

        # send thank you letter
        print send_mail(response, amount)

        # add donation to history
        donor_list.setdefault(response.lower(), []).append(amount)
        return


def send_mail(name, amount):
    """Print thank you letter for donation."""
    # create email pretext
    pretext = dedent("""
        The folowing email has been saved to the "email/" sub directory
        =====================================================================
    """)

    # create email
    email = dedent("""
        Dear {:s},

        Thank you very much for your generous donation of ${:,.2f}. We
        appreciate your thoughtfullness and we will make sure your donation
        goes to the right cause.

        Kind Regards,
        Donation Team
    """)

    # write email to file
    parent_path = pathlib.Path(__file__).parent
    email_file = open(str(parent_path) + '/email/' + name + '.txt', 'w')
    email_file.write(email.format(name, amount))
    email_file.close()

    return (pretext + email).format(name, amount)


def list_doners(d_list):
    """Return print read string with the current list of donors."""
    s = ('\n' + '{}\n' * len(d_list))[:-1]
    return s.format(*d_list.keys()).title()


def display_report(d_list):
    """Print Donation Report."""
    l_report = []

    # create report header and boder
    header = '| {:<30s} | {:>21s} |'.format('Donor Name', 'Total Donation')
    border = '=' * 58

    # create report rows
    s = '| {:<30s} | ${:20,.2f} |'
    rows = [s.format(k.title(), sum(v)) for k, v in d_list.iteritems()]

    # build report list
    l_report.append(header)
    l_report.append(border)
    l_report.extend(rows)
    l_report.append(border)

    return ('\n{}' * len(l_report)).format(*l_report)


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
            print display_report(donation_list)
        else:
            print 'Invalid Entry!  Please Try Again.'
