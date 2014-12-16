'''

Write a function that has four optional parameters (with defaults):
fore_color
back_color
link_color
visited_color
Have it print the colors (use strings for the colors)
Call it with a couple different parameters set

'''

def variableColors(fore_color = 'white', back_color='black', link_color='blue', visited_color='dark_blue'):
    print 'Colors:', fore_color, back_color, link_color, visited_color
    
if __name__ == "__main__":
    colors = ('red', 'white', 'blue', 'green')
    more_colors={'back_color': 'yellow', 'link_color':'brown', 'visited_color':'mauve', 'fore_color': 'orange'}
    variableColors()
    variableColors('red', 'white', 'blue', 'green')
    variableColors(*colors)
    variableColors(**more_colors)
    variableColors(fore_color='purple', back_color='pink')
    variableColors(link_color='purple', visited_color='pink')
      