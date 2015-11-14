"""
See if you can use a dict to switch between the users selections

THEN:
Add Exception handling to mailroom
and add some tests
and list (and dict, and set) comprehensions...
"""

donors = [
    {"name": "Carol Danvers", "donations": [25.00, 100.00]},
    {"name": "Kumala Khan", "donations": [15.00, 15.00, 25.00]},
    {"name": "Jennifer Walters", "donations": [50.00, 100.00, 65.00]},
    {"name": "Monica Rambeau", "donations": [200.00]},
    {"name": "Jessica Drew", "donations": [45.00, 30.00, 70.00]}
    ]


def safe_input(message):
    # Prevents error when ctrl-c or ctrl-d are used to stop the script.
    try:
        user_input = input(message)
        return user_input
    except (KeyboardInterrupt, EOFError):
        return None


def intro():
    print("\nMAILROOM OPTIONS")
    print("1 - Send a Thank You")
    print("2 - Create a print_report")
    print("3 - Write Thank You letters to all donors.")
    print("\n(Type 'exit' to quit.)")


def thank_you_letter():
    # Collects information from the user when sending a thank you letter.
    donor_name = get_name(donors)
    if donor_name == "exit":
        return "Returning to main menu.\n"
    donation = get_amount(donor_name, donors)
    if donation == "exit":
        return "Returning to main menu.\n"
    elif donation != 0:
        write_letter(donor_name, donation)
    else:
        print("Returning to main menu.\n")


def print_report(report_source):
    # Print a list of your donor, sorted by total historical donation amount.
    print("{:^80}".format("DONOR REPORT\n"))
    print("{:>20}{:>20}{:>20}{:>20}".format("Donor Name", "Total Amt. \
Donated", "Times Donated", "Avg. Donation"))
    print("{:>20}".format("------------------") * 4)
    for donor_dictionary in report_source:
        donor = donor_dictionary["name"]
        total_amount = sum(donor_dictionary["donations"])
        total_donations = len(donor_dictionary["donations"])
        try:
            avg_donation = total_amount / total_donations
        except ZeroDivisionError as e:
            return e
        print("{:>20}{:>20.2f}{:>20.2f}{:>20.2f}".format(
            donor, total_amount, total_donations, avg_donation))
    print(("{:>20}".format("------------------") * 4) + "\n")


def list_of_donors(donor_list):
    listing = [(donor_dict["name"]) for donor_dict in donor_list]
    return "\n".join(listing)


def get_name(donor_list):
    # Get the name of a donor for writing a thank you letter.
    # Adds a new donor to the donor_list if the donor's name is not found.
    while True:
        donor_name = safe_input("\nPlease enter the full name of the \
donor you wish to thank. (Type 'list' for a list of donors.) ")
        if donor_name is None:
            break
        elif donor_name.lower() == "exit":
            break
        elif donor_name.lower() == "list":
            print("The current list of donors is: ")
            print(list_of_donors(donor_list))
        elif [donor_dict["name"] is donor_name for donor_dict in donors]:
            return donor_name
        else:
            new_dict = {"name": donor_name, "donations": []}
            donor_list.append(new_dict)
            return donor_name


def get_amount(donor, donations):
    # Get the amount of a new donation for a thank you letter.
    # Append a new donation to the list of donations made by an
    # individual in list donationans.
    new_donation = ""
    while type(new_donation) is not float:
        new_donation = safe_input("Please enter the amount of the new \
donation from " + donor + " to the nearest whole dollar: $")
        if new_donation is None:
            break
        elif new_donation.lower() == "exit":
            break
        elif new_donation.isnumeric():
            new_donation = float(new_donation)
            [donor_dict["donations"].append(new_donation)
                for donor_dict in donations if donor_dict["name"] == donor]
            return new_donation
        else:
            print("\nYou didn't enter a whole dollar amount.")


def write_letter(donor, amount):
    # Write a thank you letter for a charitable contribution.
    # Make sure that "charity" and "signature" are correct for the
    # organization sending the letter.
    if amount == 0:
        return ("\nNo new donations. No letter will be written.\n")
    elif amount == "exit":
        return ("\nExiting to main menu.")
    else:
        new_letter = print('''Dear {},
            so much for your generous donation of ${:.2f} to
            {charity}.
            {closing},
            {signed}'''.format(
            donor, amount,
            charity="The Carter Home for Retired Superheroes",
            closing="Sincerely", signed="S.A. Carter"))
        return new_letter


def generate_letters(dictionary_of_donors):
    for dictionaries in dictionary_of_donors:
        file_name = dictionaries["name"] + "_thanks.txt"
        new_letter = ('''Dear {},
            Thank you for your generous donation(s) totaling ${:.2f}
            to {charity}.
            {closing},
            {signed}'''.format(
            donor=dictionaries["name"],
            total_amount=sum(dictionaries["donations"]),
            charity="The Carter Home for Retired Superheroes",
            closing="Sincerely", signed="S.A. Carter"))
        with open(file_name, "w") as f:
            f.write(new_letter)
            print("Letter written for {}.".format(dictionaries["name"]))


if __name__ == "__main__":
    while True:
        intro()
        choice = safe_input("\nWhat would you like to do? ")
        if choice is None:
            break
        elif choice.lower() == "exit":
            print("\nGoodbye.")
            break
        elif choice == "1":
            thank_you_letter()
        elif choice == "2":
            print_report(donors)
        elif choice == "3":
            generate_letters(donors)
            print("\nYour letters have been saved as text files.")
        else:
            print("\nThat choice isn't on the list.\n")
