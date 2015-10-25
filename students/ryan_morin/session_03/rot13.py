def rot13(input_strng):
    rotted = ''
    for i in input_strng:
        ch = ord(i)
        if ch >= ord('a') and ch <= ord('z'):
            if ch > ord('m'):
                ch -= 13
            else:
                ch += 13
        elif ch >= ord('A') and ch <= ord('Z'):
            if ch > ord('M'):
                ch -= 13
            else:
                ch += 13
        rotted += chr(ch)
    return rotted

if __name__ == '__main__':
    assert rot13(rot13('ryan was here 2day')) == "ryan was here 2day"
    assert (rot13("Zntargvp sebz bhgfvqr arne pbeare")) == "Magnetic from outside near corner"