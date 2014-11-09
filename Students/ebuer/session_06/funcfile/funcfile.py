# coding: utf-8
"""
Write a program that takes a filename and “cleans” the file by removing all the leading and trailing whitespace from each line.
    Read in the original file and write out a new one, either creating a new file or overwriting the existing one.
    Give your user the option of which to perform.
    Use map() to do the work.
    Write a second version using a comprehension.

    Use sys.argv to hold the command line arguments the user typed in.
    If the user types: $ python the_script a_file_name then:
        import sys
        filename = sys.argv[1]
        will get filename == "a_file_name"
"""

from io import open, StringIO
import sys

# Read in the original file and return contents
def gettext(infile):  # ='junkfile.txt'
    fid = StringIO()
    with open(infile, 'r', encoding='UTF-8') as f:
        fid = f.readlines()
        return fid

# Apply map lambda function to clean the text
def spstrip(fid):
    return map(lambda x: x.strip(' \n'), fid)

# use a list comprehension instead of the map function
def compstrip(fid):
    return [x.strip(' \n') for x in fid]

# print a new file
def pttext(outfile, intext):
    with open(outfile, 'w', encoding='UTF-8') as f:
        [f.write(u'{line}\n'.format(line=l)) for l in intext]


# Putting together the functions into a script
fid = sys.argv[1]  # note that argv does not count 'python' at prompt
filetext = gettext(fid)
cleantext = spstrip(filetext)
# cleantext = compstrip(filetext)

handle = raw_input('Overwrite existing? Enter Y/N ')

if handle is "Y" or handle is 'y':
    pttext(fid, cleantext)
elif handle is "N" or handle is 'n':
    fname = fid.split('.')
    pttext("_".join([fname[0], 'clean.txt']), cleantext)
else:
    print 'Sorry, that is not possible'
