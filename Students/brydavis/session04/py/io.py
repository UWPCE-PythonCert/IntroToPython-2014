#!/usr/bin/env python

# FILE LAB
# ==================================================================
# In the class repo, in:
# Examples\Session01\students.txt
# You will find the list I genrated of all the students in the class, and what programming langues they used in the past.
# Write a little script that reads that file, and generates a list of all the languages that have been used.
# Extra credit: keep track of how many sutdents specified each language.
# If you've got it set up right, git pull upstream master should update your repo. Otherwise, you can get it from gitHub:
# https://github.com/UWPCE-PythonCert/IntroToPython/blob/master/Examples/Session01/students.txt

from sys import argv

file_path = argv[1] if len(argv) > 1 else 'students.txt'

def student_langs(file_path=file_path):
	f = open(file_path).readlines()
	lang_set = set()
	lang_dict = {}

	for i in f:
	    start = i.find(':') + 1
	    line = i[start:-1].strip().split(',')

	    for l in line:
	    	l = l.strip().lower()
	    	lang_set.add(l)

	    	if l in lang_dict.keys():
	    		lang_dict[l] += 1
	    	else:
	    		lang_dict[l] = 1

	lang_set.remove('languages')
	lang_set.remove('')

	del lang_dict['']
	del lang_dict['languages']

	# for lang in lang_dict:
	# 	print '%s: %s' % (lang,lang_dict[lang]) 
	# return lang_set == set(lang_dict.keys()) 
	return lang_dict


def histogram(orig_dict,title=' '*10):
	d = orig_dict
	m = max_key_length(d)
	t = '\nHistogram - %s' % title
	g = '=' * len(t) + '=' * 5
	print t
	print g
	for i in d:
		# print i,' '*(m-len(i)), '[]'*d[i], d[i]
		print i,' '*(m-len(i)), '\xe2\x96\xa2 '*d[i], d[i]
	print g
	return
    


def max_key_length(orig_dict):
	d = orig_dict
	m = 0
	for i in d:
		l = len(i)
		if l > m: m = l
	return m


# Paths and File Processing
# ==================================================================
# write a program which prints the full path to all files in the current directory, one per line
# write a program which copies a file from a source, to a destination (without using shutil, or the OS copy command)
# update mailroom from last weeks homework to:
# use dicts where appropriate
# write a full set of letters to everyone to individual files on disk
# see if you can use a dict to switch between the users selections
# Try to use a dict and the .format() method to do the letter as one big template - rather than building up a big string in parts.

import pathlib

def ls(path='./'):
	p = pathlib.Path(path)
	# p.is_dir()
	# p.absolute()
	for f in p.iterdir():
		print pathlib.os.path.abspath(f)







if __name__ == '__main__':
	langs = student_langs()
	histogram(langs,'Student Language Background')


