import string


def rot13(str):
    all_the_characters = list(string.ascii_lowercase)
    new_string = ''
    upper = False
    for i in str:
        # preserve capitalization.
        if i.isupper():
            upper = True
            i = i.lower()
        # preserve punctuation
        if i in string.punctuation:
            new_string += i
        # preserve whitespace
        elif i in string.whitespace:
            new_string += i
        else:
            location = all_the_characters.index(i)
            new_location = location - 13
            if new_location < 0:
                new_location = len(all_the_characters) + new_location
            if upper:
                new_string += all_the_characters[new_location].upper()
            else:
                new_string += all_the_characters[new_location]
    return new_string

if __name__ == '__main__':
    # test for a and z
    assert rot13('a') == 'n'
    assert rot13('z') == 'm'
    # preserve spaces and punctuation
    assert rot13(' ') == ' '
    assert rot13('!?#%.,') == '!?#%.,'
    # preserve case
    assert rot13('Aa') == 'Nn'
