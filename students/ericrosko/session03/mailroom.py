'''
Eric Rosko
Session03
mailroom.py
Tuesday, Nov. 16, 2015

Description:
	Part Session 3 homework

Requirements:
	You must have py.test installed from http://pytest.org
	python3 -m pip install pytest

Usage: 
	py.test -v mailroom.py
	or
	python3 mailroom.py

'''

from operator import *

def send_thank_you(data):
	isNameEntered = False
	while not isNameEntered:
		fullname = input("Enter full name: ")
		if fullname == "list":
			print(get_donor_names(data))
		else:
			isNameEntered=True

	if not is_person_in_database(data,fullname):
		print("User not in database - adding.")
		data[fullname]=[]

	isNumber = False
	while not isNumber:
		amount = input("Enter donation amount: ")
		if verify_number(float(amount)):
			isNumber=True

	add_donation_for_person(data,fullname,float(amount))
	print_thank_you_email(fullname, amount)

def print_thank_you_email(name, amount):
	print("Thank you {} for your generous donation of ${}!".format(name,amount))

def print_report(data):
	
	output=""
	sortedKeys=[]
	results = {}

	for i in data:
		aList=data[i]
		for j in aList:
			total = sum(aList)
			count = len(aList)
			avg = float(total/count)

			results[i] = {'total':total, 'count':count,'average':avg}

	myNewList = sorted(results.items(), key=lambda x: getitem(x[1],'total'))
	myNewList.reverse()

	for item in myNewList:
		output += "Donor:{}\tTotal:{:.2f}\tCount:{}\t\tAverage:{:.2f}\n".format(item[0], item[1]['total'], item[1]['count'],item[1]['average'])
	return output

def verify_number(input):
	if not isinstance(input, (int,float)):
		return False
	return True

def is_person_in_database(database, person):
	if person not in database:
		return False
	return True

def add_donation_for_person(database, person, amount):
	try:
		donations = database[person]
	except KeyError:
		database[person]=[]
		donations = database[person]

	donations.append(amount)

def get_donor_names(data):
	output=''
	# the sort is just to make testing easier
	for name in sorted(data.keys()):
		if len(output) > 0:
			output += ', ' 
		output+=name

	return output

if __name__ == "__main__":
	isRunning=True
	data = dict(one=[1.01], two=[2.01,2.02], three=[3.01,3.02,3.03], four=[.5])
	while isRunning:
		choice = input("""1.) Send thank you\n2.) Create a report\nChoice: """)

		if choice == 'q':
			isRunning=False
		elif choice == '1':
			send_thank_you(data)
		elif choice == '2':
			print(print_report(data))
		else:
			print ("Bad input: {}\n".format(choice))

#############################################################################
# Tests
#############################################################################

def test_get_donor_names_mutliple_names():
	data = dict(a=[], b=[])
	assert get_donor_names(data) == 'a, b'

def test_get_donor_names_one_name():
	data = dict(a=[])
	assert get_donor_names(data) == 'a'

def test_add_donation_for_person():
	data = dict()
	assert is_person_in_database(data,'bob') == False
	add_donation_for_person(data,'bob', 5.00)
	assert is_person_in_database(data,'bob') == True

def test_add_two_donations_for_person():
	data = dict()
	add_donation_for_person(data,'bob', 5.00)
	add_donation_for_person(data,'bob', 6.00)
	t = data['bob']

	assert sum(t) == 11

def test_person_not_in_database():
	data = dict(bob=[1.01])
	assert is_person_in_database(data,'bob') == True

def test_person_not_in_database():
	data = dict(bob=[1.01])
	assert is_person_in_database(data,'ann') == False

def test_verify_number_with_int():
	assert verify_number(5) == True

def test_verify_number_with_float():
	assert verify_number(5.5) == True

def test_verify_number_with_text():
	assert verify_number('hi') == False

def test_print_database():
	data = dict(one=[1.01], two=[2.01,2.02], three=[3.01,3.02,3.03], four=[.5])
	assert print_report(data) == "Donor:three\tTotal:9.06\tCount:3\t\tAverage:3.02\nDonor:two\tTotal:4.03\tCount:2\t\tAverage:2.01\nDonor:one\tTotal:1.01\tCount:1\t\tAverage:1.01\nDonor:four\tTotal:0.50\tCount:1\t\tAverage:0.50\n"

def test_dictionary_add():
	donators = {}
	donators['one']=['1.00']
	assert len(donators) == 1
	atuple = donators.popitem()
	assert atuple[1][0] == '1.00'

def test_dictionary_length():
	donators = dict(one=[1.00])
	assert len(donators) == 1
