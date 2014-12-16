__author__ = 'Robert W. Perkins'

from_file = './test.txt'
to_file = './test/testcopy.txt'

indata = open(from_file).read()
open(to_file, 'w').write(indata)
