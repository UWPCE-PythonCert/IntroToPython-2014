# rot13.py

def rot13(str1):
    str2 = ''
    for i in (range(len(str1))):
        if str1[i] in 'abcdefghijklm' or str1[i] in 'ABCDEFGHIJKLM':
            str2 += chr(ord(str1[i]) + 13)
        elif str1[i] in 'nopqrstuvwxyz' or str1[i] in 'NOPQRSTUVWXYZ':
            str2 += chr(ord(str1[i]) - 13)
        else:
            str2 += str1[i]

    return str2

if __name__ == '__main__':
    a = rot13('Hello there!')
    print(a)

    b = rot13('I am the walrus!')
    print(b)

    c = rot13('Zntargvp sebz bhgfvqr arne pbeare')
    print(c)
