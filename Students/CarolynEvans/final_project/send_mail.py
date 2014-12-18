import smtplib
from config import config


def send_mail(email_address, subject, body=''):
    """
    This function sends email notifications to the current user.

    :param email_address: This is the email address of the current user that was obtained from the ldap call.
    :param subject: This parameter will be used as the subject line of the email.
    :param body: This parameter will be used as the body of the email.
    """

    # If email is None, the task is being run from the command line and no email is sent.
    if email_address is None:
        return

    cnf = config()
    SERVER = cnf.get('email_server')
    FROM = "noreply@rightside.co"
    TO = [email_address]
    TEXT = 'Subject: %s\n\n%s' % (subject, body)

    # Send the mail
    server = smtplib.SMTP(SERVER)
    server.sendmail(FROM, TO, TEXT)


