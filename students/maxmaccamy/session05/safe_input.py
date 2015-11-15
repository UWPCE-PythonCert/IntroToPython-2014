__author__ = 'Max'

def safeInput():
    try:
        return input()
    except (EOFError, KeyboardInterrupt):
        return None

