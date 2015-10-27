# This script should be executable. The script should accomplish the following goals:

# 1. It should have a data structure that holds a list of your donors and a
# history of the amounts they have donated. This structure should be populated
# at first with at least five donors, with between 1 and 3 donations each

# 2. The script should prompt the user (you) to choose from a menu of 2
# actions: ‘Send a Thank You’ or ‘Create a Report’.

# if __name__ == "__main__":

# -- DATA --


donors = [
    ["Carol Danvers", 25.00, 100.00],
    ["Kumala Khan", 15.00, 15.00, 25.00],
    ["Jennifer Walters", 50.00, 100.00, 65.00],
    ["Monica Rambeau", 200.00],
    ["Jessica Drew", 45.00, 30.00, 70.00]
    ]


def intro():
    print("\nMAILROOM OPTIONS")
    print("1 - Send a Thank You")
    print("2 - Create a Report")
    print("\n(Type 'exit' at any time.)\n")


def mailroom():
    intro()
    while True:
        choice = input("What would you like to do? ")
        if choice == "1":
            print("\nSend a Thank You:\n")
            thanks()
#         elif choice == "2":
#             report()
        elif choice.lower() == "exit":
            print("\nGoodbye.")
            break
#        else:
#            print("\nThat choice isn't on the list.\n")



# Sending a Thank You
def thanks():
    donor_name = get_name()
    if donor_name is not "exit":
        donation = get_amount(donor_name)
    else: 
        donation = 0
    if donation is not 0:
        write_letter(donor_name, donation)
    else:
        print("Returning to main menu.\n")
        intro()

def get_name():
    while True:
        # If the user (you) selects ‘Send a Thank You’, prompt for a Full Name.
        donor_name = input("Please enter the full name of the donor you wish to thank. (Type 'list' for a list of donors.) ")
        if donor_name.lower == "exit":
            break
        # If the user types ‘list’, show them a list of the donor names and re-prompt
        elif donor_name.lower() == "list":
            print("The current list of donors is: ")
            for i in donors:
                print(i[0])
        else:
            # If the user types a name in the list, use it.
            count = 0 
            for i in donors:
                if donor_name in i:
                    count += 1
            if count > 0:
                return donor_name
            # If the user types a name not in the list, add that name to the data structure and use it.
            else:
                donors.append([donor_name])
                return donor_name


def get_amount(donor_name):
    new_donation = 0
    while new_donation < 1:
        # Once a name has been selected, prompt for a donation amount.
        new_donation = input("Please enter the dollar amount of the new donation from " + donor_name + ", rounded: $")
        # Verify that the amount is in fact a number, and re-prompt if it isn’t.
        # Once an amount has been given, add that amount to the donation history of the selected user.
        if new_donation.lower() == "exit":
            break
        elif new_donation.isnumeric():
            new_donation = int(new_donation)
            for i in donors:
                if donor_name is i[0]:
                    i.append(new_donation)
                    return new_donation
        else:
            print("You didn't enter a dollar amount.")

# Finally, use string formatting to compose an email thanking the donor for 
# their generous donation. Print the email to the terminal and return to the original prompt.
def write_letter(donor,amount):
    if amount == 0:
        return ("No letter will be written.")
    else:
        charity = "Carter Home for Retired Superheroes"
        signed = "S.A. Carter"
        print("Dear {name}".format(name = donor))
        print("\nThank you so much for your generous donation of ${:d} to the \n{}.".format(amount, charity))
        print("\n{:},".format("Sincerely"))
        print("{}".format(signed))






# Creating a Report
# If the user (you) selected ‘Create a Report’ Print a list of your donors, sorted by total historical donation amount.
# Include Donor Name, total donated, number of donations and average donation amount as values in each row.
# Using string formatting, format the output rows as nicely as possible. The end 
# result should be tabular (values in each column should align with those above and below)
# After printing this report, return to the original prompt.
# At any point, the user should be able to quit their current task and return to the original prompt.
# From the original prompt, the user should be able to quit the script cleanly


