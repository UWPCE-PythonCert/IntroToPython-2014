# This script should be executable. The script should accomplish the following goals:

# 1. It should have a data structure that holds a list of your donors and a
# history of the amounts they have donated. This structure should be populated
# at first with at least five donors, with between 1 and 3 donations each

# 2. The script should prompt the user (you) to choose from a menu of 2
# actions: ‘Send a Thank You’ or ‘Create a Report’.

# if __name__ == "__main__":

# -- DATA --


donors = [
    ["Carol Danvers", 25, 100],
    ["Kumala Khan", 15, 15, 25],
    ["Jennifer Walters", 50, 100, 65],
    ["Monica Rambeau", 200],
    ["Jessica Drew", 45, 30, 70]
    ]


def intro():
    print("\tMAILROOM OPTIONS")
    print("\t1 - Send a Thank You")
    print("\t2 - Create a Report")
    print("\n\t(Type 'exit' at any time to quit.")


def mailroom():
    while True:
        choice = input("What would you like to do? ")
        if choice == 1:
            thanks()


# Sending a Thank You
def thanks():
    get_name()


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
            pass
        # If the user types a name not in the list, add that name to the data structure and use it.
        elif donor_name.lower() not in donors:
            donors.append([donor_name])
            return donor_name
        # If the user types a name in the list, use it.
        else: 
            assert donor_name in donors
            return donor_name


# Once a name has been selected, prompt for a donation amount.
# Verify that the amount is in fact a number, and re-prompt if it isn’t.
# Once an amount has been given, add that amount to the donation history of the selected user.
# Finally, use string formatting to compose an email thanking the donor for 
# their generous donation. Print the email to the terminal and return to the original prompt.
# It is fine to forget new donors once the script quits running.





# Creating a Report
# If the user (you) selected ‘Create a Report’ Print a list of your donors, sorted by total historical donation amount.
# Include Donor Name, total donated, number of donations and average donation amount as values in each row.
# Using string formatting, format the output rows as nicely as possible. The end 
# result should be tabular (values in each column should align with those above and below)
# After printing this report, return to the original prompt.
# At any point, the user should be able to quit their current task and return to the original prompt.
# From the original prompt, the user should be able to quit the script cleanly


