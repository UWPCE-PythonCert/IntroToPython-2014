'''
Eric Rosko
mailroom.py
Tuesday, Nov. 10, 2015

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

if __name__ == "__main__":
	isRunning=True
	while isRunning:
		choice = input("""1.) Type a current username, or add a new user, type 'r' for report, or 'q' to quit.
		""")

		if choice == 'q':
			isRunning=False
			continue


