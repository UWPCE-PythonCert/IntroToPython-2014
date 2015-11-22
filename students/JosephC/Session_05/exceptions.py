#Exceptions Lab for Session 5 of UW Python(Fall)

def safe_input():
	isItSafe = input("Try to enter something non interrupting: ")
	
	if isItSafe == '^C':
		raise KeyboardInterrupt("Error: interrupt character entered.  Try again.")
	elif isItSafe == '^D':
		raise EOFError("Error: End of File character entered.  Try again.")

safe_input()