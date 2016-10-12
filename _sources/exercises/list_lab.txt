.. _exercise_list_lab:

********
List Lab
********

Learning about lists
====================

After:

http://www.upriss.org.uk/python/session5.html

Goal:
-----

Learn the basic ins and outs of Python lists.

hint
----

to query the user for info at the command line, you use:

.. code-block:: python

     response = input("a prompt for the user > ")

``response`` will be a string of whatever the user types (until a <return>).


Procedure
---------

In your student dir in the IntroPython2015 repo, create a ``session03`` dir and put in a new ``list_lab.py`` file.

The file should be an executable python script. That is to say that one
should be able to run the script directly like so:

.. code-block:: bash

    $ ./list_lab.py

(At least on OS-X and Linux)

-- you do that with this command:

.. code-block:: bash

  $ chmod +x list_lab.py

(The +x means make this executable)

The file will also need this on the first line::

    #!/usr/bin/env python3

This is known as the "she-bang" line -- it tells the shell how to execute that file -- in this case, with ``python3``

NOTE: on Windows, there is a python launcher which, if everything is configured correctly look at that line to know you want python3 if there is more than one python on your system.

.. nextslide::

Add the file to your clone of the repository and commit changes frequently
while working on the following tasks. When you are done, push your changes to
GitHub and issue a pull request.

(if you are struggling with git -- just write the code for now)

When the script is run, it should accomplish the following four series of
actions:

.. nextslide:: Series 1

- Create a list that contains "Apples", "Pears", "Oranges" and "Peaches".
- Display the list.
- Ask the user for another fruit and add it to the end of the list.
- Display the list.
- Ask the user for a number and display the number back to the user and the
  fruit corresponding to that number (on a 1-is-first basis).
- Add another fruit to the beginning of the list using "+" and display the
  list.
- Add another fruit to the beginning of the list using insert() and display the list.
- Display all the fruits that begin with "P", using a for loop.


.. nextslide:: Series 2

Using the list created in series 1 above:

- Display the list.
- Remove the last fruit from the list.
- Display the list.
- Ask the user for a fruit to delete and find it and delete it.
- (Bonus: Multiply the list times two. Keep asking until a match is found. Once found, delete all occurrences.)

.. nextslide:: Series 3

Again, using the list from series 1:

- Ask the user for input displaying a line like "Do you like apples?"
- for each fruit in the list (making the fruit all lowercase).
- For each "no", delete that fruit from the list.
- For any answer that is not "yes" or "no", prompt the user to answer with one
  of those two values (a while loop is good here):
- Display the list.

.. nextslide:: Series 4

Once more, using the list from series 1:

- Make a copy of the list and reverse the letters in each fruit in the copy.
- Delete the last item of the original list. Display the original list and the
  copy.
