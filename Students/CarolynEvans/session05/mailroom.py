

def send_thanks():
    return 'send_thanks'


def create_report():
    return 'create_report'

def main():
    menu_choice = 0

    while menu_choice not in (1,2):
        print menu_choice

        menu_choice = raw_input("Enter 1 to send a thank you. \nEnter 2 to create a report.")

        if menu_choice == 1:
            send_thanks()

        elif menu_choice == 2:
            create_report()

if __name__ == '__main__':
    main()

