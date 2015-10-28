def first_and_last(str):
    return str[-1:] + str[1:-1] + str[0:1]
# write tests first before you write function == Test Driven Development
assert first_and_last('radical') == 'ladicar'


def every_other_gone(str):
    return str[::2]

assert every_other_gone('radical') == 'rdcl'


def first_and_last_four_and_every_other(str):
    return str[4:-4:2]

assert first_and_last_four_and_every_other('mississippi') == 'is'


def reversed(str):
    return str[::-1]

assert reversed('mississippi') == 'ippississim'


def rethirded(str):
    third = len(str)//3
    return str[third:-third] + str[-third:] + str[:third]

assert rethirded('beautiful') == 'utifulbea'
