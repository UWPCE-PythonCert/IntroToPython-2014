#!/usr/bin/env python


def create_donation_list():
    d_list = [['Salim Hamed', [100, 900, 1500]],
              ['Iris Marlin', [300]],
              ['John Doe', [200, 1904343]],
              ['Terry Smith', [850]],
              ['Bill Williams', [450, 894]],
              ['Richard Sherman', [500, 900, 50000]]]
    return d_list


def list_doners(d_list):
    s = ''
    for doner in d_list:
        s += (doner[0] + '\n')
    return s.rstrip()


def in_list(name, d_list):
    return_bool = False
    for item in d_list:
        if type(item[0]) == str:
            if item[0].lower() == name.lower():
                return_bool = True
    return return_bool


def add_to_list(name, amount, d_list):
    for item in d_list:
        if item[0].lower() == name:
            item[1].append(amount)
    return d_list


def display_report(d_list):
    report = 'Name\t\t\tTotal Donation\n'
    for item in d_list:
        report += item[0]
        report += '\t\t\t'
        report += '${:2,.0f}\n'.format(sum(item[1]))
    return report.rstrip()


def send_mail(name, amount):
    email = (
        "Dear {:s},\nThank you for your generous donation of ${:2,.0f}. "
        "We appreciate your thoughtfullness and we will make sure your "
        "dontation goes to the right cause.\nKind Regards,\nDontation Team"
    ).format(name, amount)
    return email


if __name__ == '__main__':
    # get original donation list
    donation_list = create_donation_list()
    response = ''
    response_level = 1

    # level 1
    while response_level >= 1:

        if response_level == 0:
            break

        elif response_level == 1:

            # prompt user for inital response
            response = raw_input(
                'What would you like to do? Enter "TY" for '
                '"Send a Thank You", "CR" for "Create a Report", '
                '"back" to go back, or "quit" to quit: '
            )
            response = response.lower()

            # prompt user to correct entry
            while response not in ['ty', 'cr', 'quit', 'back']:
                response = raw_input('Invalid Entry. Try again: ')
                response = response.lower()

            # set response level
            if response == 'quit':
                response_level = 0
            elif response == 'back':
                response_level = max([response_level - 1, 1])
            else:
                response_level = 2

        elif response_level == 2:

            if response == 'ty':
                response = raw_input('Please enter full name: ')
                response = response.lower()

                if response == 'quit':
                    response_level = 0
                elif response == 'back':
                    response_level = max([response_level - 1, 1])
                elif response == 'list':
                    print list_doners(donation_list)
                    response_level = 2
                    response = 'ty'  # change response to enter if statement
                elif in_list(response, donation_list):
                    response_level = 3
                    donation_name = response
                else:
                    donation_list.append([response, []])
                    response_level = 3
                    donation_name = response

            elif response == 'cr':
                print display_report(donation_list)
                response_level = 1
                response = ''

        elif response_level == 3:

            response = raw_input('Enter donation amount: ')

            # prompt user for correct entry
            while (not response.isdigit()) and (response not in ['quit', 'back']):
                response = raw_input('Invalid Entry. Try Again: ')

            if response == 'quit':
                response_level = 0
                continue
            elif response == 'back':
                response_level = max([response_level - 1, 1])
                response = 'ty'  # change response to enter if statement
                continue

            donation_list = add_to_list(donation_name, int(response), donation_list)
            print send_mail(donation_name, int(response))
            response_level = 1
            response = ''
