import sys

donors = [
    ['John Lennon', 100.00, 50.00, 586.78],
    ['Paul McCartney', 200.00, 150.00],
    ['Ringo Starr', 1.00],
    ['George Harrison', 1000.00, 500.00, 1586.78],
    ['Yoko Ono', 275.50, 5.00]
]


def get_donor_list():
    donor_list = []
    for donor in donors:
        donor_list.append(donor[0])
    return donor_list


def select_command():
    command = input("""Commands:
Enter 'Thank you' to send a thank you message.
Enter 'Report' to create a report.
Enter 'Home' to return to this screen.
Enter 'Quit' to exit My Donation Manager.""")
    while command.lower() == 'thank you':
        command = write_email()
    while command.lower() == 'report':
        command = create_report()
    while command.lower() == 'quit':
        command = sys.exit()
    return command


def prompt_user(prompt):
    command = input(prompt)
    while command.lower() == 'home':
        command = select_command()
    return command


def write_email():
    global donors

    full_name = prompt_user("Enter the donor's full name or type 'list' to see all donors.")

    while full_name == 'list':
        for donor in donors:
            print(donor[0])
        full_name = prompt_user("Enter the donor's full name or type 'list' to see all donors.")

    donation_amount = prompt_user('Enter the donation amount.')

    while donation_amount:
        try:
            donation_amount = float(donation_amount)
            break
        except:
            donation_amount = prompt_user('Please enter a numeric value.')

    new_donor = True
    for donor in donors:
        if full_name == donor[0]:
            new_donor = False
            donor.append(donation_amount)

    if new_donor:
        donors.append([full_name, donation_amount])

    thank_you = """Dear {},

    Thank you for your generous donation of ${}. You're
    the best!

    Sincerely,

    Your favorite charity """.format(full_name, donation_amount)

    print(thank_you)
    return select_command()


def create_report():
    global donors

    print('Donor\t\t\tTotal\t\tNumber\t\tAverage')
    for donor in donors:
        total_donation = sum(donor[1:])
        number_of_donations = len(donor[1:])
        average_donation = total_donation/number_of_donations
        print('{}\t\t{:.2f}\t\t{:d}\t\t{:.2f}'.format(donor[0], total_donation, number_of_donations, average_donation))
    return select_command()

if __name__ == '__main__':
    command = select_command()
