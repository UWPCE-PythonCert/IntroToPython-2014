"""
plusminus = '+ - - - - + - - - - +'
lines = '|         |         |'

print (plusminus)
print (lines)
print (lines)
print (lines)
print (lines)
print (plusminus)
print (lines)
print (lines)
print (lines)
print (lines)
print (plusminus)
"""

def make_grid()
	plusminus = '+ - - - - + - - - - +'
	lines = '|         |         |'
	return plusminus + '\n' + lines * 4 + "\n" + plusminus

