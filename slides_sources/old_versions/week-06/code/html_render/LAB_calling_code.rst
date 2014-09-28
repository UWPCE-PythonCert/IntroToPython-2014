Calling Code
###############

Code that can be used to call your html rendering classes

Step 1
--------
::

    page = Html()

    page.append("Here is a paragraph of text -- there could be more of them, but this is enough  to show that we can do some text")

Step 2
-------
::

    page = Html()

    body = Body()

    body.append(P("Here is a paragraph of text -- there could be more of them, but this is enough  to show that we can do some text"))

    page.append(body)

Step 3
---------
::

    page = Html()

    head = Head()
    head.append(Title("PythonClass = Revision 1087:"))

    page.append(head)

    body = Body()

    body.append(P("Here is a paragraph of text -- there could be more of them, but this is enough  to show that we can do some text"))

    page.append(body)

Step 4
---------
::

    page = Html()

    head = Head()
    head.append(Title("PythonClass = Revision 1087:"))

    page.append(head)

    body = Body()

    body.append(P("Here is a paragraph of text -- there could be more of them, but this is enough  to show that we can do some text",
                  style="text-align: center; font-style: oblique;"))

    page.append(body)

Step 5
---------
::

    page = Html()

    head = Head()
    head.append(Title("PythonClass = Revision 1087:"))

    page.append(head)

    body = Body()

    body.append(P("Here is a paragraph of text -- there could be more of them, but this is enough  to show that we can do some text",
                  style="text-align: center; font-style: oblique;"))

    body.append(Hr())

    page.append(body)

Step 6
---------
::

    page = Html()

    head = Head()
    head.append(Title("PythonClass = Revision 1087:"))

    page.append(head)

    body = Body()

    body.append(P("Here is a paragraph of text -- there could be more of them, but this is enough  to show that we can do some text",
                  style="text-align: center; font-style: oblique;"))

    body.append(Hr())

    body.append("And this is a ")
    body.append( A("http://google.com", "link") )
    body.append("to google")

    page.append(body)

Step 7
---------
::

    page = Html()

    head = Head()
    head.append(Title("PythonClass = Revision 1087:"))

    page.append(head)

    body = Body()

    body.append(  H(2, "PythonClass - Class 6 example") )

    body.append(P("Here is a paragraph of text -- there could be more of them, but this is enough  to show that we can do some text",
                  style="text-align: center; font-style: oblique;"))

    body.append(Hr())

    list = Ul(id="TheList", style="line-height:200%")
    list.append( Li("The first item in a list") )
    list.append( Li("This is the second item", style="color: red") )
    item = Li()
    item.append("And this is a ")
    item.append( A("http://google.com", "link") )
    item.append("to google")
    list.append(item)
    body.append(list)

    page.append(body)

Step 8
---------
::

    page = Html()

    head = Head()
    head.append( Meta(charset="UTF-8") )
    head.append(Title("PythonClass = Revision 1087:"))

    page.append(head)

    body = Body()

    body.append(  H(2, "PythonClass - Class 6 example") )

    body.append(P("Here is a paragraph of text -- there could be more of them, but this is enough  to show that we can do some text",
                  style="text-align: center; font-style: oblique;"))

    body.append(Hr())

    list = Ul(id="TheList", style="line-height:200%")
    list.append( Li("The first item in a list") )
    list.append( Li("This is the second item", style="color: red") )
    item = Li()
    item.append("And this is a ")
    item.append( A("http://google.com", "link") )
    item.append("to google")
    list.append(item)
    body.append(list)

    page.append(body)
