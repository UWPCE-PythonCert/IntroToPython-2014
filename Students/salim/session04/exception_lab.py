#!/usr/bin/env python


def safe_input():
    try:
        return raw_input('Type ^c or ^d to raise an error.')
    except (KeyboardInterrupt, EOFError):
        return None

if __name__ == '__main__':
    safe_input()
