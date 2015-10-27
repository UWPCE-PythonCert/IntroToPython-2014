#! /usr/bin/env python3

import codecs

decrypt = "Zntargvp sebz bhgfvqr arne pbeare"
decrypt2 = "Tehzcl jvmneqf znxr gbkvp oerj sbe gur rivy Dhrra naq Wnpx."

def rot13(string):
    d = codecs.decode(string, 'rot13')
    return d
        
        
if __name__ == "__main__":
    assert rot13(decrypt) == "Magnetic from outside near corner"
    assert rot13(decrypt2) == "Grumpy wizards make toxic brew for the evil Queen and Jack."
    print('tests passed')
