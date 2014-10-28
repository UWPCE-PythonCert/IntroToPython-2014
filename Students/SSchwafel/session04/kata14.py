#!/usr/bin/python
import random

#Open the text file for Sherlock Homes

book_file = open('sherlock_small.txt')
text_doc = book_file.read()
book_file.close()

#Divide text_doc into a list

text_doc = text_doc.replace('--',' ')

text_doc = text_doc.replace('.','')
text_doc = text_doc.replace(',','')
text_doc = text_doc.lower()

text_doc = list(text_doc.split())

#print text_doc

new_text = []

dict_words = {}


#for i in text_doc:
def take_first_three_values(x):
    """Takes first three values from text document, turns val.1 into key, second two into a list of items"""
    #grabs first value from text doc, removes it

    word1 = x.pop(0)

    word2 = x[0]

    word3 = x[1]

    #add a dictionary entry for the first three values

    dict_words.setdefault(' '.join((word1, word2)), []).append(word3)

while len(text_doc) > 0:

    try:
        take_first_three_values(text_doc)

    except IndexError:
        break

key = random.choice(dict_words.keys())
print '\n'
print key.capitalize(),
new_text.extend(key.split())


for i in range(200):
    try:

        next_word = random.choice(dict_words[key])
        print next_word,
        new_text.append(next_word)
        key = ' '.join(new_text[-2:])

    except KeyError:
        continue

#new_text.append(str(dict_words[starting_point]))
#new_text.append(str(starting_point.split()[1]))
#next_word = random.choice(dict_words[starting_point])
#
##print new_text
#print ' '.join(map(str, new_text))
#
#print dict_words[starting_point]
#
#
#for i in dict_words.keys():
#    print '\n'
#    print i
#    print dict_words[i]
