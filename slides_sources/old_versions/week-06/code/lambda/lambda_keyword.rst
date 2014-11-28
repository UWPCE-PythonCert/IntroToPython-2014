lambda and keyword evaluation excercise
#########################################


The challenge:
=================

Write a function that returns a list of n functions,
such that each one, when called, will return the input value,
incremented by an increasing number.

You should use a for loop, lambda, and a keyword argument

Not clear? here's what you should get::

	In [96]: the_list = function_builder(4)
    ### so the_list should contain n functions (callables)

	In [97]: the_list[0](2)
	Out[97]: 2
    ## the zeroth element of the list is a function that add 0
    ## to the input, hence called with 2, returns 2

	In [98]: the_list[1](2)
	Out[98]: 3
	## the 1st element of the list is a function that adds 1
	## to the input value, thus called with 2, returns 3

	In [100]: for f in the_list:
	    print f(5)
	   .....:     
	5
	6
	7
	8
    ### If you loop through them all, and call them, each one adds one more to the input, 5... i.e. the nth function in the list adds n to the input.


Extra credit:
================

Do it with a list comprhension, instead of a for loop

TDD:
==========

In lambda_keyword.py, there is a function defined::


    def function_builder(n):
        ## put something in here...
        pass

Clearly, it does nothing. However in test_lambda_keyword.py there are some tests -- you can run them, but they will fail::

    $ py.test test_lambda_keyword.py 
    ...
    ...
    >   	assert func_list[0](12) == 12
    E    TypeError: 'NoneType' object has no attribute '__getitem__'

    test_lambda_keyword.py:42: TypeError
    =========================== 3 failed in 0.04 seconds ===============


Your goal is to fill in that funciton so that those tests pass.

"Cheating"
=============

Note that those tests only test a few things, and with small values -- so  you could pretty easily hard-code a bunch of stuff to make them pass -- but what's the fun of that?

This is eveidence that "full test coverage" is a fantasy!

