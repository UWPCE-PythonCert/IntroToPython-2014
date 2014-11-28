
def execute():
    """Run the main program """
    donors = [["Jon Doe", 50, 2], ["Jane Doe", 35, 7], ["Anonymous", 30, 10]]
    prompt = "Please, select the following options\n1 - Send a Thank you Letter\n2 - Create Report\n3 - Quit\n"
    while True:
        print prompt
        answer = raw_input("What is your choice: ")
        if answer == '2':
            print_report(donors)
        elif answer == '1':
            generate_letters(donors)
        elif answer == '3':
            print "Have a good day"
            break
        else:
            print "Unrecognized option"
    print ""
            
def print_report(d):
    """Print users' report"""
    for donor in d:
        avg_amnt = 0
        if donor[2] == 0:
            avg_amnt = 0
        else:
            avg_amnt = donor[1]/donor[2]
        print "Name: %s\tTotal Donated: $%2.2f\tNumber of Donations: %i\tAverage Donation: $%2.2f" % (donor[0], donor[1], donor[2], avg_amnt)
    print ""
    
def generate_letters(d):
    """Generate Thank you letter"""
    name = select_donor(d)
    donation = get_donation(name)
    email_text = "Dear " + name + ",\n\nThank you very much for your generous donation of $" + str(donation) + ".\nThis donation will go a long way."
    email_text = email_text + "\n\nThank you again,\n\nSupport Staff"
    print "\n======================================================================="
    print email_text
    print "=======================================================================\n"
    for k in d:
        if k[0] == name:
            k[1] = k[1] + float(donation)
            k[2] = k[2] + 1
    
def get_donation(n):
    """Obtain donation ammount"""
    while True:
        amount = raw_input("\nProvide donation amount: ")
        try:
            if float(amount):
                return float(amount)
        except ValueError:
            print "Invalid Number provided for donation"

def select_donor(d):
    """Obtain Donor name to use"""
    while True:
        n = raw_input("\nType the name of the donor or type the work 'list': ")
        if n == "list":
            print n == "list"
            for x in d:
                print x[0]
        else:
            for g in d:
                if g[0] == n:
                    return n
            d.append([n, 0, 0])
            return n

if __name__ == "__main__":
    """Execute the main program"""
    execute()
    
