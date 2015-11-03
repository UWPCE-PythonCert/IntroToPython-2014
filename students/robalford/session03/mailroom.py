donors = {
    'John Lennon': [100.00, 50.00, 586.78],
    'Paul McCartney': [200.00, 150.00],
    'Ringo Starr': [1.00],
    'George Harrison': [1000.00, 500.00, 1586.78],
    'Yoko Ono': [275.50, 5.00]
}


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


def send_thank_you():
    full_name = input("Enter the donor's full name. Type 'list' to see all donors or 'home' to exit.")
    while True:
        if full_name.lower() == 'list':
            for donor in donors.keys():
                print(donor)
                break
        elif full_name.lower() == 'home':
            return
        else:
            break

    while True:
        donation_amount = input("Enter the donation amount. Type 'home' to exit")
        if donation_amount.lower() == 'home':
            return
        try:
            donation_amount = float(donation_amount)
        except:
            donation_amount = input('Please enter a numeric value.')
        else:
            break

    new_donor = True
    if full_name in donors.keys():
            new_donor = False
            donors[full_name].append(donation_amount)

    if new_donor:
        donors[full_name] = [donation_amount]

    print(write_email(full_name, donation_amount))


def create_report():
    print('Donor\t\t\tTotal\t\tNumber\t\tAverage')
    for donor in donors:
        total_donation = sum(donors[donor])
        number_of_donations = len(donors[donor])
        average_donation = total_donation/number_of_donations
        report = '{}\t\t{:.2f}\t\t{:d}\t\t{:.2f}'.format(donor, total_donation, number_of_donations, average_donation)
        print(report)


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
            create_report()
        elif command.lower() == 'save letters':
            create_letter_files()
        elif command.lower() == 'quit':
            program_running = False
        else:
            print('Invalid command. Please try again.')
