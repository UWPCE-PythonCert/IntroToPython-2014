"""
update mailroom from last week to:

Use dicts where appropriate

Write a full set of letters to everyone to individual files on disk

See if you can use a dict to switch between the users selections

Try to use a dict and the .format() method to do the letter as one big 
template – rather than building up a big string in parts.

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
    print("2 - Create a Report")
    print("3 - Write Thank You letters to all donors.")
    print("\n(Type 'exit' at any time.)")


def thanks():
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


def report(report_source):
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
        print("{:>20}{:>20.2f}{:>20.2f}{:>20.2f}".format(donor, total_amount, total_donations, avg_donation))
    print(("{:>20}".format("------------------") * 4) + "\n")

    # Include Donor Name, total donated, number of donations and average donation amount as values in each row.
    # Using string formatting, format the output rows as nicely as possible. The end 
    # result should be tabular (values in each column should align with those above and below)
    # After printing this report, return to the original prompt.
    # At any point, the user should be able to quit their current task and return to the original prompt.
    # From the original prompt, the user should be able to quit the script cleanly


def get_name(donor_list):
    # Get the name of a donor for writing a thank you letter.
    # Adds a new donor to the donor_list if the donor's name is not found.
    while True:
        # If the user (you) selects ‘Send a Thank You’, prompt for a Full Name.
        donor_name = safe_input("\nPlease enter the full name of the \
donor you wish to thank. (Type 'list' for a list of donors.) ")
        if donor_name is None:
            break
        elif donor_name.lower == "exit":
            break
        # If the user types ‘list’, show them a list of the donor names and re-prompt
        elif donor_name.lower() == "list":
            print("The current list of donors is: ")
            for donor_dict in donor_list:
                print(donor_dict["name"])
        else:
            # If the user types a name in the list, use it.
            for donor_dict in donors:
                if donor_dict["name"] == donor_name:
                    return donor_name
            # If the user types a name not in the list, add that name to the data structure and use it.
            else:
                new_dict = {"name": donor_name, "donations": []}
                donor_list.append(new_dict)
                return donor_name


def get_amount(donor, donations):
    # Get the amount of a new donation for a thank you letter.
    # Append a new donation to the list of donations made by an individual in list donationans.
    new_donation = ""
    while type(new_donation) is not float:
        # Once a name has been selected, prompt for a donation amount.
        new_donation = safe_input("Please enter the amount of the new \
donation from " + donor + " to the nearest whole dollar: $")
        # Verify that the amount is in fact a number, and re-prompt if it isn’t.
        # Once an amount has been given, add that amount to the donation history of the selected user.
        if new_donation is None:
            break
        elif new_donation.lower() == "exit":
            break
        elif new_donation.isnumeric():
            new_donation = float(new_donation)
            for donor_dict in donations:
                if donor_dict["name"] == donor:
                    donor_dict["donations"].append(new_donation)
                    return new_donation
        else:
            print("\nYou didn't enter a whole dollar amount.")


# Finally, use string formatting to compose an email thanking the donor for 
# their generous donation. Print the email to the terminal and return to the original prompt.
def write_letter(donor, amount):
    # Write a thank you letter for a charitable contribution. Make sure that "charity" and 
    # "signature" are correct for the organization sending the letter.
    if amount == 0:
        return ("\nNo new donations. No letter will be written.\n")
    elif amount == "exit":
        return ("\nExiting to main menu.")
    else:
        new_letter = print("\nDear {},".format(donor) + "\nThank you \
so much for your generous donation of ${:.2f} to \
the \n{charity}.".format(amount, charity="Carter Home for Retired \
Superheroes") + "\n{closing},".format(closing="Sincerely") +
            "\n{signed}".format(signed="S.A. Carter"))
        return new_letter


def generate_letters(dictionary_of_donors):
    for dictionaries in dictionary_of_donors:
        # for entry in dictionaries:
        donor = dictionaries["name"]
        file_name = donor + "_thanks.txt"
        total_amount = sum(dictionaries["donations"])
        new_letter = ("\nDear {},".format(donor) + "\nThank \
you for your generous donation(s) totaling ${:.2f} to the \
\n{charity}.".format(total_amount, charity="Carter Home for Retired \
Superheroes") + "\n{closing},".format(closing="Sincerely") +
            "\n{signed}".format(signed="S.A. Carter"))
        with open(file_name, "w") as f:
            f.write(new_letter)
            print("Letter written for {}.".format(donor))

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
            print("\nSend a Thank You:\n")
            thanks()
        elif choice == "2":
            print("\nCreate a Report:\n")
            report(donors)
        elif choice == "3":
            generate_letters(donors)
            print("\nYour letters have been saved as text files.")
        else:
            print("\nThat choice isn't on the list.\n")
