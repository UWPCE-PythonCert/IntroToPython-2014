'''
Write a format string that will take:

    ( 2, 123.4567, 10000)

    and produce:

    'file_002 :   123.46, 1e+04'
'''
#'{:.2f}'.format(123.4567)
#'{:0>3d}'.format (2)
#'{:.0e}'.format(10000)

'file_{:0>3d}, {:.2f}, {:.0e}'.format (2, 123.4567, 10000)
# Rewrite: "the first 3 numbers are: {:d}, {:d}, {:d}".format(1,2,3) 
# to take an arbitrary number of values
t = (1,2,3)
"the first 3 numbers are: {:d}, {:d}, {:d}".format(*t)