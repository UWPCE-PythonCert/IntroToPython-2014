#!/usr/bin/env python

"""
Examples from: http://codingbat.com

Put here so we can write unit tests for them ourselves
"""

# Python > Warmup-1 > sleep_in


def sleep_in(weekday, vacation):
<<<<<<< HEAD
<<<<<<< HEAD
    return not (weekday == True and vacation == False)


=======
    return not (weekday and vacation)
>>>>>>> 280ef895939c277e57ec13a273e99cb3420e860f
=======
    return not (weekday is True and vacation is False)

def monkey_trouble(a_smile, b_smile):
    if a_smile is b_smile:
        return True
    else:
        return False


>>>>>>> ac3fdc60a59913a3b8f9a60b7c4f2ee2b5eb08fe
