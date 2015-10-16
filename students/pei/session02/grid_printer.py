# print ("let's see if this works")
# a = ('+' + '-'*4) * 2 + '+'
# b = ('|' + " "*4) * 2 + '|'
# print ((a + ('\n' + b)*4) + '\n' + (a + ('\n' + b)*4) + '\n' +a)

def mkgrid(k):
    a = ('+' + '-'*(4+k)) * 2 + '+'
    b = ('|' + " "*(4+k)) * 2 + '|'
    print ((a + ('\n' + b)*k) + '\n' + (a + ('\n' + b)*k) + '\n' +a)

def mkgrid2(k, j):
    a = ('+' + '-'*(4 + k)) * k + '+'
    b = ('|' + " "*(4 + k)) * k+ '|'
    #print (a + ('\n'+ b) + '\n')
    print (((a + ('\n'+ b)*k + '\n') * j) + a)

mkgrid2 (2, 4)
mkgrid2(3, 3)
mkgrid2(4, 1)
mkgrid2 (5, 7)


print(mkgrid(3))

print(mkgrid(5))
