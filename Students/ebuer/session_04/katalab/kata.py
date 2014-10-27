"""
OBJECTIVE:
Look at each set of three adjacent words in a document.
Use the first two words of the set as a key.
The value for each key is a list of words that follow the key.

Initialize with a random set of two words and build

HELP REQUESTS:

"""

from katafunc import linebreak, bookbreak, stringbreak, sanitize

book = open('sherlock.txt')
book.seek(1289)

katadict = dict()

book_text = book.read(500000)

temp = book_text.split(' ')
# at this point you have a list of words w\n mixed in

for word in temp:
    if word.find('\n') != -1:
        i = temp.index(word) # assume \n mashups are unique
        temp.pop(i)
        temp.insert(i, stringbreak(word, '\n')[0])
        temp.insert(i+1, stringbreak(word, '\n')[1])

# print temp

while len(temp) > 3:
    val = sanitize(temp[2].lower())
    key = '{word1} {word2}'\
        .format(word1=sanitize(temp[0].lower()),
            word2=sanitize(temp[1].lower()))

    if key not in katadict:
        katadict.setdefault(key, [val])

    elif key in katadict:
        templist = katadict.get(key)

        if val not in templist:
            templist.append(val)
            katadict.update({key: templist})

    temp.pop(0)

for k, v in katadict.iteritems():
    print '{key}: {values}'.format(key=k, values=v)
