def colors(fore_color='red', back_color='yellow', link_color='blue', visited_color='green'):
    print fore_color
    print back_color
    print link_color
    print visited_color

def colors_kwargs(**kwargs):
    for key, value in kwargs.iteritems():
        print 'key = {}'.format(key)
        print 'value = {}'.format(value)



# colors('darkred', 'darkyellow', 'darkblue', 'darkgreen')


colors_kwargs(fore_color='darkred', back_color = 'darkyellow', link_color ='darkblue', visited_color ='darkgreen')

