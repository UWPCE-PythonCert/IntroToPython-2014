#!/usr/bin/env python


def pos_neg(a, b, negative):
    if negative:
        return a < 0 and b < 0
    else:
        return (a < 0 and b > 0) or (a > 0 and b < 0)

if __name__ == "__main__":
    # run some tests if run as script
    # (from the codingbat site -- not all, I got bored)
    assert pos_neg(1, -1, False) is True
    assert pos_neg(-1, 1, False) is True
    assert pos_neg(-4, -5, True) is True
    assert pos_neg(-4, -5, False) is False
    assert pos_neg(-4, -5, True) is True

    assert pos_neg(-6, -6, False) is False
    assert pos_neg(-2, -1, False) is False
    assert pos_neg(1, 2, False) is False
    assert pos_neg(-5, 6, True) is False
    assert pos_neg(-5, -5, True) is True



    print "all tests passed"
