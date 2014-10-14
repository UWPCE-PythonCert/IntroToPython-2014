
def monkey_trouble(a_smile, b_smile):
    if (a_smile and b_smile) or (not a_smile and not b_smile):
        return True
    else:
        return False

a_smile = False
b_smile = True

answer_1 = monkey_trouble(a_smile, b_smile)
print answer_1, a_smile, b_smile

"""
solution notes really short answer:
def more_trouble(a_smile, b_smile)
return (a_smile==b_smile)
"""

def more_trouble(a_smile, b_smile):
    return (a_smile==b_smile)
answer_2=more_trouble(a_smile, b_smile)
print answer_2

