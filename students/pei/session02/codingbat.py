#warmup 1
def sleep_in(weekday, vacation):
    return (not weekday) or vacation

def monkey_trouble(a_smile, b_smile):
    return (a_smile) == (b_smile)
# quick tests
print (monkey_trouble(True, True))
print (monkey_trouble(True, False))
print (monkey_trouble(False, False))

def sum_double (a, b):
    if a !=b:
        return (a+b)
    else: 
        return 2 * (a+b)

# quick tests
print (sum_double(2, 2))
print (sum_double (2, 3))

def not_string(str):
    if str [:3]== "not":
        return str
    else: 
        return "not " + str

# quick tests
print (not_string('candy'))
print (not_string('not candy'))

def missing_char(str, n):
    return str [ : n] + str [ n+1: ]

#test
print(missing_char('kitten', 1))
print(missing_char('kitten', 0))
print(missing_char('kitten', 4))

def front_back(str):
    if len(str) <=1:
        return str
    else:   
        return str [-1] + str [1: (len(str) -1)] + str [0]

def front3(str):
    if len(str) <3:
        return str*3
    else:
        return str[:3]*3