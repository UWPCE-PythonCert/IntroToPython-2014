def first_last(x):
    first = x[0]
    last = x[-1]
    middle = x[1:-1]
    print (last+middle+first)

def every_other_rem(x):
    print (x[::2])

def fl_eo(x):
    middle = x[5:-4:2]
    print (middle)

def reverse(x):
    print (x[::-1])

def fst_mid_lst_re(x):
    segment = int(round((len(x)/3),0))
    first = x[:segment]
    middle = x[(segment):(segment*2)]
    last = x[(segment*2):]
    print(middle+last+first)