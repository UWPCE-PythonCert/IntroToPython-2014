def colors(*fore_color, **link_color):
    print("The positional arguments are fore_color and back_color = ,", fore_color)
    print("The keyboard arguments are link_colr and visited_color = ,", link_color)

colors('yellow', 'black', link_color = 'green', visited_color = 'grey')
colors('blue', 'red', link_color = 'green', visited_color = 'grey')

