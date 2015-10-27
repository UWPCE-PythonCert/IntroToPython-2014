#Slicing Lab

def sequence1(seq):
#return a sequence with the first and last items exchanged

    print (seq[-1:] + seq[1:-1]+seq[:0])    
   

sequence1('fuck yeah, buddy')

def sequence2(seq):
# return a sequence with every other item removed
    
    print(seq[::2])

   

sequence2('fuck yeah, buddy')


def sequence4(seq):
#return a sequence reversed (just with slicing)
    seq[::-1]

sequence4('something')

def sequence5(seq):
# return a sequence with the middle third, then last third, then the first third in the new order

    i = len(seq) //3
    if 1 % 3:
        print( seq[i*2:i*3+1] + seq[:i] + seq[i:i*3] )

sequence5('fuck yeah, buddy')
