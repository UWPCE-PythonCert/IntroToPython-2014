#! /usr/bin/env python3


import sys

donors = [
    ('John Doe', ['25', '50', '50']),
    ('Jane Doe', ['25', '25', '25']),
    ('Al Coholic', ['100']),
    ('Homer Sexual', ['50', '100']),
    ('Hugh Jass', ['25', '50', '100'])
]


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
                for p, d in donors:
                    print(p)
            else:
                for p, d in donors:
                    if p == n:
                        m = get_donation()
                        d.append(m)
                        break
                    else:
                        m = get_donation()
                        donors.append((n, [m]))
                        break
                #print(donors)
                make_email(n,m)
        if a == '2':
            print('\nName\t\t\tDonations\tAverage\t\tTotal\n')
            for p, d in donors:
                t = 0
                for i in d:
                    t = t + int(i)
                avg = int(t) // len(d)
                print("{:20}\t{:^9}\t{:^7}\t\t{:^5}".format(p, len(d), avg, t))
        if a == 'q':
            sys.exit()
            

if __name__ == "__main__":
    while 1:
        mailroom()