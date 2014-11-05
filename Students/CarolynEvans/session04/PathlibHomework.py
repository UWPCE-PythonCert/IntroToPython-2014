
def printFullPath():
    import pathlib

    p = pathlib.Path('.')

    for f in p.iterdir():
        print f.absolute()


def copyFile(filename):
    outfile = 'copyof_' + filename
    o = open(outfile, 'w')
    for line in open(filename):
        o.write(line)
    o.close

copyFile('sherlock.txt')








