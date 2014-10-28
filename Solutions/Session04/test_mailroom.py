#!/usr/bin/env python

"""
unit tests for the mailroom program
"""
import os

import mailroom


#DB = mailroom.donor_db

def test_list_donors():
    listing = mailroom.list_donors()

    # hard to test this throughly -- better not to hard code the entire
    # thing. But check for a few aspects -- this will catchthe likley
    # errors
    assert listing.startswith("Donor list:\n")
    assert "Jeff Bezos" in listing
    assert "William Gates, III" in listing
    assert len(listing.split('\n')) == 5


def test_find_donor():
    """ checks a donor that isthere, but with odd case and spaces"""
    donor = mailroom.find_donor("jefF beZos ")

    assert donor[0] == "Jeff Bezos"


def test_find_donor_not():
    "test one that's not there"
    donor = mailroom.find_donor("Jeff Bzos")

    assert donor is None


def test_gen_letter():
    """ test the donor letter """

    # create a sample donor
    donor = ( "Fred Flintstone", [432.45, 65.45, 230.0] )
    letter = mailroom.gen_letter(donor)
    # what to test? tricky!
    assert letter.startswith("Dear Fred Flintstone")
    assert letter.endswith("-The Team\n")
    assert "donation of $230.00" in letter


def test_add_donor():
    name = "Fred Flintstone  "

    donor = mailroom.add_donor(name)
    donor[1].append(300)
    assert donor[0] == "Fred Flintstone"
    assert donor[1] == [300]
    assert mailroom.find_donor(name) == donor


def test_generate_donor_report():

    report = mailroom.generate_donor_report()

    print report
    assert report.startswith("               Donor Name | Total Given | Num Gifts | Average Gift")
    assert "               Jeff Bezos        877.33           1         877.33" in report


def test_save_letters_to_disk():
    """This only tests that the files get created, but that's a start"""

    mailroom.save_letters_to_disk()

    assert os.path.isfile('Jeff_Bezos.txt')
    assert os.path.isfile('William_Gates,_III.txt')

