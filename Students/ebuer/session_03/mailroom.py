#mailroom program to break the monotony

import random

def rd():
    return round(random.random() * 100, 2)

#this may be a bad idea but we will see, a list of tuples for clients
client_list = [
    (('Askew', 'Anne'), (rd(), rd(), rd())),
    (('Bocher', 'Joan'), (rd(), rd())),
    (('Clarkson', 'Jeremy'), (rd())),
    (('Hamont', 'Matthew'), (rd(), rd(), rd())),
    (('May', 'James'), (rd(), rd())),
    (('Parris', 'George van')] (rd(), rd(), rd()))]








#take a name and check the list
def client_check(nme, client_list):
    fname, lname = nme.split(' ')
    if (lname, fname) in client_list:
        print '{f} {l} is a previous donor.'.format(f=fname, l=lname)
        return True
    else:
        print '{f} {l} is a not a previous donor.'.format(f=fname, l=lname)
        return False

res=client_check('Annie Askew', client_list)
