strng = (2, 123.4567, 10000)

print ('file_00{} :    {:.2f}, {:.0e}'.format(*strng))

strng2 = (1,2,3,4,5,6)

def arb_tup(*x):
    str_count = len(strng2)
    temp_strng = [str(i) for i in strng2]
    print ('The first {} numbers are: {}'.format(str_count,",".join(temp_strng)))

arb_tup(strng2)ls