##parrot trouble in paradise


def parrot_trouble(talking, hour):
    if not talking:
        return False
    elif hour < 7 or hour > 20:
        return True
    else:
        return False

talking = True
hour = 8

print parrot_trouble(talking, hour)

"""
def parrot_trouble(talking, hour):
  return (talking and (hour < 7 or hour > 20))
  # Need extra parenthesis around the or clause
  # since and binds more tightly than or.
  # and is like arithmetic *, or is like arithmetic +
"""

#makes 10

def makes10(a, b):
    if a == 10 or b == 10:
        return True
    elif a + b == 10:
        return True
    else:
        return False
a = 5
b = 10
print 'Makes 10:', makes10(a, b)
