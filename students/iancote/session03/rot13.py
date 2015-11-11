import codecs

def rot13(x):
    return codecs.encode(x, 'rot13')


if __name__ == '__main__':
    assert rot13('abcde') == 'nopqr'
    assert rot13('xyzabc') == 'klmnop'
    assert rot13(rot13('qwerty')) == 'qwerty'

    print("rot13('Zntargvp sebz bhgfvqr arne pbeare')): ")
    print(rot13('Zntargvp sebz bhgfvqr arne pbeare'))
