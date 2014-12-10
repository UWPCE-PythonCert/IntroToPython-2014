__author__ = 'Ari'

from cStringIO import StringIO

import html_render as hr

reload(hr) # for ipython

## writing file out


def render_page(page, filename):
    """
    render the tree of elements
    """

    f = StringIO()
    page.render(f, "    ")

    f.reset()

    print f.read()

    f.reset()
    open(filename, 'w').write(f.read())


page = hr.Html()

head = hr.Head()

#head.append(hr.Meta(charset="UTF-8"))
head.append(hr.Title("some stuff ex"))

page.append(head)

body = hr.Body()

body.append(hr.H(2, "Python Class - Hmwk 6 ex"))

body.append(hr.P("Here is a paragraph - keep reading!!",
                 style="text-align: center, font-style: oblique;"))

body.append(hr.Hr())

list = hr.U1(id="TheList", style="line-height:200%")

list.append(hr.Li("the first item"))
list.append(hr.Li("the second item", style="color: red"))

item = hr.Li()
item.append("And this is a ")
item.append(hr.A("http://google.com", "link"))
item.append("to google")

list.append(item)

body.append(list)

page.append(body)

render_page(page, "test_html_outpt.html")