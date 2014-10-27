__author__ = 'Robert W. Perkins'


def mk_dbase():
    """Create data structure for donor list"""
    # donor name = key: sum of donations, donation 1, donation 2, ...
    ndbase = {
        'Jeff McCarthy': [4000, 2500, 1000, 500],
        'Tabitha Simmons': [2450, 450, 2000],
        'Angela Cartwright': [5500, 5500],
        'Billy Murray': [3700, 3450, 250],
        'Alexa Dalton': [6940, 240, 1200, 5500]
    }
    return ndbase


def get_input():
    """Ask user whether to send thank you note or create report and return answer"""

    choices = {
        '1': 'Enter "1" to Send a Thank-You Note',
        '2': 'Enter "2" to Create a Report',
        'q': 'Enter "q" to quit-->'
    }
    in_put = None
    while not in_put in choices:
        in_put = raw_input('%s, %s, %s' % (choices['1'], choices['2'], choices['q']))
    return in_put


def safe_input():
    try:
        new_d = raw_input("Enter donation amount (must be numeric)-->")
    except EOFError:
        return None
    except KeyboardInterrupt:
        return None
    return int(new_d)


def print_email(p_name, p_donation):
    """ Print thank you note for donation from p_name """
    ltr_temp = {'Template1': 'Dear {name}, Thanks so much for your generous donation of ${donation}.  '
                             'It is greatly appreciated!'
                }

    print ltr_temp['Template1'].format(name=p_name, donation=p_donation)


def app_record(app_name, app_dict):
    """ Append an existing donor record """
    app_donation = safe_input()
    app_dict[app_name].append(app_donation)
    app_dict[app_name][0] += app_donation
    print_email(app_name, app_donation)


def add_record(add_name, add_dict):
    """ Add new donor to database """
    add_donation = safe_input()
    add_dict[add_name] = [add_donation, add_donation]
    print_email(add_name, add_donation)


def thank_you(donor_dict):
    """ Find or create a donor, add new donation, and return a thank you note"""
    name = 'list'
    while name == 'list':
        new_name = raw_input("Enter full name of donor-->")
        name = str(new_name)
        if not (name == 'list'):
            break
        else:
            for item in donor_dict:
                print item

    if name in donor_dict:
        app_record(name, donor_dict)
    else:
        add_record(name, donor_dict)


def write_efile(name, donation_list):
    """write a donor email to disk named "name".txt"""
    to_file = './%s.txt' % name
    outdata = 'Dear %s, Thanks so much for your recent generous donation of $%s.  ' \
              'It is greatly appreciated!' % (name, donation_list[-1])
    open(to_file, 'w').write(outdata)


#def sum_element(key_dbase):
    #"""set key for sorting on sum element of data structure"""
    #return key_dbase[1]


def mk_report(rep_dict):
    """ Create a sorted list of donors"""
    print 'Donor Name\t\t\tTotal Donations\t# of Donations\t\tAverage Donation'
    #rep_dbase.sort(key=sum_element)
    for j, k in rep_dict.items():
        num_donations = len(k)-1
        avg_donation = k[0]/(len(k)-1)
        print '%s\t\t\t%s\t\t\t\t%s\t\t\t\t\t\t%s' % (j, k[0], num_donations, avg_donation)
        write_efile(j,k)


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
