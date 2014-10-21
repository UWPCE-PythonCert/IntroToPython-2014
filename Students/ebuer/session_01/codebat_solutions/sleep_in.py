"""
Written by EB, 2014-10-01
create a function that takes two variables and runs logical eval

sleep in when it is not a weekday, or you are on vacation
do not sleep in on a weekday that is not vacation
"""


def sleep_in(weekday, vacation):
    if not weekday or vacation:
        return True
    else:
        return False

weekday = False
vacation = True

result = sleep_in(weekday, vacation)

print result
