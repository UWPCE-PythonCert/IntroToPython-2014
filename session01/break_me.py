'''Session 1, Task 3 (Explore Errors)

In the break_me.py file write four simple Python functions:

Each function, when called, should cause an exception to happen
Each function should result in one of the four
common exceptions from our lecture.
For review: NameError, TypeError, SyntaxError, AttributeError'''


def name_error():
    print(bob)


def type_error():
    num = "bob"
    fraction = num / 5


def syntax_error():
    print "bob"


class Bob:
    # here to help with the attribute_error function
    def hello(self):
        print("hello")


def attribute_error():
    Bob.nonexistant_function()
