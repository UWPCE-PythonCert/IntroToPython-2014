#! /usr/bin/env python3

# mailroom exercise with a dictionary instead of lists

import sys

donors = {
    'John Doe' : ['25', '50', '50'],
    'Jane Doe' : ['25', '25', '25'],
    'Al Coholic' : ['100'],
    'Homer Sexual' : ['50', '100'],
    'Hugh Jass' : ['25', '50', '100'],
}


def get_donation():
    m = ''
    while not m.isdigit():
        m = input("\nDonation amount: ")
    return m


def make_email(name, donation):
    print("\nThank you {} for your donation of ${}!".format(name, donation))


def mailroom():
    a = ''
    while a not in ('1','2'):
        a = input("\nPress 1 to 'Send a Thank You', 2 to 'Create a Report', or  q to 'Quit': ")
        if a == '1':
            n = input("\nEnter full name or type 'list' to list all current donors: ")
            if n == 'list':
                print()
                for k in donors.keys():
                    print(k)
            elif n in donors.keys():
                m = get_donation()
                donors[n].append(m)
                print(donors[n])
                make_email(n,m)
            else:
                m = get_donation()
                donors[n] = [m]
                print(donors[n])
        if a == '2':
            print('\nName\t\t\tDonations\tAverage\t\tTotal\n')
            for n in donors.keys():
                d = donors[n]
                t = 0
                for i in d:
                    t = t + int(i)
                avg = int(t) // len(d)
                print("{}\t\t{:^9}\t{:^7}\t\t{:^5}".format(n, len(d), avg, t))
        if a == 'q':
            sys.exit()
            

if __name__ == "__main__":
    while 1:
        mailroom()