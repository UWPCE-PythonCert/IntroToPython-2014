#! /usr/bin/env python3



donors = {
    'John Doe' : [25, 50, 50],
    'Jane Doe' : [25, 25, 25],
    'Al Coholic' : [100],
    'Homer Sexual' : [50, 100],
    'Hugh Jass' : [25, 50, 100],
}

def mailroom():
    a = input("\nPress 1 to 'Send a Thank You' or 2 to 'Create a Report': ")
    if a == '1':
        n = input("\nEnter full name or type 'list' to list all current donors: ")
        if n == 'list':
            print()
            for k in donors.keys():
                print(k)
        elif n in donors.keys():
            m = ''
            while not m.isdigit():
                m = input("\nDonation amount: ")
            print(m)    
        else:
            m = ''
            while not m.isdigit():
                m = input("\nDonation amount: ")
            donors[n] = m
            print(donors[n])



if __name__ == "__main__":
    while 1:
        mailroom()