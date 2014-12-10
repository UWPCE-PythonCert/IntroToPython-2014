###Session 10: Unicode, Persistence  
* utf-8 is a superset of ANSI
* utf-16 is not

codec module
encode -> from utf to string (bytes)
decode -> string (bytes) to utf

Declaring you car coding in unicode:  
    # -*- coding: utf-8 -*-

Escaping unicode characters:

print u'the integral sign: \u222b'
print u'the integral sign: \N{integral}'

inamidst.com/stuff/unidata

Python has a default encoding that is usually in ascii

    sys.getdefaultencoding()

Use unicode object in all your code: decode on input encode on output.

Python makes using unicode easy:

    from __future__ import unicode_literals
    # this will apply the assumed 'u' in front of every string
    s = 'this is now a unicode string'
    type(s)

python 3 has all strings in unicode

The big 4 for encoding:  
* utf-8 (*nix)
* utf-16
* ASCII
* Latin-1 (1 byte is 1 character, no decoding errors but may return garbage)

Unicode code points are the same as ASCII for the first 127 characters

File names and that sort of thing should be passed to python in unicode. If you pass unicode python will return unicode, pass a ascii string and you will get your results in the same format

Don't call decode on a unicode object





