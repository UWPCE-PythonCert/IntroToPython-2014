
original = '''
518659005232r583491410442e291745698219m421410443129o162080940635v32416189681e64832
3758660l64832378918a291745692333r648323762540g324161887930e680739944367s22691331914
3t129664756724p486242827755r648323758580i97248568173m486242846295e421410460783
'''

originalParsedText = '''
518659005232
r
583491410442
e
291745698219
m
421410443129
o
162080940635
v
32416189681
e
648323758660
l
64832378918
a
291745692333
r
648323762540
g
324161887930
e
680739944367
s
226913319143
t
129664756724
p
486242827755
r
648323758580
i
97248568173
m
486242846295
e
421410460783
'''


nums = '''
486242831895
551075217947
259329507176
388994275884
129664751092
0
615907574147
32416188601
259329512488
615907584293
291745691343
648323773780
194497138302
97248563157
453826655534
615907594667
64832376454
453826635794
388994273508
'''

#Code posted on Daniwe.com by a moderators named 
def isprime(n):
    '''check if integer n is a prime'''
    # make sure n is a positive integer
    n = abs(int(n))
    # 0 and 1 are not primes
    if n < 2:
        return n, 'False'
    # 2 is the only even prime number
    if n == 2: 
        return 2, 'True'    
    # all other even numbers are not primes
    if not n & 1: 
        return n/2, 'False'
    # range starts with 3 and only needs to go up the squareroot of n
    # for all odd numbers
    for x in range(3, int(n**0.5)+1, 2):
        if n % x == 0:
            return n/x, 'False'
    return n, 'True'
    
def solve():
    '''
    Process a list of numbers and factor out the largest prime number in each.
    Add 65 to the number left and convert to a character
    '''
    
    numbers = nums.split()
    largestPrimesGone = list()

    for line in numbers:
        i = int(line)
        print 'checking', i
        n, prime = isprime(i)
        while prime == 'False' and n > 2:
            print  'was not prime now checking', n
            n, prime = isprime(n)
      
        print 'largest prime is ', n
        if n != 0:
            n = i / n
        print 'new num is ', n
        largestPrimesGone.append(n)
         

    addr = ''
    for line in largestPrimesGone:
        print line
        addr = addr + str(unichr(line+65))

      
    print addr
      
   

    
      
solve()
