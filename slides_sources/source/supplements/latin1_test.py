#!/usr/bin/env python

"""
An example of using latin-1 as a universal encoding

latin-1 is a superset of ASCII that is suitable for western european languages.

Is the most common, and a good default, if you need a one-byte per char encoding
for European text.

It also has a nice property:
   : every byte value from 0 to 255 is avalid charactor

Thus you will never get an UnicodeDecodeError if
you try to decode arbitrary bytes with latin-1.

And it can "round-trip" trhough a unicode object.

This can be useful is you don't know the encoding -- at least it won't break.
It's also useful if you need to work with cobined text+binary data.



"""

# all the byte values in a bytes (str) object:
all_bytes = ''.join( [chr(i) for i in range(255)] )

print type(all_bytes)
print len(all_bytes)

print "Example value: 20"
print ord(all_bytes[20]) == 20
print "Example high value: 245"
print ord(all_bytes[245]) == 245

# now decode it to a unicode object:
try:
    uni = all_bytes.decode()
except UnicodeDecodeError:
    print "OOPS: can't decode with default encoding"

# latin-1 works:
try:
    all_uni = all_bytes.decode('latin-1')
    print "Yup -- that worked"
    print all_uni
    print "note that the ASCII subset is the same..."
except UnicodeDecodeError:
    print "OOPS: This should have worked!!"
    raise

## now show that it round-trips:
all_bytes2 = all_uni.encode('latin-1')

if all_bytes2 == all_bytes:
    print "yup -- that worked...the values are preserved on the round trip."
else:
    print "Hey, that should have worked"







