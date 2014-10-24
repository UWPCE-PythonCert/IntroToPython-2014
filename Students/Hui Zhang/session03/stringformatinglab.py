# Method 1: using string format operator
""" Write a format string that will take:

    ( 2, 123.4567, 10000)

    and produce:

    'file_002 :   123.46, 1e+04'
"""

str1 = [2, 123.4567, 10000]
p11 = str("%03d" % str1[0])
p12 = "file_" + p11 + " :"
p13 = "%8.2f" % 123.4567
p14 = "%0.e" % 10000
print p12, p13+",", p14



# Method 2: using format()
""" Write a format string that will take:

    ( 2, 123.4567, 10000)

    and produce:

    'file_002 :   123.46, 1e+04'
"""

str1 = [2, 123.4567, 10000]
"file_{0:03} : {1:>8.2f}, {2:0.0e}".format(2, 123.4567, 10000)