import string


def rot13(str):
    new_text = []
    a = ord('a')
    z = ord('z')
    for i in str:
        # preserve capitalization.
        upper = False
        if i.isupper():
            upper = True
            i = i.lower()
        # preserve punctuation and whitespace
        if not i.isalpha():
            new_text += i
        else:
            location = ord(i)
            new_location = location - 13
            if new_location < a:
                new_location = (z - (a - 1)) + new_location
            if upper:
                new_text += chr(new_location).upper()
            else:
                new_text += chr(new_location)
    return ''.join(new_text)

if __name__ == '__main__':
    # test for a and z
    assert rot13('a') == 'n'
    assert rot13('z') == 'm'
    # preserve spaces and punctuation
    assert rot13(' ') == ' '
    assert rot13('!?#%.,') == '!?#%.,'
    # preserve case
    assert rot13('Aa') == 'Nn'
