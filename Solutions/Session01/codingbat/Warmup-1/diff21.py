#!/usr/bin/env python


def diff21(n):
    """
    basic solution
    """
    if n > 21:
        return 2 * (n - 21)
    else:
        return 21 - n


def diff21b(n):
    """
    direct return of conditional expression
    """
    return 2 * (n - 21) if n > 21 else 21 - n

if __name__ == "__main__":
    # needs
    print(diff21(3))
    print(diff21b(3))
