
def string_times(str, n):
    return n * str

def front_times(str, n):
    front_end=str[:3]
    return n * front_end

def string_bits(str):
    copier = True
    print_string = ''
    for l in str:
        if copier:
            print_string += l
            print print_string
            copier = False
        else:
            copier = True
    return print_string

str=''
print string_bits(str)

def string_splosion(str):
    print_string=''
    for n in range(len(str)):
        temp = str[0:n+1]
        #print_string += temp
        print print_string
    return print_string

str='Code'
string_splosion(str)

def last2(str):
    end_string = str[-2:]
    i = 0
    for n in range(len(str)-2):
        if str[n:n+2] == end_string:
            i += 1
    return i

def count9(nums):
    i = 0
    for n in nums:
        if n == 9:
            i += 1
    return i
