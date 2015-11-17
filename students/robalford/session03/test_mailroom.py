import os

import mailroom


def test_list_donors():
    donor_list = mailroom.list_donors()
    assert 'John Lennon' and 'Ringo Starr' in donor_list


def test_write_email():
    email = mailroom.write_email('Yoko Ono', 500.00)
    assert email.startswith('Dear Yoko Ono')
    assert 'donation of $500.0' in email


def test_add_new_donation():
    # new donation for existing donor
    mailroom.add_new_donation('Ringo Starr', 1.00)
    assert mailroom.donors['Ringo Starr'][-1] == 1.00
    # add new donor
    mailroom.add_new_donation('Bob Dylan', 10000.00)
    assert mailroom.donors['Bob Dylan'][0] == 10000.00


def test_create_report():
    # add a new donor and check that they are in report
    mailroom.add_new_donation('New Donor', 23.00)
    report = mailroom.create_report()
    assert ('New Donor', 23.0, 1, 23.0) in report
    # verify average donation
    assert report[0][1]/report[0][2] == report[0][3]


def test_create_letter_files():
    mailroom.create_letter_files()
    assert os.path.isfile('John Lennon.txt')
