#!/usr/local/bin/python


def func(fore_color='White',
         back_color='Black',
         link_color='Blue',
         visited_color='Green'):
    """Print colors."""
    s = ('{} ' * 4).strip()

    print s.format(fore_color, back_color, link_color, visited_color)


def func_args(**kwargs):
    """Print colors."""
    s = '{fore_color}, {back_color}, {link_color}, {visited_color}'

    print s.format(**kwargs)


# call the function with various parameters
func((1, 2, 3, 4))  # prints the tuple in the first argument

func(*(1, 2, 3, 4))

args = (1, 2, 3, 4)
func(*args)

kwargs = {'fore_color':'hey',
          'back_color':'there',
          'link_color':'how',
          'visited_color':'you'}
func_args(**kwargs)
