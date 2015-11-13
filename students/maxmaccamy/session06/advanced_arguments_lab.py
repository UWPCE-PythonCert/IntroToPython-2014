__author__ = 'Max'

def page_color(fore_color = 'White',
               back_color = 'White',
               link_color = 'White',
               visited_color = 'White'):
    fs = 'fore_color    = {fore}\n \
          back_color    = {back}\n \
          link_color    = {link}\n \
          visited_color = {visited}\n'
    print(fs.format(fore = fore_color, back = back_color, link = link_color, visited = visited_color))

def page_color1(**kwargs):
    fs = 'fore_color    = {fore}\n \
          back_color    = {back}\n \
          link_color    = {link}\n \
          visited_color = {visited}\n'
    print(fs.format(fore = kwargs['fore_color'], back = kwargs['back_color'], link = kwargs['link_color'], visited = kwargs['visited_color']))

def page_color2(**kwargs):
    fs = 'fore_color    = {fore}\n \
          back_color    = {back}\n \
          link_color    = {link}\n \
          visited_color = {visited}\n'
    print(fs.format(fore = kwargs['fore_color'], back = kwargs['back_color'], link = kwargs['link_color'], visited = kwargs['visited_color']))

def page_color3(**kwargs):
    fs = 'fore_color    = {}\n \
          back_color    = {}\n \
          link_color    = {}\n \
          visited_color = {}\n'
    print(fs.format(kwargs))

if __name__ == '__main__':
    print("Running ")
    page_color()

    fullargs = {'fore_color': 'Red',
              'back_color': 'Green',
              'link_color': 'Blue',
              'visited_color': 'Purple'}

    partialargs = {'fore_color': 'Red',
              'back_color': 'Green',
              'link_color': 'Blue'}

    args =  ('Purple', 'Blue', 'Green', 'Red')

    page_color1(**kwargs)

    # The below commented out function will fail since the function definition
    # does not contain any positional arguments.
    #page_color2(*args, **kwargs)

    page_color3(**kwargs)


