#!/usr/local/bin/python


import mailroom3 as mail


def test_create_donation_list():
    assert type(mail.create_donation_list()) == dict


def test_send_mail():
    assert type(mail.send_mail('Salim Hamed', 100)) == str
    assert mail.send_mail('Salim Hamed', 100).count('Salim Hamed') == 1
    assert mail.send_mail('Salim Hamed', 100).count('100') == 1


def test_list_doners():
    assert type(mail.list_doners(mail.create_donation_list())) == str
    assert (mail.list_doners(mail.create_donation_list()).count('\n') ==
            len(mail.create_donation_list()))
    assert mail.list_doners(mail.create_donation_list()).count('Salim') == 1


def test_display_report():
    assert type(mail.display_report(mail.create_donation_list())) == str
    assert mail.display_report(mail.create_donation_list()).count('Salim') == 1
