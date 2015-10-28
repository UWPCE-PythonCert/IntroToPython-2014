# This script should be executable. The script should accomplish the following goals:

# 1. It should have a data structure that holds a list of your donors and a
# history of the amounts they have donated. This structure should be populated
# at first with at least five donors, with between 1 and 3 donations each

# 2. The script should prompt the user (you) to choose from a menu of 2
# actions: ‘Send a Thank You’ or ‘Create a Report’.

donors = [
    ["Carol Danvers", 25.00, 100.00],
    ["Kumala Khan", 15.00, 15.00, 25.00],
    ["Jennifer Walters", 50.00, 100.00, 65.00],
    ["Monica Rambeau", 200.00],
    ["Jessica Drew", 45.00, 30.00, 70.00]
    ]


def safe_input(message):
    try: 
        input(message)
    except (KeyboardInterrupt, EOFError):
        return None


def intro():
    print("\nMAILROOM OPTIONS")
    print("1 - Send a Thank You")
    print("2 - Create a Report")
    print("\n(Type 'exit' at any time.)\n")


def mailroom():
    intro()
    while True:
        choice = safe_input("What would you like to do? ")
        if choice == "1":
            print("\nSend a Thank You:\n")
            thanks()
        elif choice == "2":
            print("\nCreate a Report:\n")
            report(donors)
        elif choice.lower() == "exit":
            print("\nGoodbye.")
            break
        else:
            print("\nThat choice isn't on the list.\n")
            intro()


# Sending a Thank You
def thanks():
    donor_name = get_name(donors)
    if donor_name == "exit":
        return print("Returning to main menu.\n")
    donation = get_amount(donor_name, donors)
    if donation is not 0:
        write_letter(donor_name, donation)
    else:
        print("Returning to main menu.\n")
        intro()


def report(l):
    # Print a list of your donor, sorted by total historical donation amount.
    print("{:^80}".format("DONOR REPORT\n"))
    print("{:>20}{:>20}{:>20}{:>20}".format("Donor Name", "Total Amt. Donated", "Times Donated", "Avg. Donation"))
    print("{:>20}".format("------------------") * 4)
    for i in l:
        donor = i[0].title()
        total_amount = sum(i[1:])
        total_donations = (len(i)-1)
        avg_donation = total_amount / total_donations
        print("{:>20}{:>20.2f}{:>20.2f}{:>20.2f}".format(donor, total_amount, total_donations, avg_donation))
    print(("{:>20}".format("------------------") * 4) + "\n")
    intro()

    # Include Donor Name, total donated, number of donations and average donation amount as values in each row.
    # Using string formatting, format the output rows as nicely as possible. The end 
    # result should be tabular (values in each column should align with those above and below)
    # After printing this report, return to the original prompt.
    # At any point, the user should be able to quit their current task and return to the original prompt.
    # From the original prompt, the user should be able to quit the script cleanly


def get_name(l):
    # Get the name of a donor for writing a thank you letter.
    # Adds a new donor list to the list l if the donor's name is not found.
    while True:
        # If the user (you) selects ‘Send a Thank You’, prompt for a Full Name.
        donor_name = input("Please enter the full name of the donor you wish to thank. (Type 'list' for a list of donors.) ")
        if donor_name.lower == "exit":
            break
        # If the user types ‘list’, show them a list of the donor names and re-prompt
        elif donor_name.lower() == "list":
            print("The current list of donors is: ")
            for i in l:
                print(i[0])
        else:
            # If the user types a name in the list, use it.
            count = 0
            for i in l:
                if donor_name in i:
                    count += 1
            if count > 0:
                return donor_name
            # If the user types a name not in the list, add that name to the data structure and use it.
            else:
                l.append([donor_name])
                return donor_name


def get_amount(donor, l):
    # Get the amount of a new donation for a thank you letter.
    # Append a new donation to the list of donations made by an individual in list l.
    new_donation = 0
    while new_donation < 1:
        # Once a name has been selected, prompt for a donation amount.
        new_donation = input("Please enter the amount of the new donation from " + donor + " to the nearest whole dollar: $")
        # Verify that the amount is in fact a number, and re-prompt if it isn’t.
        # Once an amount has been given, add that amount to the donation history of the selected user.
        if new_donation.lower() == "exit":
            break
        elif new_donation.isnumeric():
            new_donation = float(new_donation)
            for i in l:
                if donor is i[0]:
                    i.append(new_donation)
                    return new_donation
        else:
            print("You didn't enter a dollar amount.")


# Finally, use string formatting to compose an email thanking the donor for 
# their generous donation. Print the email to the terminal and return to the original prompt.
def write_letter(donor,amount):
    # Write a thank you letter for a charitable contribution. Make sure that "charity" and 
    # "signature" are correct for the organization sending the letter.
    if amount == 0:
        return ("\nNo new donations. No letter will be written.\n")
    else:
        charity = "Carter Home for Retired Superheroes"
        closing = "Sincerely"
        signed = "S.A. Carter"
        print("\nDear {},".format(donor))
        print("\nThank you so much for your generous donation of ${:.2f} to the \n{}.".format(amount, charity))
        print("\n{:},".format(closing))
        print("{}\n".format(signed))


if __name__ == "__main__":
    mailroom()