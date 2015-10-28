'''
Ian Cote
Mail Room
'''


def list_donors():
    ''' Return sorted list of donors'''
    x = [i for i in donors.keys()]
    x.sort()
    return x


def write_email(d, a):
    ''' Print email to screen
        d is the donor name
        a is the amount donated'''
    email = '''
Dear {name},
    Thank you kindly for your significant contribution of ${amount:,.2f}.

Sincerely,
The Mgmt
'''
    return email.format(name=d, amount=a)


def get_donation():
    '''Request and return a .2f formatted float'''
    while True:
        try:
            a = float(input("Enter donation amount: "))
        except ValueError:
            print("Donation must be a number.")
        break
    # Ensure that we are returning a formatted float
    return float('{0:.2f}'.format(a))


def send_thank_you():
    prompt = "Donor's full name (enter 'list' for roster or 'menu'"\
             " for main menu): "
    # Print out donor list if requested
    while True:
        d = input(prompt)
        if d == 'list':
            print('Current Donors', '='*70)
            for i in list_donors():
                print(i)
            print('\n')
            continue
        elif d == 'menu':
            return
        else:
            # We got a name
            break
    # Add new donor if not in list
    if d not in donors:
        donors[d] = []
    # Get donation amount
    amount = get_donation()
    donors[d].append(amount)
    print(write_email(d, amount))

if __name__ == '__main__':
    donors = {
          'Bobcat Goldthwait': [100, 150, 125],
          'Whoopie Goldberg': [500],
          'Demi Moore': [25, 25, 25, 50, 127.25],
          'Nelson Mandela': [1000.25, 15.72, 2000, 432.12],
          'Faith Coleman': [1, 1, 1, 1],
          'Carl Butler': [2.5, 2.5, 2.5, 50],
          'Harry Simpson': [65, 13.24],
          'Michelle Knox': [893.68, 932.48, 42.37]
          }

    menu = '''
MailRoom
=====================================================================
A) Send a 'Thank You' note
B) Create a report
X) Quit

'''

    while True:
        print(menu)
        x = input('> ')
        if x.lower() == 'a':
            # Send a 'Thank You'
            send_thank_you()
        elif x.lower() == 'b':
            # Report
            pass
        elif x.lower() == 'x':
            # Quit
            break
