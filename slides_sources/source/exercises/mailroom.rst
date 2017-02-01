.. _exercise_mailroom:

********
Mailroom
********

A complete program
==================

Using basic data types and logic for a full program

Goal:
-----

You work in the mail room at a local charity. Part of your job is to write
incredibly boring, repetitive emails thanking your donors for their generous
gifts. You are tired of doing this over an over again, so you've decided to
let Python help you out of a jam.

The program
-----------

Write a small command-line script called ``mailroom.py``. This script should be executable. The script should accomplish the following goals:

* It should have a data structure that holds a list of your donors and a
  history of the amounts they have donated. This structure should be populated
  at first with at least five donors, with between 1 and 3 donations each

* The script should prompt the user (you) to choose from a menu of 3 actions:
  'Send a Thank You' or 'Create a Report' or 'quit')

Sending a Thank You
-------------------

* If the user (you) selects 'Send a Thank You', prompt for a Full Name.

  * If the user types 'list', show them a list of the donor names and re-prompt
  * If the user types a name not in the list, add that name to the data structure and use it.
  * If the user types a name in the list, use it.
  * Once a name has been selected, prompt for a donation amount.
  * Turn the amount into a number -- it is OK at this point for the program to crash if someone types a bogus amount.
  * Once an amount has been given, add that amount to the donation history of
    the selected user.
  * Finally, use string formatting to compose an email thanking the donor for
    their generous donation. Print the email to the terminal and return to the
    original prompt.

**It is fine to forget new donors once the script quits running.**

Creating a Report
------------------

* If the user (you) selected 'Create a Report' print a list of your donors,
  sorted by total historical donation amount.

  - Include Donor Name, total donated, number of donations and average donation amount as values in each row. You do not need to print out all their donations, just the summary info.
  - Using string formatting, format the output rows as nicely as possible.  The end result should be tabular (values in each column should align with those above and below)
  - After printing this report, return to the original prompt.

* At any point, the user should be able to quit their current task and return
  to the original prompt.

* From the original prompt, the user should be able to quit the script cleanly


Your report should look something like this::

    Donor Name                | Total Given | Num Gifts | Average Gift
    ------------------------------------------------------------------
    William Gates, III         $  653784.49           2  $   326892.24
    Mark Zuckerberg            $   16396.10           3  $     5465.37
    Jeff Bezos                 $     877.33           1  $      877.33
    Paul Allen                 $     708.42           3  $      236.14

Guidelines
----------

First, factor your script into separate functions. Each of the above
tasks can be accomplished by a series of steps.  Write discreet functions
that accomplish individual steps and call them.

Second, use loops to control the logical flow of your program. Interactive
programs are a classic use-case for the ``while`` loop.

Of course, ``input()`` will be useful here.

Put the functions you write into the script at the top.

Put your main interaction into an ``if __name__ == '__main__'`` block.

Finally, use only functions and the basic Python data types you've learned
about so far. There is no need to go any farther than that for this assignment.

Submission
----------

As always, put the new file in your student directory in a ``session03``
directory, and add it to your clone early. Make frequent commits with
good, clear messages about what you are doing and why.

When you are done, push your changes and make a pull request.

.. _exercise_mailroom_plus:

Adding dicts...
---------------


For the next week (after Session04)

You should have been able to do all that with the basic data types:

numbers, strings, lists and tuples.

But once you've learned about dictionaries (Session04) you may be able to re-write it a bit more simply and efficiently.

 * Update mailroom from last week to:

  - Use dicts where appropriate
  - Write a full set of letters to everyone to individual files on disk
  - See if you can use a dict to switch between the users selections
  - Try to use a dict and the .format() method to do the letter as one
    big template -- rather than building up a big string in parts.

Example:

.. code-block:: ipython

  In [3]: d
  Out[3]: {'first_name': 'Chris', 'last_name': 'Barker'}


  In [5]: "My name is {first_name} {last_name}".format(**d)
  Out[5]: 'My name is Chris Barker'

Don't worry too much about the "**" -- we'll get into the details later, but for now, it means, more or less -- pass this whole dict in as a bunch of keyword arguments.


.. _exercise_mailroom_exeptions:

Adding Exceptions
-----------------

**After Session05:**

* Exceptions:

Now that you've learned about Exception handling, you can update your code to handle errors better -- like when a user inputs bad data.

* Comprehensions:

Can you use comprehensions to clean up your code a bit?

* Tests

Add some tests..


