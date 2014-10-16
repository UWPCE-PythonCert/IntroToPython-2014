#!/usr/bin/env python


def cigar_party(cigars, is_weekend):
    """
    basic solution
    """
    if is_weekend and cigars >= 40:
            return True
    elif 40 <= cigars <= 60:
        return True
    return False


def cigar_party2(cigars, is_weekend):
    """
    some direct return of bool result
    """
    if is_weekend:
        return (cigars >= 40)
    else:
        return (cigars >= 40 and cigars <= 60)


def cigar_party3(cigars, is_weekend):
    """
    conditional expression
    """
    return (cigars >= 40) if is_weekend else (cigars >= 40 and cigars <= 60)

if __name__ == "__main__":
    # some tests

    assert cigar_party(30, False) is False
    assert cigar_party(50, False) is True
    assert cigar_party(70, True) is True
    assert cigar_party(30, True) is False
    assert cigar_party(50, True) is True
    assert cigar_party(60, False) is True
    assert cigar_party(61, False) is False
    assert cigar_party(40, False) is True
    assert cigar_party(39, False) is False
    assert cigar_party(40, True) is True
    assert cigar_party(39, True) is False

    print "All tests passed"
