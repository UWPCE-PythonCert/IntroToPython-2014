#!/usr/bin/env python2.7
from textwrap import dedent

def colors(**kwargs):
    print "Colors are: {fore_color} {back_color} {link_color} {visited_color}".format(**kwargs)


colors(fore_color='white', back_color='black', link_color='red', visited_color='orange')

def colors2(fore_color, back_color, link_color='red', visited_color='orange'):
    print "Colors are: %s %s %s %s"%(fore_color, back_color, link_color, visited_color)

two_colors = ('white', 'black')
other_colors = {'link_color' : 'yellow', 'visited_color' : 'purple'}

colors2(*two_colors)
colors2(*two_colors, **other_colors)

def colors3 (fore_color='white', back_color='black', link_color='red', visited_color='orange', **kwargs):
    message = dedent('''
        Required variable colors are:
        fore_color    : {fore_color}
        back_color    : {back_color} 
        link_color    : {link_color}
        visited_color : {visited_color}
        '''.format(fore_color=fore_color, back_color=back_color, link_color=link_color, visited_color=visited_color) )
    print message
    if ( len(kwargs) > 0 ):
        for k, v in kwargs.items():
            print "{0} : {1}".format(k, v)

colors3()
colors3("orange", "white", "black", "red")

other_colors = {'special_characters' : 'purple', "code_text" : "green"}
colors3("blue", "yellow", "chartruse", "brown", **other_colors)
