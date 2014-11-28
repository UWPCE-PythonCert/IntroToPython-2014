'''
Comprehension lab

Various and sundry comprehensions plus unit testing.

I did all the lab comprehensions and understood them. Not sure if I was supposed to reproduce them here. But decided to do the code_bat problem with testing.

'''

def count_evens (l):
    return len ([num for num in l if num % 2 == 0])

if __name__ == "__main__":
    assert (count_evens([2, 1, 2, 3, 4]) == 3)
    assert (count_evens([2, 2, 0]) == 3)
    assert (count_evens([1, 3, 5]) == 0)