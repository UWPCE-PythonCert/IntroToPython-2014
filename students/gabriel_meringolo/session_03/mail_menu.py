donors = [["Graham", 1, 5, 10], ["Eric", 4, 6], ["Terry", 5, 5, 5], ["John", 20], ["Michael", 10, 10]]


def get_two(item):
    '''returns second item in list'''
    return item[1]


def report(x):
    '''
    compiles the donor list descending by total donations
    :param x: donor database list
    :return:
    '''
    d_list = []
    for i in x:
        d_list.append(list(((i[0], sum(i[1:]), len(i) - 1, (sum(i[1:]) // (len(i) - 1))))))
    d_list = sorted(d_list,key=get_two, reverse=True)
    print("\nDonors              Total Amt           Total Donations        Average Amt        ")
    print("------------------------------------------------------------------------------\n")
    for i in d_list:
        donor = str(i[0])
        totes = str(i[1])
        donx = str(i[2])
        ave = str(i[3])
        print("{}".format(donor) , " " * (20 - len(str(i[0]))) , "${}".format(totes) ,
              " " * 18 , "{}".format(donx) , " " * 22 + "${}".format(ave),)
    print("\n")



def mail_head(x):
    '''
    prints mailroom greeting
    :param x: donor database list
    :return:
    '''
    print("#----------------------------#")
    print("|       MAIL-TRON 2000       |")
    print("|           V 1.0            |")
    print("#----------------------------#\n\n")
    input("Press enter to continue.\a\n")
    print("Welcome to the Python Endowment Fund mailroom.")
    mail_menu(x)


def quit_mr():
    '''prints goodbye and quits program'''
    print("\nThank you for using the Mail-Tron 2000\nGoodbye")
    quit()


def mail_menu(x):
    '''
    prints mailroom user interface
    :param x: donor database list
    :return:
    '''
    print("\nPlease make a selection from the menu below.")
    print("--------------------------------------------\a")
    menu = input("1: Send a 'Thank You' Letter to Donor\n2: Create Donor report\n3: Quit\n> ")
    if menu == "1":
        thank_you(x)
    if menu == "2":
        report(x)
        mail_menu(x)
    if menu.lower() == "quit" or menu == "3":
        quit_mr()


def thank_you(x):
    '''
    displays thank you letter menu
    :param x: donor database list
    :return:
    '''
    pers = input("\nPlease make a selection from the menu below\n"
                 "-------------------------------------------\n"
                 "1. Enter Donor name\n2. Display list of Donors\n3. Return to Main Menu\n4. Quit\n> ")
    if pers == "1":
        thanks(x, add_donate(x, (donor_check(x))))
    if pers == "2":
        donor_names(x)
        thank_you(x)
    if pers == "3":
        mail_menu(x)
    if pers.lower() == "quit" or pers == "4":
        quit_mr()


def flat_list(x):
    '''
    flattens nested list and makes new list
    :param x: nested list
    :return:
    '''
    flat = []
    for i in x:
        for ii in i:
            flat.append(ii)
    return flat


def donor_names(x):
    '''
    prints list of donor names
    :param x: donor list
    :return: donors ini x
    '''
    print("\n")
    for i in x:
        print(i[0])
    print("\n")

def add_donor(x, y):
    '''
    adds donor to list
    :param x: donor database list
    :param y: donor name
    :return: donor name y added at end of list x
    '''
    x.append([y, ])
    print("\nAdded Donor: {}".format(y))
    return y


def donor_check(x):
    '''
    checks for donor on list
    :param x: donor database list
    :param y: donor name
    :return:
    '''
    y = input("\nEnter Donor name\n> ")
    if y.lower() == "quit":
        quit_mr()
    if y in flat_list(x):
        print("\nDonor Found")
        return y
    elif y not in flat_list(x):
        return add_donor(x,y)


def add_donate(x, y):
    '''
    adds a donation
    :param x: donor database list
    :param y: donor name
    :return:
    '''
    z = input("\nEnter donation amount\n> ")
    if num_check(x, y, z) == True:
        for i in x:
            if i[0] == y:
                i.append(int(z))
                return i


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



def num_check(x, y, z):
    '''
    checking for float or int
    :param x: donor database list
    :param y: donor
    :param z: donation amount
    :return:
    '''
    try:
        float(z) or int(z)
        return True
    except:
        print("That is not a valid donation")
        add_donate(x, y)


if __name__ == '__main__':
    mail_head(donors)


"""x = donor list
   y = donor name
   z = donation amount
"""
