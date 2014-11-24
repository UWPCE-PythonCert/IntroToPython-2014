#!/usr/bin/env python2.7

# cleans a file of leading and trailing whitespace

import sys

def strip_whitespace(astring):
    """
    Simple function that takes a string as an argument and cleans
    leading and trailing whitespace
    """
    return astring.strip()

readfile = open(sys.argv[1], 'r') # file name to be cleaned
# new file name to write to
newfile = open(raw_input("'(N)ew clean file name' ?> "), 'w')

# lines = []
# for line in readfile:
#     # add each new line in the file to the list
#     lines.append(line)
#     # use a map to clean each element of leading and trailing whitespace
#     cleanlines = map(strip_whitespace, lines)

# This is much cleaner than the above.  Since the file object "readfile"
# is an iterator, we don't need to loop over it like in the above, but 
# do this instead:
cleanlines = map(strip_whitespace, readfile)

# write the cleaned lines to the new file
for line in cleanlines:
    newfile.write(line + "\n")
newfile.close()

