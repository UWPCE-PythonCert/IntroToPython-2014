donors = {"Graham": [1, 5, 10], "Eric": [4, 6], "Terry" : [5, 5, 5], "John": [20,], "Michael": [10, 10]}
donor_dict = donors
#dict_list = list(donor)


def report(donor_dict):
    print("\nDonors              Total Amt           Total Donations        Average Amt        ")
    print("------------------------------------------------------------------------------")
    for i in donor_dict:
        donor = i
        donations = str((donors.get(i))).strip("[]")
        total = sum(donors.get(i))
        average = sum(donors.get(i))//len(donors.get(i))
        print("{:<20} {:>4} {:>25} {:>20}".format(donor, total, donations, average))


def quit_mr():
    '''prints goodbye and quits program'''
    print("\nThank you for using the Mail-Tron 2000\nGoodbye")
    quit()


def mail_menu(donor_dict):
    '''
    prints mailroom user interface
    :param donor_dict: donor database list
    :return:
    '''
    print("\nPlease make a selection from the menu below.")
    print("--------------------------------------------\a")
    menu = input("1: Send a 'Thank You' Letter to Donor\n2: Create Donor report\n3: Quit\n> ")
    if menu == "1":
        thank_you(donor_dict)
    if menu == "2":
        report(donor_dict)
        mail_menu(donor_dict)
    if menu.lower() == "quit" or menu == "3":
        quit_mr()


def thank_you(donor_dict):
    '''
    displays thank you letter menu
    :param donor_dict: donor database list
    :return:
    '''
    pers = input("\nPlease make a selection from the menu below\n"
                 "-------------------------------------------\n"
                 "1. Enter Donor name\n2. Display list of Donors\n3. Return to Main Menu\n4. Quit\n> ")
    if pers == "1":
        thanks(donor_dict, add_donate(donor_dict, (donor_check(donor_dict))))
    if pers == "2":
        donor_names(donor_dict)
        thank_you(donor_dict)
    if pers == "3":
        mail_menu(donor_dict)
    if pers.lower() == "quit" or pers == "4":
        quit_mr()


def donor_names(donor_dict):
    '''
    prints list of donor names
    :param donor_dict: donor list
    :return: donors ini x
    '''
    print("\n" + "\n".join(list(i for i in donor_dict)))




def mail_head(donor_dict):
    '''
    prints mailroom greeting
    :param donor_dict: donor database list
    :return:
    '''
    print("#----------------------------#")
    print("|       MAIL-TRON 2000       |")
    print("|           V 2.1            |")
    print("#----------------------------#\n\n")
    input("Press enter to continue.\a\n")
    print("Welcome to the Python Endowment Fund mailroom.")
    mail_menu(donor_dict)







#mail_head(donors)












def add_donor(donor_dict, donor_name):
    '''
    adds donor to list
    :param x: donor database list
    :param y: donor name
    :return: donor name y added at end of list x
    '''
    donor_dict[donor_name] = []
    print("\nAdded Donor: {}".format(donor_name))
    return donor_name


def donor_check(donor_dict):
    '''
    checks for donor on list
    :param x: donor database list
    :param y: donor name
    :return:
    '''
    donor_name = input("\nEnter Donor name\n> ")
    if donor_name.lower() == "quit":
        quit_mr()
    if donor_name in donor_dict:
        print("\nDonor Found")
        return donor_name
    elif donor_name not in donor_dict:
        return add_donor(donor_dict, donor_name)


def add_donate(donor_dict, donor_name):
    '''
    adds a donation
    :param x: donor database list
    :param y: donor name
    :return:
    '''
    donation = input("\nEnter donation amount\n> ")
    if num_check(donation):
        (donor_dict.get(donor_name)).append(donation)
        print((donor_dict.get(donor_name)))
        print("**" * 100)
        print("**" * 100)
        for name in donor_dict:
            if name == donor_name:
                print(donor_dict.keys(donor_name))
                donor_dict[donor_name] = donation
                print("found")

               # i(int(donation))
                #return i


def thanks(x, y):
    '''
    creates and prints boring repetitve email
    :param x: donor database list
    :param y: specific donor sub list
    :return:
    '''
    name = y[0]
    donation = y[-1]
    print("Thank you Mr(s). {} for your most genourous donation of ${}".format(name, donation))
    mail_menu(x)



def num_check(donation):
    '''
    checking for float or int
    :param x: donor database list
    :param y: donor
    :param z: donation amount
    :return:
    '''
    try:
        int(donation)
        return True
    except:
        print("That is not a valid donation")
        #add_donate(x, y)


if __name__ == '__main__':
    mail_head(donors)
