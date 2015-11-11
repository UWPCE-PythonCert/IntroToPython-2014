#! /usr/bin/env python 3


colors = {
    'back_color': 'black',
    'fore_color': 'white',
    'link_color': 'green',
    'visited_color': 'blue',
}


def print_colors1(*args, **kwargs):
    print(args)


def print_colors2(*args, **kwargs):
    print(kwargs)


if __name__ == '__main__':
    print_colors1(fore_color='white', back_color='black', link_color='green', visited_color='blue')
    print_colors2(fore_color='white', back_color='black', link_color='green', visited_color='blue')
    print_colors1('purple', 'black', link_color='green', visited_color='blue')
    print_colors2('purple', 'black', link_color='green', visited_color='blue')
    print_colors2(**colors)
