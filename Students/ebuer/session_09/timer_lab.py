
import time



class Timer(object):

    def __enter__(self):
        print "in __enter__"
        self.start = time.time()
        return self

    def __exit__(self, err_type, err_val, err_trc):
        print "in __exit__"
        self.elapsed = time.time() - self.start

        print "program run took %f seconds" %self.elapsed
        print err_type, err_val, err_trc

        if issubclass(err_type, RuntimeError):
            print "a RuntimeError occurred"
            return True # passing True indicates the error has been addressed and we can continue running the code
        else:
            print "something else happened"


