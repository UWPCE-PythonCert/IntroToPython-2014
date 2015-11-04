def swap(seq):
    return seq[-1:]+seq[1:-1]+seq[:1]
assert swap('something') == 'gomethins'

def rem(seq):
    return seq[::2]
assert rem('a word') == 'awr'


def rem4(seq):
    return seq[4:-4:2]
assert rem4('0123456789') == '4'


def reverse(seq):
    return seq[::-1]
print(reverse('a string'))


def thirds(seq):
    i = len(seq)//3
    if i%3:
        return seq[i*2:i*3+1] + seq[:i] + seq[i:i*2]
print(thirds(tuple(range(12))))


# sequence test1
sequence = [1,2,3,4,5,6]
test = swap(sequence)
print(test)

#sequence test2
sequence = [1,2,3,4,5,6]
test = rem(sequence)
print(test)

#sequence test3
sequence = [1,2,3,4,5,6,7,8,9,10,11,12]
test = rem4(sequence)
print(test)

#sequence test4
sequence = [1,2,3,4,5,6,7,8,9,10,11,12]
test = reverse(sequence)
print(test)

#sequence test5
sequence = [1,2,3,4,5,6,7,8,9,10,11,12]
test = thirds(sequence)
print(test)

