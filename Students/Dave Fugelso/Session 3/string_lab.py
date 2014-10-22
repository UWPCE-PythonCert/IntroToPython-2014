'''
Rewrite: the first 3 numbers are: %i, %i, %i"%(1,2,3)

for an arbitrary number of numbers...

Write a format string that will take:

( 2, 123.4567, 10000)

and produce:

'file_002 :   123.46, 1e+04'

Then do these with the format() method...

'''

if __name__ == "__main__":
    print '%i, %i, %i'%(1,2,3)
    
    arbitraryNumberOfNumbers = (1,2,3,4,5,6,7)
    formatString = '%i, ' * len(arbitraryNumberOfNumbers)
    formatString = formatString[0:len(formatString)-2]
    print formatString%arbitraryNumberOfNumbers
    
    formatString = 'file_%03i : %f %.0e'
    print formatString%( 2, 123.4567, 10000)
    
    # With format
    
    print '{0} {1} {2}'.format (1, 2, 3)
    print '{} {} {}'.format (1, 2, 3)
    
    formatString = '{}, ' * len(arbitraryNumberOfNumbers)
    formatString = formatString[0:len(formatString)-2]
    print formatString.format(*arbitraryNumberOfNumbers)  
    
    
    print 'file_:{0:03d} : {1:f} {2:.0e}'.format( 2, 123.4567, 10000)
 
 