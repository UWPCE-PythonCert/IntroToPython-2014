#@python: 2

test_string = 'The quick brown fox jumped over the lazy dog'
test_string2 = 'Relaxing in basins at the end of inlets \
                terminates the endless tests from the box'


def switcher(str):
    return str[-1] + str[1:-1] + str[0]


def skipper(str):
    return str[0:50:2]


ans = skipper(test_string2)
print (ans)

