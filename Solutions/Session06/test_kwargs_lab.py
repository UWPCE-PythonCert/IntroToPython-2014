#!/usr/bin/env python3

"""
Test code for the args-kwargs lab

This kind of experimental code isn't all the suited to testing, but it's
not a bad way to run code as you develop it anyway...

And we want to encourage test code -- so we'll use it everywhere possible

Note: I decided that instead of having my funciton print somthing it would
return a string -- that way I could test that the returned string was correct.

"""

import pytest  # used for testing exceptions

from kwargs_lab import colors, call_colors, colors_manual


# Calling "colors" in various ways.
def test_all_positional():
    result = colors('red', 'blue', 'yellow', 'chartreuse')

    # these aren't exhaustive by any means
    # but mostly I want to make the code runs without error
    print(result)
    assert 'red' in result
    assert 'blue' in result
    assert 'chartreuse' in result
    # you can force a test failure if you want to see the output
    # assert False


def test_one_keyword():
    result = colors(link_color='purple')
    # these aren't exhaustive by any means
    # but mostly I want to make the code runs without error
    print(result)
    assert 'link: purple' in result
    # you can force a test failure if you want to see the output
    # assert False


def test_pos_and_keyword():
    result = colors('yellow', 'gray', link_color='purple')
    # these aren't exhaustive by any means

    print(result)
    assert 'foreground: yellow' in result
    assert 'background: gray' in result
    assert 'link: purple' in result
    # you can force a test failure if you want to see the output
    # assert False


def test_duplicate():
    """
    It's an error to have a keyword argument that duplicates a
    positional one
    """
    # this is the nifty pytest way to check for Exceptions
    with pytest.raises(TypeError):
        result = colors('yellow', fore_color='purple')
        print(result)


def test_duplicate2():
    """
    It's an error to have a keyword argument that duplicates a
    positional one
    """
    # this is a way to do it by hand:
    try:
        result = colors('yellow', fore_color='purple')
        print(result)
        assert False
    except TypeError as err:
        # you can also check if the error message is what you expect
        assert "multiple values for argument" in err.args[0]


def test_call_tuple():
    t = ('red', 'blue', 'yellow', 'chartreuse')
    result = colors(*t)

    # these aren't exhaustive by any means
    # but mostly I want to make the code runs without error
    print(result)
    assert 'red' in result
    assert 'blue' in result
    assert 'chartreuse' in result
    # you can force a test failure if you want to see the output
    # assert False


def test_call_dict():
    d = {'fore_color': 'red',
         'visited_color': 'cyan',
         'link_color': 'green',
         'back_color': 'blue',
         }
    result = colors(**d)

    print(result)
    assert 'foreground: red' in result
    assert 'background: blue' in result
    assert 'visited: cyan' in result
    assert 'link: green' in result
    # you can force a test failure if you want to see the output
    # assert False


def test_call_tuple_dict():
    t = ('red', 'blue')

    d = {'visited_color': 'cyan',
         'link_color': 'green',
         }
    result = colors(*t, **d)

    print(result)
    assert 'foreground: red' in result
    assert 'background: blue' in result
    assert 'visited: cyan' in result
    assert 'link: green' in result
    # you can force a test failure if you want to see the output
    # assert False


def test_call_everything():
    """
    this one uses:
      - a positional argument
      - *tuple
      - a keyword argument
      - **dict
    """
    t = ('red',)  # note the extra comma to amke it a tuple!

    d = {'visited_color': 'cyan'}

    result = colors('blue', *t, link_color='orange', **d)

    print(result)
    assert 'foreground: blue' in result
    assert 'background: red' in result
    assert 'visited: cyan' in result
    assert 'link: orange' in result
    # you can force a test failure if you want to see the output
    # assert False


def test_call_undefined_kwarg():
    # should get an error passing in non-existand keyword
    with pytest.raises(TypeError):
        result = colors(weird_color='grey')


# ###########################
# now lets try calling call_colors in all the above ways, and see if we get what we expect.
#
# Note that these tests are really testing the Python machinery
#  -- which you don't need to do! Python is already well tested.
#
# But writing theese tests tests your undestanding of how things work
#    if a test fails, it's because you ( I ;- ) didn't understand the
#    calling convertions.
# ############################


def test_call_all_positional():
    args, kwargs = call_colors('red', 'blue', 'yellow', 'chartreuse')

    # no kwrags, they should all be in the args tuple:
    assert not kwargs  # kwargs is empty
    assert args == ('red', 'blue', 'yellow', 'chartreuse')


def test_call_one_keyword():
    args, kwargs = call_colors(link_color='purple')

    assert not args  # args should be an empty tuple
    assert kwargs['link_color'] == 'purple'
    assert len(kwargs) == 1  # only one entry in the kwargs dict


def test_call_pos_and_keyword():
    args, kwargs = call_colors('yellow', 'gray', link_color='purple')

    assert args == ('yellow', 'gray')
    assert kwargs == {'link_color': 'purple'}


def test_call_duplicate():
    """
    This was an error above -- but is not here -- no keyword arguments
    to duplicate!
    """

    args, kwargs = call_colors('yellow', fore_color='purple')

    assert args == ('yellow',)
    assert kwargs == {'fore_color': 'purple'}


def test_call_call_tuple():
    t = ('red', 'blue', 'yellow', 'chartreuse')
    args, kwargs = call_colors(*t)

    # This is straighforward -- the args tuple should be the one passed in!
    assert args == t

    # But it is NOT the SAME tuple!
    assert args is not t
    # and an empty kwargs dict
    assert kwargs == {}  # multiple ways to test for an empty dict.


def test_call_call_dict():
    d = {'fore_color': 'red',
         'visited_color': 'cyan',
         'link_color': 'green',
         'back_color': 'blue',
         }
    args, kwargs = call_colors(**d)

    # also easy -- should be the dict passed in
    assert kwargs == d
    assert args == tuple()


def test_call_call_tuple_dict():
    t = ('red', 'blue')

    d = {'visited_color': 'cyan',
         'link_color': 'green',
         }
    args, kwargs = call_colors(*t, **d)

    # this should be just what's passed in.
    assert args == t
    assert kwargs == d


def test_call_call_everything():
    """
    this one uses:
      - a positional argument
      - *tuple
      - a keyword argument
      - **dict
    """
    t = ('red',)  # note the extra comma to amke it a tuple!

    d = {'visited_color': 'cyan'}

    args, kwargs = call_colors('blue', *t, link_color='orange', **d)

    # This one is more interesting:
    assert args == ('blue',) + t
    assert args == ('blue', 'red')  # a different way to spell the same thing

    assert kwargs == {'visited_color': 'cyan', 'link_color': 'orange'}
    # or:
    d['link_color'] = 'orange'
    assert kwargs == d


# ##################
# Now to test the manual upacking of args, kwargs
# All the same tests as above should pass
# ##################


# Calling "colors" in various ways.
def test_manual_all_positional():
    result = colors('red', 'blue', 'yellow', 'chartreuse')

    # these aren't exhaustive by any means
    # but mostly I want to make the code runs without error
    print(result)
    assert 'red' in result
    assert 'blue' in result
    assert 'chartreuse' in result
    # you can force a test failure if you want to see the output
    # assert False


def test_manual_one_keyword():
    result = colors_manual(link_color='purple')
    # these aren't exhaustive by any means
    # but mostly I want to make the code runs without error
    print(result)
    assert 'link: purple' in result
    # you can force a test failure if you want to see the output
    # assert False


def test_manual_pos_and_keyword():
    result = colors_manual('yellow', 'gray', link_color='purple')
    # these aren't exhaustive by any means

    print(result)
    assert 'foreground: yellow' in result
    assert 'background: gray' in result
    assert 'link: purple' in result
    # you can force a test failure if you want to see the output
    # assert False


def test_manual_duplicate():
    """
    It's an error to have a keyword argument that duplicates a
    positional one
    """
    # this is the nifty pytest way to check for Exceptions
    with pytest.raises(TypeError):
        result = colors_manual('yellow', fore_color='purple')
        print(result)


def test_manual_duplicate2():
    """
    It's an error to have a keyword argument that duplicates a
    positional one
    """
    # this is a way to do it by hand:
    try:
        result = colors_manual('yellow', fore_color='purple')
        print(result)
        assert False
    except TypeError as err:
        # you can also check if the error message is what you expect
        assert "multiple values for argument" in err.args[0]


def test_manual_call_tuple():
    t = ('red', 'blue', 'yellow', 'chartreuse')
    result = colors_manual(*t)

    # these aren't exhaustive by any means
    # but mostly I want to make the code runs without error
    print(result)
    assert 'red' in result
    assert 'blue' in result
    assert 'chartreuse' in result
    # you can force a test failure if you want to see the output
    # assert False


def test_manual_call_dict():
    d = {'fore_color': 'red',
         'visited_color': 'cyan',
         'link_color': 'green',
         'back_color': 'blue',
         }
    result = colors_manual(**d)

    print(result)
    assert 'foreground: red' in result
    assert 'background: blue' in result
    assert 'visited: cyan' in result
    assert 'link: green' in result
    # you can force a test failure if you want to see the output
    # assert False


def test_manual_call_tuple_dict():
    t = ('red', 'blue')

    d = {'visited_color': 'cyan',
         'link_color': 'green',
         }
    result = colors_manual(*t, **d)

    print(result)
    assert 'foreground: red' in result
    assert 'background: blue' in result
    assert 'visited: cyan' in result
    assert 'link: green' in result
    # you can force a test failure if you want to see the output
    # assert False


def test_manual_call_everything():
    """
    this one uses:
      - a positional argument
      - *tuple
      - a keyword argument
      - **dict
    """
    t = ('red',)  # note the extra comma to amke it a tuple!

    d = {'visited_color': 'cyan'}

    result = colors_manual('blue', *t, link_color='orange', **d)

    print(result)
    assert 'foreground: blue' in result
    assert 'background: red' in result
    assert 'visited: cyan' in result
    assert 'link: orange' in result
    # you can force a test failure if you want to see the output
    # assert False


def test_manual_call_undefined_kwarg():
    # should get an error passing in non-existand keyword
    with pytest.raises(TypeError):
        result = colors_manual(weird_color='grey')
