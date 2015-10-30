#!/usr/bin/env python3


def safe_input():
    try:
        x = input("Enter something: ")
        return x
    except (KeyboardInterrupt, EOFError):
        return None


if __name__ == '__main__':
    safe_input()