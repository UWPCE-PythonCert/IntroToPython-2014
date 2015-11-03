import sys

donors = {
    'John Lennon': [100.00, 50.00, 586.78],
    'Paul McCartney': [200.00, 150.00],
    'Ringo Starr': [1.00],
    'George Harrison': [1000.00, 500.00, 1586.78],
    'Yoko Ono': [275.50, 5.00]
}


# def get_donor_list():
#     donor_list = []
#     for donor in donors:
#         donor_list.append(donor[0])
#     return donor_list


def select_command():
    command = input("""Commands:
Enter 'Thank you' to send a thank you message.
Enter 'Report' to create a report.
Enter 'Home' to return to this screen.
Enter 'Quit' to exit My Donation Manager.""")
    program_running = True
    while program_running:
        if command.lower() == 'thank you':
            command = write_email()
        if command.lower() == 'report':
            command = create_report()
        if command.lower() == 'quit':
            command = sys.exit()
    return command


def prompt_user(prompt):
    command = input(prompt)
    while command.lower() == 'home':
        command = select_command()
    return command


def write_email():
    # global donors

    full_name = prompt_user("Enter the donor's full name or type 'list' to see all donors.")

    while full_name == 'list':
        for donor in donors.keys():
            print(donor)
        full_name = prompt_user("Enter the donor's full name or type 'list' to see all donors.")

    donation_amount = prompt_user('Enter the donation amount.')

    while donation_amount:
        try:
            donation_amount = float(donation_amount)
            break
        except:
            donation_amount = prompt_user('Please enter a numeric value.')

    new_donor = True
    if full_name in donors.keys():
            new_donor = False
            donors[full_name].append(donation_amount)

    if new_donor:
        donors[full_name] = [donation_amount]

    thank_you = """Dear {},

    Thank you for your generous donation of ${}. You're
    the best!

    Sincerely,

    Your favorite charity """.format(full_name, donation_amount)

    print(thank_you)
    return select_command()


def create_report():
    print('Donor\t\t\tTotal\t\tNumber\t\tAverage')
    for donor in donors:
        total_donation = sum(donors[donor])
        number_of_donations = len(donors[donor])
        average_donation = total_donation/number_of_donations
        report = '{}\t\t{:.2f}\t\t{:d}\t\t{:.2f}'.format(donor, total_donation, number_of_donations, average_donation)
        print(report)
    return select_command()

def create_letter_files():


if __name__ == '__main__':
    command = select_command()
