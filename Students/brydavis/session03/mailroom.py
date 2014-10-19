#!/usr/bin/env python

from donor_db import donor_list 

menu_options = '\nMailroom Menu Options\n1) Create a Donor Report\n2) Send a \'Thank You\' Letter\n3) Exit Program\n\nEnter your selection: '
ask_donor_name = 'Enter donor\'s full name or type \'list\':\n'
possible_donor = ''
action_input = 0

# # Uncomment this section to enable CLI input
# from sys import argv
# possible_donor = argv[1] if len(argv) > 1 else 'Dummy Smith'
# action_input = int(argv[2]) if len(argv) > 2 else 0


def user_action(ai=action_input):


	def request_donor():
		return raw_input(ask_donor_name)

	def list_donors():
		print '\nList of Donors\n=========='
		for d in donor_list:
			print d
		print '\n'
		return

	def create_report():


		donor = request_donor()			
		donation_list = donor_list[donor]
		
		if donor == 'list': 
			list_donors()
			return create_report()
		elif check_donor(donor):
			print 'Creating report...\n'
			print 'Donor: %s' % donor
			print 'List of donations (d#):'
			for i, donation in enumerate(donation_list, start=1):
				print 'd%d: ' % i, '$%d' % donation  
			return True
		else:
			return create_report()

		
		
	def send_letter(donor=''):

		def request_donor():
			return raw_input(ask_donor_name)

		def list_donors():
			print '\nList of Donors\n=========='
			for d in donor_list:
				print d
			print '\n'
			return

		donor = request_donor()

		if donor == 'list': 
			list_donors()
			return send_letter()
		elif check_donor(donor):
		 	print 'Sending %s a \'Thank You\' Letter' % donor
			return True
		else:
			return send_letter()

		return

	def ask_again():
		aa = raw_input(menu_options)
		user_action(int(aa))

	def check_donor(donor=possible_donor,dlist=donor_list):
		is_donor = dlist.has_key(donor)
		print 'Is %s a donor?' % donor, is_donor
		print 'Donations amounts: ', dlist[donor], '\n' if is_donor else []
		return is_donor

	def exit_program():
		print '\nExiting Mailroom Program\nGoodbye\n'
		 

	report_status = create_report() if ai == 1 else False
	letter_status = send_letter() if ai == 2 else False
	ask_again() if not report_status and not letter_status else None 


	# donor_verified = check_donor if not possible_donor else 

	return


def init():
	# intro()
	# user_action() if action_input > 0 else None
	user_action()


# def assert_testing():
# 	assert user_action()

# def intro():
# 	global possible_donor
# 	global action_input
# 	# possible_donor = raw_input('Search donor names: ')
# 	# action_input = int(raw_input('\nTask Options\n1) Create a Donor Report\n2) Send a \'Thank You\' Letter\n\nEnter your selection: '))


if __name__ == '__main__':
	# assertion testing
	# assert_testing()

	# program execution
	init()

