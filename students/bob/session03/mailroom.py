#!/usr/bin/python

# mailroom.py - automate thank-you note generation

#  data structure that holds a list of donors & history of the amounts they've paid

# notes from reading:
#   start using raw_input in place of input.  input allows for code execution

donors = {'alice':[1,2,3],'bob':[10,20,30],'carl':[11,12,13],'dan':[44,66],'earl':[2]}

def mailroom():
    ##send = send()
    ##mailroom = mailroom()
    ##report = report()
    action = input('''
Enter "1" to send a Thank You,
      "2" to create a report, or
      "0" to exit the program:   ''')
    if action == '1':
        print(send())
    if action == '2':
        print(report())
    if action == '0':
        return('')
    else:
        return(mailroom())

def send():
    amount = 'temp' # variable to enter the while loop
    ##del amount # need to ensure the varaible doesn't exist for later processing
    donor = input("Enter donor's full name: ")
    if donor not in donors: # if the name isn't in the dict
        donors[donor] = []  # create it
    while type(amount) != float:
        try:
           amount = input('Please enter the donation amount: $')
           amount = float(amount)
        except ValueError:
            print('Float or int, buddy')

    ##amount = input('Please enter the dollar amount: ')  ## this ruins everything until we ensure it's int or float.
    ##print(amount,type(amount))
    ##while type(amount) != (int or float):
    ##    del amount
    ##    amount = input('Please enter the amount {} donated: '.format(donor))
    ##    print(amount,type(amount))
    donors[donor] += [amount] # add the amount to the donor's list
    print('''
        Dear {}, 
        Project Arcturus couldn't have succeeded without your ${}.

        Drop me a line if you're on the East Coast.
        Hank Scorpio

        '''.format(donor,amount))
    print(mailroom())

def report():
    print('\nreports:  COMING EVENTUALLY')
    print(mailroom())

if __name__ == '__main__':
    print(mailroom())

