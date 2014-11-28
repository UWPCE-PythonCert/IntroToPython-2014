# my fungrid 
n = input('Please input your number:' )
def fungrid():
    for i in range(0, 2):
        print '+' + n*'-' + '+' + n*'-' + '+'
        for m in range(0, n):
            print '|' + n*' ' + '|' + n*' ' + '|'
    print '+' + n*'-' + '+' + n*'-' + '+'
fungrid()