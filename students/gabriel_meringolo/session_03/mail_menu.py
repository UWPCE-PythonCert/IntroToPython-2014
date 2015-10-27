donors = [["Graham", 1, 5, 10], ["Eric", 4, 6], ["Terry", 5, 5, 5], ["John", 20], ["Michael", 10, 10]]

def get_two(item): #returns the second item
    return item[1]

def doner_list(x): #compiles the donor list descending by total donations
    d_list = []
    for i in x:
        d_list.append(list(((i[0], sum(i[1:]), len(i) - 1, (sum(i[1:]) // (len(i) - 1))))))
    d_list = sorted(d_list,key=get_two, reverse=True)
    print("Donors              Total Amt           Total Donations        Average Amt        ")
    print("------------------------------------------------------------------------------\n")
    for i in d_list:
        donor = str(i[0])
        totes = str(i[1])
        donx = str(i[2])
        ave = str(i[3])
        print("{}".format(donor) + " " * (20 - len(str(i[0]))) + "${}".format(totes) +
              " " * 18 + "{}".format(donx) + " " * 22 + "${}".format(ave),)
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
    print("Welcome to the Python Endowment Fund mailroom.\n\n")
    mail_menu(x)


def mail_menu(x):
    '''
    prints mailroom user interface
    :param x: donor database list
    :return:
    '''
    print("Please make a selection from the menu below.")
    print("--------------------------------------------\a")
    menu = input("1: Send a 'Thank You' Letter to Donor\n2: Create Donor report\n3: Quit\n>")
    if menu == "1":
        name = input("")
        thank_you()
    if menu == "2":
        doner_list(x)
        mail_menu(x)
    if menu.lower() == "quit" or menu == "3":
        print("\nThank you for using the Mail-Tron 2000\nGoodbye")
        quit()


mail_head(donors)




#If the user (you) selected ‘Create a Report’ Print a list of your donors, sorted by total historical donation amount.
#Include Donor Name, total donated, number of donations and average donation amount as values in each row.
#Using string formatting, format the output rows as nicely as possible. The end result should be tabular (values in each column should align with those above and below)
#After printing this report, return to the original prompt.
#At any point, the user should be able to quit their current task and return to the original prompt.
#From the original prompt, the user should be able to quit the script cleanly


#print(dnrct)
#print(dntct)
#print(amtct)