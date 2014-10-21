Session 03 notes from class
---------------------------------
Strings
ord () is the ordinal of a string value.  This allows us to quickly alphabetize strings. Cap letters are indexed in front of lower case.

string.index() locates the first instance of a specified string passed to the operator.

string.count() acts as you'd expect it to with the count looking for the argument passed.

raw_input() takes a string that is presented to the user -- this function always returns a string, if you want an integer or float you must cast the value

float()
int()
etc

input() trys to make an intelligent guess as to what type the input is.  This is a bad habit to get into using since it will accept bad inputs and attempt to run them, allowing for reverse injection attacks.

enumerate() will return the index for each value in a list

FLOW CONTROL
break -- terminates loop

continue -- skips everything below the continue line and returns to the top of the loop

else on a "FOR" loop -- else is executed if the loop does not break, e.g. it runs to completion.

enumerate(argument) -- returns both the index and the value for an argument

string.split(argument) -- splits string on argument passed
string.join(argument) -- join list values into a string with argument separators

strings are immutible, so all string operations return a new string.

.isnumeric()
.isalnum()
.isalpha()
etc


ord() translates a character to ordinal value
char() translates values into characters

string.format() -- most current formatting tool, pretty powerful

string function lab
list lab
string formatting lab
homework
