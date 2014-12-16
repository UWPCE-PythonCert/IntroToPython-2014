#the not string function


def not_string(str):
    if str.find('not') > 0 or str.find('not') == -1:
        return 'not ' + str
    else:
        return str

str = 'not candy bad'
print 'Not string result:', not_string(str)

print str.find('not')

##codingbat solution, note use of double returns since only 1 is executed
# def not_string(str):
#   if len(str) >= 3 and str[:3] == "not":
#     return str
#   return "not " + str
#   # str[:3] goes from the start of the string up to but not
#   # including index 3


def missing_char(str, n):
    return str[:n - 1] + str[n:]
