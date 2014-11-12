"""
OBJECTIVE:
Look at each set of three adjacent words in a document.
Use the first two words of the set as a key.
The value for each key is a list of words that follow the key.

Initialize with a random set of two words and build

HELP REQUESTS: I ha a really hard time with writing the dict to a file,
ended up using csv module to help me out.  Any advice would be great.

"""

from katafunc import stringbreak, sanitize  # linebreak, bookbreak,
import csv

book = open('sherlock.txt')
book.seek(1289)  # 1289 to skip header in large file

katadict = dict()

book_text = book.read(560492)  # 560491 to capture text of large file

book.close()

temp = book_text.split(' ')
# at this point you have a list of words w\n and punctuation mixed in


for i, word in enumerate(temp):
    if word.find('\n') != -1:
        temp.pop(i)  # entry must be popped or loop hangs up
        temp.insert(i, stringbreak(word, '\n')[0])
        temp.insert(i + 1, stringbreak(word, '\n')[1])


for i, word in enumerate(temp):
    temp[i] = sanitize(word)
    if temp[i] is '':
        temp.pop(i)


while len(temp) > 3:
    n = 0
    word1 = temp[n]  # .lower()
    word2 = temp[n + 1]  # .lower()
    val = temp[n + 2]  # .lower()

    key = '{word1} {word2}'.format(word1=word1, word2=word2)

    if key not in katadict:  # some single word keys are slipping through
        katadict.setdefault(key, [val])

    elif key in katadict:
        templist = katadict.get(key)

        if val not in templist:
            templist.append(val)
            katadict.update({key: templist})

    temp.pop(0)


# write everything to a file to save memory later
f = open('kata_dfile.csv', 'w')

for k, v in katadict.iteritems():
    dline = (k, v)
    spamwriter = csv.writer(f, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow(dline)
f.close()

# crap that didn't work
# csvwriter = csv.DictWriter(f, delimiter= ',', fieldnames= k)
# dline = "{key}: {values},".format(key=k, values=v)
# f.write(dline)

# print to terminal to check functionality
# for k, v in katadict.iteritems():
#     dline = '{key}: {values},\n'.format(key=k, values=v)
#     print dline
