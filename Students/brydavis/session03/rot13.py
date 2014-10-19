#!/usr/bin/env python

from sys import argv


s = argv[1] if len(argv) > 1 else 'Hello World!'
a = int(argv[2]) if len(argv) > 2 else 13


def rot13(s=s,a=a):
	hashed = ''

	for i in s:
		c = ord(i)+a
		# print c
		hashed += chr(c) if c < 256 else chr(c - 255)

	return hashed


def decrypt (s=s,a=a):
	hashed = ''

	for i in s:
		c = ord(i)-a
		# print c
		hashed += chr(c) if c > -1 else chr(c + 255)

	return hashed

def try_all_decrypt1(s=s):
	
	for n in range(256):
		hashed = ''

		for i in s:
			c = ord(i)-n
			hashed += chr(c) if c > -1 else chr(c + 255)
	
		print n, hashed


def try_all_decrypt2(s=s):
	
	for n in range(256):
		hashed = ''

		for i in s:
			c = ord(i)+n
			hashed += chr(c) if c < 256 else chr(c - 255)
	
		print n, hashed




if __name__ == '__main__':

	print 'Testin ROT13 encryption...\n'
	assert rot13()
	assert decrypt()

	h = rot13()

	print 'Orignal text: %s' % s
	print 'Encrypted hash: %s' % h
	print 'Decrypted hash: %s' % decrypt(h)