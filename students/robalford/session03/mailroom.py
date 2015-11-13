donors = {
    'John Lennon': [100.00, 50.00, 586.78],
    'Paul McCartney': [200.00, 150.00],
    'Ringo Starr': [1.00],
    'George Harrison': [1000.00, 500.00, 1586.78],
    'Yoko Ono': [275.50, 5.00]
    }


def list_donors():
    return '\n'.join(donors.keys())


def select_command():
    command = input("""Commands:
Enter 'Thank you' to send a thank you message.
Enter 'Report' to create a report.
Enter 'Save letters' to save a copy of all thank you letters.
Enter 'Quit' to exit My Donation Manager.""")
    return command


def write_email(donor, donation_amount):
    thank_you = """Dear {},

    Thank you for your generous donation of ${}. You're
    the best!

    Sincerely,

    Your favorite charity """.format(donor, donation_amount)

    return thank_you


def add_new_donation(full_name, donation_amount):
    try:
        donors[full_name].append(donation_amount)
    except KeyError:
        donors[full_name] = [donation_amount]


def send_thank_you():
    getting_donor = True
    while getting_donor:
        full_name = input("Enter the donor's full name. Type 'list' to see all donors or 'home' to exit.")
        if full_name.lower() == 'list':
            print(list_donors())
            getting_donor
        elif full_name.lower() == 'home':
            return
        else:
            break

    donation_amount = input("Enter the donation amount. Type 'home' to exit")

    while True:
        if donation_amount.lower() == 'home':
                return
        try:
            donation_amount = float(donation_amount)
        except ValueError:
            donation_amount = input('Please enter a numeric value.')
        else:
            break

    add_new_donation(full_name, donation_amount)

    print(write_email(full_name, donation_amount))


def create_report():
    donor_reports = []
    for donor, donations in donors.items():
        donor_report = (
            donor, sum(donations),
            len(donations),
            sum(donations)/len(donations)
        )
        donor_reports.append(donor_report)
    return donor_reports


def print_report():
    donor_reports = create_report()
    print('Donor\t\t\tTotal\t\tNumber\t\tAverage')
    for report in donor_reports:
        print('{}\t\t{:.2f}\t\t{}\t\t{:.2f}\n'.format(*report))


def create_letter_files():
    for donor in donors:
        total_donation = sum(donors[donor])
        letter = write_email(donor, total_donation)
        with open(donor + '.txt', 'w') as letter_file:
            letter_file.write(letter)
    print("All letter saved to disc.")

if __name__ == '__main__':
    program_running = True
    while program_running:
        command = select_command()
        if command.lower() == 'thank you':
            send_thank_you()
        elif command.lower() == 'report':
            print_report()
        elif command.lower() == 'save letters':
            create_letter_files()
        elif command.lower() == 'quit':
            program_running = False
        else:
            print('Invalid command. Please try again.')
