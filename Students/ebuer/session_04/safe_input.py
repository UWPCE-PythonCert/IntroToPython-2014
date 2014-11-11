"""
Create wrapper function for raw_input that returns none when ^C or ^D
are entered at the prompt.
"""


def safe_input():
    """
    Returns raw_input that is not EOF or KeyboardInterrupt.

    Syntax: safe_input()
    """
    try:
        ri_value = raw_input('Enter value: ')
    except (EOFError, KeyboardInterrupt):
        return None
    else:
        print 'Input Accepted.'
        return ri_value

