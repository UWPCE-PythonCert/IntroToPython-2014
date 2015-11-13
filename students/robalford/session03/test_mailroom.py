from mailroom import write_email, add_new_donation

def test_write_email():
    email = write_email('Yoko Ono', 500.00)
    assert email.startswith('Dear Yoko Ono')
    assert 'donation of $500.0' in email

def test_add_new_donation():
    # exit function if user types 'home'
    assert add_new_donation('Bob Dylan', 'home') == None


