#!/usr/bin/python3
'''
Copy any file of any length

file_copy source destination
'''

import sys

if len(sys.argv) == 3:
    source, destination = sys.argv[1:3]
    with open(source, 'rb') as s:
        with open(destination, 'wb') as d:
            while True:
                buf = s.read(1024)
                if len(buf) == 0:
                    break
                d.write(buf)
else:
    print('Usage: file_copy <source> <destination>')
