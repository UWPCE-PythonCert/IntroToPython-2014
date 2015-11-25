def f(fore_color,back_color,link_color='y',visited_color='z'):
    print (('{},{} -- {},{}').format(fore_color,back_color,link_color,visited_color))

args = ('white', 'orange')
kwargs = {'link_color':'pink', 'visited_color':'beige'}

f(*args, **kwargs)