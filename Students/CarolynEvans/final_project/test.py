def test_config():
    # Test config.py
    from config import config

    cnf = config()
    assert cnf.get('hummingbird_url') == 'http://hummingbird.dizzyninja.co/'
    assert cnf.get('dw_dbname') == 'rightsidedw'
    assert cnf.get('email_server') == 'mail.notify-customer.com'


def test_hummingbird():
    # Test hummingbird.py
    # TODO: Add more hummingbird commands to the test.
    from hummingbird import hummingbird

    h = hummingbird()
    result = h('word-split', input='toiletseat')
    assert result['output']['split'] == 'toilet seat'


def test_data_warehouse():
    # Test data_warehouse.py
    # This test dumps a database table to a file.
    # TODO: Add a select query and an update query to the test.
    from data_warehouse import data_warehouse

    dw = data_warehouse()
    # TODO: Make the following line readable.
    query = "unload ('SELECT * FROM utld.tld') to 's3://rightside-data/whois/output/ActiveDomainStatus_20141210_ce.txt' with CREDENTIALS 'aws_access_key_id=AKIAI5ZAKRM5QRQ3LJXA;aws_secret_access_key=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' DELIMITER '\t' PARALLEL OFF ALLOWOVERWRITE GZIP;"
    assert dw(query) == u'no results to fetch'
    #result = dw(query)
    #print result
    x='x'



def test_send_mail():
    # Test send_mail.py
    # The send_mail function only works inside the firewall.
    from send_mail import send_mail
    email_address = 'carolyn.evans@rightside.co'
    subject = 'test.py'
    assert send_mail(email_address=email_address, subject=subject, body="") == None


if __name__ == '__main__':
    test_config()
    test_data_warehouse()
    test_hummingbird()
    #test_send_mail()

