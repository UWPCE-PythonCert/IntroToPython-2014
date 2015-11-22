#keyword argument lab

def quad(fore_color = 'teal', back_color='macbook_gold', link_color='blue', visited_color='purple'):
    print(fore_color, back_color, link_color, visited_color)

    

    """ Have it pull the parameters out with *args, **kwargs """

    
quad()

quad('black','black','gold','black')
