#!/usr/bin/env python

"""
a simple script can run and test your html rendering classes.

Uncomment the steps as you add to your rendering.

"""

from io import StringIO

# importing the html_rendering code with a short name for easy typing.
import html_render as hr
# reloading in case you are running this in iPython
#  -- we want to make sure the latest version is used
import importlib
importlib.reload(hr)


# writing the file out:
def render_page(page, filename):
    """
    render the tree of elements

    This uses StringIO to render to memory, then dump to console and
    write to file -- very handy!
    """

    f = StringIO()
    page.render(f, "    ")

    f.seek(0)

    print(f.read())

    f.seek(0)
    open(filename, 'w').write(f.read())


# Step 1
#########

page = hr.Element()

page.append("Here is a paragraph of text -- there could be more of them, "
            "but this is enough  to show that we can do some text")

page.append("And here is another piece of text -- you should be able to add any number")

render_page(page, "test_html_output1.html")

# The rest of the steps have been commented out.
#  Uncomment them a you move along with the assignment.

# ## Step 2
# ##########

# page = hr.Html()

# body = hr.Body()

# body.append(hr.P("Here is a paragraph of text -- there could be more of them, "
#                  "but this is enough  to show that we can do some text"))

# body.append(hr.P("And here is another piece of text -- you should be able to add any number"))

# page.append(body)

# render_page(page, "test_html_output2.html")

# # Step 3
# ##########

# page = hr.Html()

# head = hr.Head()
# head.append(hr.Title("PythonClass = Revision 1087:"))

# page.append(head)

# body = hr.Body()

# body.append(hr.P("Here is a paragraph of text -- there could be more of them, "
#                  "but this is enough  to show that we can do some text"))
# body.append(hr.P("And here is another piece of text -- you should be able to add any number"))

# page.append(body)

# render_page(page, "test_html_output3.html")

# # Step 4
# ##########

# page = hr.Html()

# head = hr.Head()
# head.append(hr.Title("PythonClass = Revision 1087:"))

# page.append(head)

# body = hr.Body()

# body.append(hr.P("Here is a paragraph of text -- there could be more of them, "
#                  "but this is enough  to show that we can do some text",
#               style="text-align: center; font-style: oblique;"))

# page.append(body)

# render_page(page, "test_html_output4.html")

# # Step 5
# #########

# page = hr.Html()

# head = hr.Head()
# head.append(hr.Title("PythonClass = Revision 1087:"))

# page.append(head)

# body = hr.Body()

# body.append(hr.P("Here is a paragraph of text -- there could be more of them, "
#                  "but this is enough  to show that we can do some text",
#               style="text-align: center; font-style: oblique;"))

# body.append(hr.Hr())

# page.append(body)

# render_page(page, "test_html_output5.html")

# # Step 6
# #########

# page = hr.Html()

# head = hr.Head()
# head.append(hr.Title("PythonClass = Revision 1087:"))

# page.append(head)

# body = hr.Body()

# body.append(hr.P("Here is a paragraph of text -- there could be more of them, "
#                  "but this is enough  to show that we can do some text",
#               style="text-align: center; font-style: oblique;"))

# body.append(hr.Hr())

# body.append("And this is a ")
# body.append( hr.A("http://google.com", "link") )
# body.append("to google")

# page.append(body)

# render_page(page, "test_html_output6.html")

# # Step 7
# #########

# page = hr.Html()

# head = hr.Head()
# head.append(hr.Title("PythonClass = Revision 1087:"))

# page.append(head)

# body = hr.Body()

# body.append( hr.H(2, "PythonClass - Class 6 example") )

# body.append(hr.P("Here is a paragraph of text -- there could be more of them, "
#                  "but this is enough  to show that we can do some text",
#               style="text-align: center; font-style: oblique;"))

# body.append(hr.Hr())

# list = hr.Ul(id="TheList", style="line-height:200%")

# list.append( hr.Li("The first item in a list") )
# list.append( hr.Li("This is the second item", style="color: red") )

# item = hr.Li()
# item.append("And this is a ")
# item.append( hr.A("http://google.com", "link") )
# item.append("to google")

# list.append(item)

# body.append(list)

# page.append(body)

# render_page(page, "test_html_output7.html")

# # Step 8
# ########

# page = hr.Html()


# head = hr.Head()
# head.append( hr.Meta(charset="UTF-8") )
# head.append(hr.Title("PythonClass = Revision 1087:"))

# page.append(head)

# body = hr.Body()

# body.append( hr.H(2, "PythonClass - Class 6 example") )

# body.append(hr.P("Here is a paragraph of text -- there could be more of them, "
#                  "but this is enough  to show that we can do some text",
#                  style="text-align: center; font-style: oblique;"))

# body.append(hr.Hr())

# list = hr.Ul(id="TheList", style="line-height:200%")

# list.append( hr.Li("The first item in a list") )
# list.append( hr.Li("This is the second item", style="color: red") )

# item = hr.Li()
# item.append("And this is a ")
# item.append( hr.A("http://google.com", "link") )
# item.append("to google")

# list.append(item)

# body.append(list)

# page.append(body)

# render_page(page, "test_html_output8.html")
