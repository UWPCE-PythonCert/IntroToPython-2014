A context manager as a simple timer
#####################################

See if you can write a context manger that will time some code. 

When using it, you can do::

    with timer:
        this_is_some_code_to_run()
        how_long_might_it_take


and you'll get something like::

  this code took 0.12 seconds

NOTE:
-------

you can do simple timing with the time module. Without a context, you'd do::

	import time

	start_time = time.clock()

	run_some_code_here

	run_time = time.clock - start_time
	print "this code took %f seconds"%run_time)

But isn't::
    with Timer():

easier?


NOTE2:
-------

The context manager's __exit__() method is called with three arguments, the exception details (type, value, traceback): the same values returned by sys.exc_info(), which can also be None if no exception occurred). 

If you do'nt want to do anytihng special with exceptions, youc an ignore them, but the __exit__ method msut take something::

    def __exit__(self, *args)
        your_code_that
        ignors_exceptions


will do fine...