def string_splosion(str):
    new_string = ''
    for i in range(len(str)+1):
        new_string += str[:i]
    return new_string


def cigar_party(cigars, is_weekend):
    if (40 <= cigars <= 60 and not is_weekend) or (cigars >= 40 and is_weekend):
        return True
    else:
        return False


def count_evens(nums):
    return len([num for num in nums if num % 2 == 0])
