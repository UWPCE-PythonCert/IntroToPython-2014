#!/usr/bin/python

#Open the text file for Sherlock Homes

book_file = open('sherlock_small.txt')
text_doc = book_file.read()
book_file.close()

#Divide text_doc into a list

text_doc = text_doc.replace('--',' ')

print list(text_doc.split())


