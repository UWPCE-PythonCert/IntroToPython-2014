"""
junk.py
"""

# length of person name for printing
def person_len(person):
    l = 0
    for p in person:
        l += len(p)
    return l


# make a name list and a money list
def list_maker(client_list):
    donors = []
    donations = []
    for person in client_list:
        donors.append(person[0])
        donations.append(person[1])
    return donors, donations


# make standard name format for handling
def name_split(nme):
    fname, lname = nme.split(' ')
    return (lname, fname)


# take a name and check the list, return true where present, else false
def client_check(nme, donors):
    fname, lname = nme.split(' ')
    if (lname, fname) in donors:
        print '{f} {l} is a previous donor.'.format(f=fname, l=lname)
        return True
    else:
        print '{f} {l} is a not a previous donor.'.format(f=fname, l=lname)
        return False