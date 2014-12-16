#!/usr/bin/python

def colors(x='green',y='red',z='perrywinkle',n='yellow'):
    print x + ' ' + y + ' '+ z + ' ' + n

colors()
colors('banana','catfish','bogwater','blue')

color_list = {'x':'green','y':'red','z':'perrywinkle','n':'yellow'}

colors(**color_list)
color_list = ['green','red','perrywinkle','yellow']
colors(*color_list)

