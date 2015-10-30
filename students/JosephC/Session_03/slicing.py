#Slicing Lab

def sequence1(seq):
#return a sequence with the first and last items exchanged
    seq = str(seq)
    print (seq[-1:] + seq[1:-1]+seq[:1])    
   

sequence1('fuck yeah, buddy')


def sequence2(seq):
# return a sequence with every other item removed
    seq = str(seq)
    print(seq[::2])

   
sequence2('oh my')

#   return a sequence with the first and last 4 items removed, and every other item in between
def sequence3(seq):
    
    seq = str(seq)
    print("Here is your string: " , seq[1:len(str(seq))-5:2])

sequence3(123456789)


#return a sequence reversed (just with slicing)
def sequence4(seq):
 
    seq = str(seq)    
    print(seq[::-1])

sequence4('something')

def sequence5(seq):
# return a sequence with the middle third, then last third, then the first third in the new order
    seq = str(seq)
    i = len(seq) //3
    if 1 % 3:
        print( seq[i*2:i*3+1] + ' ' + seq[:i] + ' ' + seq[i:i*3] )

sequence5('abc')
