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


def in_dbase(name, dbase):
    """ Check if name is in dbase and return boolean """
    for i in range(len(dbase)-1):
        if name in dbase[i]:
            return True
    return False


def app_record(name, dbase):
    """ Append an existing record with new donations """
    for i in range(len(dbase)-1):
        if name in dbase[i]:
            dbase[i].append(get_donation())
    print dbase

def add_record(name, dbase):
    """ Call get_donation and add new donor to database with result """
    new = [name, get_donation()]
    dbase.append(new)
    print dbase

def thank_you(dbase):
    """ Find or create a donor, add new donation, and return a thank you note"""
    name = 'list'
    while name == 'list':
        new_name = raw_input("Enter full name of donor-->")
        name = str(new_name)
        if not (name == 'list'):
            break
        else:
            for i in range(len(dbase)-1):
                print dbase[i][0]

    if in_dbase(name, dbase):
        app_record(name, dbase)
    else:
        add_record(name, dbase)


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
        else:
            mk_report()
    print "Exiting"


