##given an integer n return true when it is  within 10 of 100 or 200


def near_hundred(i):
    temp1 = abs(100 - i)
    temp2 = abs(200 - i)
    if temp1 < 10 or temp2 < 10:
        return True

i = 91
print 'Near Hundred Result:', near_hundred(i)


##pos_neg()

def pos_neg(a, b, negative):
    if {(a > 0 and b < 0) or (a < 0 and b > 0)} and not negative:
        return True
    elif (a < 0 and b < 0) and negative:
        return True
    else:
        return False

a = -3
b = -2
negative = True

print 'Positive Negative Result:', pos_neg(a, b, negative)

#codingbat solution
# def pos_neg(a, b, negative):
#   if negative:
#     return (a < 0 and b < 0)
#   else:
#     return ((a < 0 and b > 0) or (a > 0 and b < 0))