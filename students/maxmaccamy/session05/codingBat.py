__author__ = 'Max'

def cigar_party(cigars, is_weekend):
    return ((cigars >= 40) and (cigars <= 60)) or ((cigars > 60) and is_weekend)

def count_evens(nums):
    """
    :param nums: list containing integers
    :return: number of evens contained in list
    """
    count = 0
    for numbers in list(nums):
        if (0 == numbers % 2):
            count += 1
    return count

if __name__ == '__main__':
    assert (1 == count_evens([1, 2]))
    assert (2 == count_evens([1, 2]))