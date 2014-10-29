__author__ = 'Robert W. Perkins'


def show_color(fore_color='red', back_color='yellow', link_color='blue', visited_color='ltblue'):

    formatter = 'The fore color is {f_color}\n' \
        'The back color is {b_color}\n' \
        'The link color is {l_color}\n' \
        'The visited color is {v_color}\n'

    print formatter.format(f_color=fore_color, b_color=back_color, l_color=link_color, v_color=visited_color)


if __name__ == '__main__':
    show_color()
    show_color(fore_color='green')
    d = {
        'fore_color': 'teal',
        'back_color': 'mauve',
        'link_color': 'ochre',
        'visited_color': 'viridian'
    }
    show_color(**d)