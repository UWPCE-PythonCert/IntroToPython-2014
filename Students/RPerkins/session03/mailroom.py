__author__ = 'Robert W. Perkins'


def mk_dbase():
    """Create data structure for donor list"""
    ndbase = [[], [], [], [], []]
    # donor name, sum of donations, donation 1, donation 2, ...
    ndbase[0] = ['Jeff McCarthy', 4000, 2500, 1000, 500]
    ndbase[1] = ['Tabitha Simmons', 2450, 450, 2000]
    ndbase[2] = ['Angela Cartwright', 5500, 5500]
    ndbase[3] = ['Billy Murray', 3700, 3450, 250]
    ndbase[4] = ['Alexa Dalton', 6940, 240, 1200, 5500]
    return ndbase


def get_input():
    """Ask user whether to send thank you note or create report and return answer"""
    answer = None
    while not ((answer == '1') or (answer == '2') or (answer == "q")):
        new_answer = raw_input("Enter '1' to Send a Thank-You Note, Enter '2' to Create a Report, Enter 'q' to quit-->")
        answer = str(new_answer)
    return answer


def get_donation():
    """ Prompt for donation amount, validate input, return amount"""
    d = u' '
    while not d.isnumeric():
        new_d = raw_input("Enter donation amount (must be numeric)-->")
        d = unicode(new_d)
    return str(d)


def in_dbase(i_name, tar_dbase):
    """ Check if name is in dbase and return boolean """
    for i in range(len(tar_dbase)):
        if i_name in tar_dbase[i]:
            return True
    return False


def print_email(p_name, p_donation):
    """ Print thank you not for donation from p_name """
    print 'Dear %s, Thanks so much for your generous donation of $%s.  It is greatly appreciated!' % (p_name, p_donation)


def app_record(app_name, app_dbase):
    """ Append an existing donor record """
    for i in range(len(app_dbase)):
        if app_name in app_dbase[i]:
            app_donation = get_donation()
            app_dbase[i].append(app_donation)
            app_dbase[i][1] += int(app_donation)
            print_email(app_name, app_donation)
            break


def add_record(add_name, add_dbase):
    """ Add new donor to database """
    add_donation = get_donation()
    new = [add_name, int(add_donation), add_donation]
    add_dbase.append(new)
    print_email(add_name, add_donation)


def thank_you(dbase):
    """ Find or create a donor, add new donation, and return a thank you note"""
    name = 'list'
    while name == 'list':
        new_name = raw_input("Enter full name of donor-->")
        name = str(new_name)
        if not (name == 'list'):
            break
        else:
            for i in range(len(dbase)):
                print dbase[i][0]
    if in_dbase(name, dbase):
        app_record(name, dbase)
    else:
        add_record(name, dbase)


def sum_element(key_dbase):
    """set key for sorting on sum element of data structure"""
    return key_dbase[1]


def mk_report(rep_dbase):
    """ Create a sorted list of donors"""
    print 'Donor Name\t\t\tTotal Donations\t# of Donations\t\tAverage Donation'
    rep_dbase.sort(key=sum_element)
    for j in range(len(rep_dbase)):
        donor_slice = rep_dbase[j][2:]
        num_donations = (len(donor_slice))
        avg_donation = int(rep_dbase[j][1])/num_donations
        print '%s\t\t\t%s\t\t\t\t%s\t\t\t\t\t\t%s' % (rep_dbase[j][0], rep_dbase[j][1], num_donations, avg_donation)


if __name__ == '__main__':
    donor = mk_dbase()
    answer = None
    while not (answer == "q"):
        answer = get_input()
        if answer == "q":
            break
        elif answer == "1":
            thank_you(donor)
        else:
            mk_report(donor)
    print "Exiting"