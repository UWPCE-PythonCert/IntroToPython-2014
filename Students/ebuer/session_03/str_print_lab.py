#String formatting lab

#create a function that prints in integer format for
#an arbitary number of ints or other values
test_list = [1, 3, 5, 7, 13, 17, 23, 29.5]

def intprinter(L=[0,1,2,3]):
    n = len(L)
    ni = []
    for i in L:
        ni.append(int(i))
    temp=str(ni).lstrip('[').rstrip(']')
    print 'The first %i numbers are %s' %(n, temp)

intprinter(test_list)


#write a formatting string to transform the provided inputs
lab_inp = (2, 123.4567, 10000) #it's a tuple!

#using old formatting
print 'file_00%i, %.2f, %.3e' %(lab_inp[0], lab_inp[1], lab_inp[2])

#using .format
newstring = 'file_00{a:d}, {b:.2f}, {c:.0e}'\
    .format(a=lab_inp[0], b = lab_inp[1], c = lab_inp[2] )

print 'your formatted string: %s' %newstring

