#@python: 2
#slicing lab functions

test_string = 'The quick brown fox jumps over the lazy dog'
test_string2 = 'Pack my box with five dozen liquor jugs'
test_string3 = [0, 1, 1, 2, 3, 5, 8, 13]


#first and last characters exchanged
def switcher(t_str):
    return '%s%s%s' %(t_str[-1], t_str[1:-1],t_str[0])


#ever other character
def skipper(t_str):
    return t_str[::2]

#first 4 and last 4 chars removed, every other in between
def hacker(t_str):
    return t_str[4:-4:2]


#reverse a string using slicing
def reverso(t_str):
    return t_str[::-1] #whole string, step/walk backwards

#return middle, last, first thirds of random string
def scrambler(t_str):
    temp = len(t_str)
    front = t_str[0:temp / 3]
    mid = t_str[temp / 3 : 2 * temp / 3]
    last = t_str[2 * temp /3 :]
    return '%s%s%s' %(mid, last, front)

#printing block
print switcher(test_string)
print skipper(test_string3)
print hacker(test_string2)
print reverso(test_string2)
print scrambler(test_string)

