__author__ = 'Robert W. Perkins'


def mk_dbase():
    """Create data structure for donor list"""
    ndbase = [[], [], [], [], []]
    ndbase[0] = ['Jeff McCarthy', 2500, 1000, 500]
    ndbase[1] = ['Tabitha Simmons', 450, 2000]
    ndbase[2] = ['Angela Cartwright', 5500]
    ndbase[3] = ['Billy Murray', 3450, 250]
    ndbase[4] = ['Alexa Dalton', 240, 1200, 5500]
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
    # print 'checking if %s is in dbase' % i_name
    # print len(tar_dbase)-1
    # print len(tar_dbase)
    # for i in range(len(tar_dbase)-1):
    for i in range(len(tar_dbase)):
        # print i, i_name in tar_dbase[i]
        if i_name in tar_dbase[i]:
            return True
    return False

def print_email(p_name, p_donation):
    """ Print thank you not for donation from p_name """
    print 'Dear %s, Thanks so much for your generous donation of $%s.  It is greatly appreciated!' % (p_name, p_donation)

def app_record(app_name, app_dbase):
    """ Append an existing record with new donations """
    for i in range(len(app_dbase)):
        if app_name in app_dbase[i]:
            app_donation = get_donation()
            app_dbase[i].append(app_donation)
            print_email(app_name, app_donation)
            break
    # print app_dbase

def add_record(add_name, add_dbase):
    """ Call get_donation and add new donor to database with result """
    add_donation = get_donation()
    new = [add_name, add_donation]
    add_dbase.append(new)
    print_email(add_name, add_donation)
    # print '--in add_record--', add_dbase


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
        # print '%s is in the dbase' % name
        app_record(name, dbase)
    else:
        # print '%s is not in the dbase' % name
        add_record(name, dbase)
        # print 'in thank_you, returning from add_record--', dbase

def mk_report():
    """ Create a sorted list of donors"""
    print 'Report'

if __name__ == '__main__':
    donor = mk_dbase()
    answer = None
    while not (answer == "q"):
        answer = get_input()
        if answer == "1":
            thank_you(donor)
            # print '--in main--, after thank_you returns', donor
        else:
            mk_report()
    print "Exiting"


