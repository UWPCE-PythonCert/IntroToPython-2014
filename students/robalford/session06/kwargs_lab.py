def print_colors(fore_color='blue', back_color='red', link_color='purple', visited_color='yellow'):
    print(fore_color, back_color, link_color, visited_color)

print_colors()

colors = {'back_color': 'green', 'visited_color': 'chartruese'}

print_colors(**colors)

colors = ('black', 'white')

print_colors(*colors)


def print_arbitrary_colors(*args, **kwargs):
    print(args, kwargs)

print_arbitrary_colors('blue', 'black', fore_color='white')
