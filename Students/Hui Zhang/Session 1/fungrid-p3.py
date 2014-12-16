# my fungrid
n = input('Please input your number:' )
def fungrid():
    for i in range(0, 3):
        print '+' + n*'-' + '+' + n*'-' + '+' + n*'-' + '+'
        for m in range(0, n):
            print '|' + n*' ' + '|' + n*' ' + '|' + n*' ' + '|'
    print '+' + n*'-' + '+' + n*'-' + '+' + n*'-' + '+'
fungrid()