

# here is our printer function
def colors(fore_color='blue', back_color='black',
           link_color='red', visited_color='green'):
    print "Field colors: %s, %s\nLink colors: %s, %s\n"\
        % (fore_color, back_color, link_color, visited_color)

# try args, a tuple
targ = ('magenta', 'cyan')

# try kwargs, a dictionary
darg = {'visited_color': 'neon', 'fore_color': 'heart',
        'link_color': 'batman', 'back_color': 'bone'}

colors(**darg)

# more argument passing with our targ and darg
print 'I hate {visited_color}, but I love {fore_color}'.format(**darg)
print 'I hate {1}, but I love {0}\n'.format(*targ)

marg = {'my date': 'your mom', 'my girlfriend': 'your sister',
        'my best friend': 'your dad'}

print 'This is really tough but {my date} said that {my girlfriend} is sleeping with {my best friend}'.format(**marg)
