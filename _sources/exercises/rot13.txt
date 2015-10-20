.. _exercise_rot13:

*****
ROT13
*****

Goal
----

Get used to working with the number values for characters

Get a bit of practice with string methods and string processing


ROT13 encryption
-----------------

The ROT13 encryption scheme is a simple substitution cypher where each letter
in a text is replace by the letter 13 away from it (imagine the alphabet as a
circle, so it wraps around).

The task
--------

Add a python module named ``rot13.py`` to the session03 dir in your student dir. This module should provide at least one function called ``rot13`` that takes any amount of text and returns that same text encrypted by ROT13.

This function should preserve whitespace, punctuation and capitalization.

Your module should include an ``if __name__ == '__main__':`` block with tests (asserts) that demonstrate that your ``rot13`` function and any helper functions you add work properly.


.. nextslide:: A bit more

There is a "short-cut" available that will help you accomplish this task. Some
spelunking in `the documentation for strings`_ should help you to find it. If
you do find it, using it is completely fair game.

As usual, add your new file to your local clone right away.  Make commits
early and often and include commit messages that are descriptive and concise.

When you are done, if you want me to review it, push your changes to github
and issue a pull request.

try decrypting this:

"Zntargvp sebz bhgfvqr arne pbeare"

.. _the documentation for strings: https://docs.python.org/3/library/stdtypes.html#string-methods
