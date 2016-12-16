#!/usr/bin/env python

"""
Exceptions Lab solution:

The raw_input() function can generate two exceptions:
EOFError or KeyboardInterrupt on end-of-file(EOF) or canceled input.

Create a wrapper function, perhaps safe_input() that returns None rather
rather than raising these exceptions, when the user enters ^C for Keyboard
Interrupt, or ^D (^Z on Windows) for End Of File.

NOTE: if the user types a few charactors, and the hits ctrl+C, the
KeyboardInterrupt gets caught somewhere deeper in the process, and
this function doesn't work.

Don't worry about that -- I don't really understnd what's going on in
the REPL (Read, Evaluate, Print Loop) either -- and the point of this
assigment is simple Exception handling.
"""


def safe_input(prompt_string=""):
    """
    print user for input -- returning a string.

    This is just like the built-in input(), but it will return None
    if the user hits ctrl+c, (or ctrl+D) rather than raise an Exception.
    """
    try:
        response = input(prompt_string)
        return response
    except (EOFError, KeyboardInterrupt):
        return None

if __name__ == "__main__":
    response = safe_input("Say Something: ")
    if response is None:
        print("Hey! you cancled out!!!")
    else:
        print("You said:", response)
