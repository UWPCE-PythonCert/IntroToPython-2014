#! /usr/bin/env python3

# had a busy week - this is a work in progress - just realized too i probably should not be using dicts
# i will make another version using just lists (or maybe a tuple with a list in it)

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

def mailroom():
    a = ''
    while a != '1' or '2':
        a = input("\nPress 1 to 'Send a Thank You' or 2 to 'Create a Report': ")
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
            else:
                m = get_donation()
                donors[n] = [m]
                print(donors[n])



if __name__ == "__main__":
    while 1:
        mailroom()