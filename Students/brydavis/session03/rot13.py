#!/usr/bin/env python

from sys import argv

s =  argv[1] if len(argv) > 1 else 'Hello World!'

def rot13(s=s):
	hashed = ''

	for i in s:
		hashed += chr(ord(i)+13)

	return hashed


if __name__ == '__main__':

	print 'Testin ROT13 encryption...'
	assert rot13()

	print 'Orignal text: %s' % s
	print 'Encrypted text: %s' % rot13()