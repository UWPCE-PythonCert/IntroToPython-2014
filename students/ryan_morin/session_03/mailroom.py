
dl = [['John Smith', 100, 30], ['Fred Jenkins', 80], ['Mag Down', 123, 20, 5], ['Jo James', 10],
              ['Mike Tom', 20,50]]

def in_dl(dl):
    """
    The function generates a list of names
    :param dl: List of existing donors and amounts donated
    :return: returns the list of names in dl
    """
    dn = []
    for d in dl:
        dn.append(d[0])
    return dn

def sorted_list(dl):
    for i in dl:
        print(i)

def is_number(inpt):
    """
    The function checks whether an input is a float
    :param inpt: The input that is being checked
    :return: a bool - True if input is a float and False if otherwise
    """
    try:
        float(inpt)
        return True
    except ValueError:
        return False

def donor_list(dl):
    """
    Prints a list of names
    :param dl: List of existing donors and amounts donated
    :return: Print formatted list of names from list dl
    """
    print ('\n')
    print ("The list of current donors:")
    for d in dl:
        print (d[0])
    print ('\n')

def report(dl):
    """
    The function prints a formatted list of information pertaining to donors
    :param dl: List of existing donors and amounts donated
    :return: Prints a formatted list of names, number of donations, donation total and average donation
    """
    total = 0
    print('\n')
    for donor in dl:
        doner_name = donor[0]
        num_don = (len(donor)-1)
        total = sum(donor[1:])
        avg_don = total//num_don
        print ("Name: {:15} | Number of Donations: {:5} | Donation Total ${:>5} | Average Donation ${:>5}".format(
            doner_name, num_don, total, avg_don))
    print ("\n")
    return menu()

def menu():
    """
    Prompts user and calls one of two functions based on response
    """
    print('\n')
    action = input('Choose from the following actions: "Send a Thank You" or "Create a Report": ')
    if action == 'Send a Thank You':
        thank_you()
    elif action == 'Create a Report':
        report(dl)
    else:
        print('\n')
        return('Good bye')


def thank_you():
    """
    The function prompts the user for two inputs, confirms one input is number and updates list dl
    :return: prints an output to the console
    """
    response = ""
    amount = ""
    while response != 'Quit':
        response = input('Please provide a full name or type "Quit" to exit: ')
        if response == 'Quit':
            print('\n')
            print ("...exiting program")
            menu()
        elif response.lower() == 'list':
            donor_list(dl)
        else:
            while is_number(amount) == False:
                amount = input("Please provide a donation amount: ")
            if response not in in_dl(dl):
                dl.append(response)
            for i in dl:
                if response == i[0]:
                    i.append(amount)
            print('\n')
            print ("Thanks {} for your generous ${:,} donation".format(response, int(amount)))
            print('\n')

if __name__ == '__main__':
    print (menu())