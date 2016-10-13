#!/usr/bin/env python


def print_report():
    print("This will print a report")


def send_thanks():
    print("This will write a thank you note")

# here is where triple quoted strings can be helpful
msg = """
What would you like to do?

To send a thank you: type "s"
To print a report: type "p"
To exit: type "x"
"""


def main():
    """
    run the main interactive loop
    """

    response = ''
    # keep asking until the users responds with an 'x'
    while True:  # make sure there is a break if you have infinite loop!
        print(msg)
        response = input("==> ").strip()  # strip() in case there are any spaces

        if response == 'p':
            print_report()
        elif response == 's':
            send_thanks()
        elif response == 'x':
            break
        else:
            print('please type "s", "p", or "x"')

if __name__ == "__main__":
    main()
