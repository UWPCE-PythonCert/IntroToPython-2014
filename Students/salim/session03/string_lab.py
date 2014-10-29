#!/usr/bin/env python

# print numbers
numbers = [1, 4, 83, 321, -56, 88]
print 'The first 3 numbers are: %i, %i, %i' % tuple(numbers[:3])

# use format()

# automatic field numbering
print 'file_{:=03} :   {:10.2f}, {:10.0e}'.format(2, 123.4567, 10000)

# positional field numbering
print 'file_{0:=03} :   {1:10.2f}, {2:10.0e}'.format(2, 123.4567, 10000)


# use % notation

# automatic field numbering
print 'file_%03d:   %10.2f, %10.0e' % (2, 123.4567, 10000)
