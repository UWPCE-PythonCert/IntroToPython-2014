__author__ = 'Robert W. Perkins'

import pathlib

pth = pathlib.Path('./')
for f in pth.iterdir():
    print '%s\%s' % (pth.absolute(), f)
