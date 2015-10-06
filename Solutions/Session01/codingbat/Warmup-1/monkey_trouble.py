#!/usr/bin/env python

#############################
# Warmup-1 > monkey_trouble


def monkey_trouble(a_smile, b_smile):
    """
    really simple solution
    """
    if a_smile and b_smile:
        return True
    elif not a_smile and not b_smile:
        return True
    else:
        return False


def monkey_trouble2(a_smile, b_smile):
    """
    slightly more sophisticated
    """
    if a_smile and b_smile or not (a_smile or b_smile):
        return True
    else:
        return False


def monkey_trouble3(a_smile, b_smile):
    """
    conditional expression -- kind of ugly in this case
    """
    result = True if (a_smile and b_smile or not (a_smile or b_smile)) else False
    return result


def monkey_trouble4(a_smile, b_smile):
    """
    direct return of boolean result
    """
    return a_smile and b_smile or not (a_smile or b_smile)

if __name__ == "__main__":
    # a few tests

    # neat trick to test all versions:
    for test_fun in (monkey_trouble,
                     monkey_trouble2,
                     monkey_trouble3,
                     monkey_trouble4):
        assert test_fun(True, True) is True
        assert test_fun(False, False) is True
        assert test_fun(True, False) is False
        assert test_fun(False, True) is False

    print("All tests passed")
