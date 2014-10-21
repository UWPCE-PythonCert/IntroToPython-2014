##make a function that swaps first and last letter of a string


def front_back(str):
    if len(str) > 1:
        first_letter = str[0]
        last_letter = str[len(str) - 1]
        mid_letters = str[1:len(str) - 1]
        return last_letter + mid_letters + first_letter
    else:
        return str

#codingbat solution
# def front_back(str):
#   if len(str) <= 1:
#     return str

#   mid = str[1:len(str)-1]  # can be written as str[1:-1]

#   # last + mid + first
#   return str[len(str)-1] + mid + str[0]


def front3(str):
    if len(str) <= 3:
        return 3 * str
    return 3 * str[0:3]

#codingbat says slicing is silent on indexing errors, not sure aobut this
