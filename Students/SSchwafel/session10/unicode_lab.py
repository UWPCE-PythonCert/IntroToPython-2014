#!/usr/bin/python

file = open('/home/schuyler/PythonFolder/session10/ICanEatGlass.utf81.txt', 'rw')

unicode_string = u'bananas'.encode('utf-8')

unicode_chess_piece = u'\u2654'

unicode_chess_piece = unicode_chess_piece.encode('utf-8')

print unicode_chess_piece

#print unicode_string

print file.read()

file.write(unicode_chess_piece)

print file.read()

file.close()
