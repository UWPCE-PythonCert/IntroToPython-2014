#!/usr/bin/python

#Open the text file for Sherlock Homes

book_file = open('sherlock_small.txt')
text_doc = book_file.read()
book_file.close()

#Divide text_doc into a list

text_doc = text_doc.replace('--',' ')

text_doc = list(text_doc.split())

print text_doc

dict_words = {}


#for i in text_doc:

def take_first_three_values(x):
    """Takes first three values from text document, turns val.1 into key, second two into a list of items"""
    #grabs first value from text doc, removes it
    key = x.pop(0)
    #first value has now switched to second word, removes that one too

    word1 = x.pop(0)
    #first value has now switched to third word, removes that one too

    word2 = x.pop(0)

    #add a dictionary entry for the first three values
    dict_words[key] = [word1,word2]

take_first_three_values(text_doc)

print '\n'
print "Here's the dictionary entry list so far:\n"
print dict_words
print "Here's the original entry list with values removed:\n"    
print text_doc
