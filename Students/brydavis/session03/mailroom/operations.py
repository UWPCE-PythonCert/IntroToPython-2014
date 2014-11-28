#!/usr/bin/env python

from donor_db import donor_list 
from globes import *


def request_donor():
	global donor_list
	donor = raw_input(ask_donor_name)
	
	def verify_donor(donor,donor_list):
		
		is_donor = donor_list.has_key(donor)
		print 'Is %s a donor?' % donor, is_donor
		if is_donor:
			print 'Donations amounts: ', donor_list[donor]
		else:
			# print 'Try again\n'
			print 'Adding donor to database\n'
			donor_list[donor] = []
		
		return is_donor

	def list_donors():
		print '\nList of Donors\n=========='
		for d in donor_list:
			print d
		print '\n'
		return

	if donor == 'list': 
		list_donors()
		return request_donor()
	elif verify_donor(donor,donor_list):
		return donor
	else:
		return request_donor()


def create_report():
	donor = request_donor()			
	donations = donor_list[donor]
	printout = ''
	
	printout += 'Donor Report\n'
	printout += 'Name: %s' % donor
	printout += '\nList of Donations (%d):' % len(donations)
	
	for i, d in enumerate(donations, start=1):
		printout += '\n\td%d: $%d' % (i,d)  
	
	# return True
	return ask_again(printout)

		
def send_letter():
	donor = request_donor()			
 	printout = 'Sending %s a \'Thank You\' Letter' % donor
	# return True

	# TODO: COMPSE AND SEND email
	return ask_again(printout)

def add_donation():
	global donor_list
	donor = request_donor()

 	def verify_donation():
		donation = int(raw_input('\nHow much would %s like to donate? ' % donor))			
		donation_verified = (raw_input('\nPlease confirm a $%d donation from %s? (Yes / No / Cancel) \n' % (donation, donor))).lower()			

	 	if donation_verified ==  'yes':
	 		donor_list[donor].append(donation)
		 	printout = 'Success! %s has just donated $%d.' % (donor, donation)	
			return ask_again(printout)

	 	elif donation_verified ==  'cancel': 
	 		printout = 'A donation in the amount of $%d has been cancelled.' % donation	
			return ask_again(printout)
		else:
			verify_donation()

 	return verify_donation()


def ask_again(msg=''):
	print '\n'*30, msg
	return user_action(int(raw_input(menu_options)))

def exit_program():
	print '%s\n' % exit_msg 
	return None

def user_action(ai=0):
	if ai == 1:
		add_donation() 	
	elif ai == 2:
		create_report() 
	elif ai == 3:
		send_letter()
	elif ai == 4:
		exit_program()
	else:
		ask_again()


def init():
	# intro()
	# user_action() if action_input > 0 else None
	print '\n'*30
	user_action()


# def assert_testing():
# 	assert user_action()

# def intro():
# 	global possible_donor
# 	global action_input
# 	# possible_donor = raw_input('Search donor names: ')
# 	# action_input = int(raw_input('\nTask Options\n1) Create a Donor Report\n2) Send a \'Thank You\' Letter\n\nEnter your selection: '))


# if __name__ == '__main__':
# 	# assertion testing
# 	# assert_testing()

# 	# program execution
# 	init()
