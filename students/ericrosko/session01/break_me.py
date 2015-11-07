
#type error
def makeTypeError():
	pass
	print ("hello" + 5)

# /Users/erosko/Desktop/python/IntroPython2015/students/ericrosko/session01/break_me.py in <module>()
#       1 
#       2 #type error
# ----> 3 print ("hello" + world)
#       4 #----------------------------------------------
#       5 

# NameError: name 'world' is not defined
def makeNameError():
	print(thisIsNotDefined)
# /Users/erosko/Desktop/python/IntroPython2015/students/ericrosko/session01/break_me.py in makeNameError()
#      14 # NameError: name 'world' is not defined
#      15 def makeNameError():
# ---> 16         print(thisIsNotDefined)
#      17 
#      18 def makeKeyError():
#
#NameError: name 'thisIsNotDefined' is not defined

def makeKeyError():
	myDict = {0:0,0:0}
	myDict["0"]
# /Users/erosko/Desktop/python/IntroPython2015/students/ericrosko/session01/break_me.py in makeKeyError()
#      18 def makeKeyError():
#      19         myDict = {0:0,0:0}
# ---> 20         myDict["0"]
#      21 
#      22 #makeTypeError()
#
# KeyError: '0'


#def makeSyntaxError():
#	print("asdf
#SyntaxError: EOL while scanning string literal

def makeAttributeError():
	"asdf".fakemethod()
# /Users/erosko/Desktop/python/IntroPython2015/students/ericrosko/session01/break_me.py in makeAttributeError()
#      42 
#      43 def makeAttributeError():
# ---> 44         "asdf".fakemethod()
#      45 
#      46 #makeTypeError()

# AttributeError: 'str' object has no attribute 'fakemethod'

#makeTypeError()
#makeNameError()
#makeKeyError()
#makeAttributeError()
#raise Exception

options = { 0 : makeTypeError,
			1 : makeNameError,
			2 : makeKeyError,
			3 : makeAttributeError}

		

def main():
	while True:
		user_input = input("""\n (q to quit): 
			0.) makeTypeError
			1.) makeNameError
			2.) makeKeyError
			3.) makeAttributeError
			Note: For a syntax error, the py file won't even compile.
			""")
		if user_input == 'q':
			break;
		print("input is: + user_input")
		options[int(user_input)]()

main()
