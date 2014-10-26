"""
Write a little script that:
    Reads that file
    Generates a list of all the languages that have been used.
    Extra credit: keep track of how many times each language is used.

    There has to be some better way than what is on lines 20/21
"""

f = open('students.txt', 'r')
f.readline()  # throw out header

lang_dict = dict()

while True:
    line = f.readline()
    if not line:
        break

    temp = line.split(':')
    temp = temp[1].split(',')

    for l in temp:
        # print l
        l = l.strip(' \n')
        lang_count = lang_dict.get(l, 'new')
        if lang_count is 'new':
            lang_dict.setdefault(l, 1)
        else:
            lang_count += 1
            lang_dict.update({l: lang_count})
f.close()

lang_dict.pop('')
print_list = lang_dict.items()


def plist(ltup):
    return ltup[1]

print_list.sort(key=plist, reverse=True)

print 'List of language sorted by popularity:'

for lang, n in print_list:
    print '{lang}: {n}'.format(lang=lang, n=n)
