'''
Ian Cote
Mail Room
'''


def list_donors():
    pass


def thankyou():
    d = input("Donor's name (enter 'list' for current donor roster): ")
    if d == 'list':
        print(list_donors)


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
==============================================================
A) Send a 'Thank You' note
B) Create a report
X) Quit

'''

    while True:
        print(menu)
        x = input('>')
        if x.lower() is 'a':
            pass
        elif x.lower() is 'b':
            pass
        elif x.lower() is 'x':
            break
