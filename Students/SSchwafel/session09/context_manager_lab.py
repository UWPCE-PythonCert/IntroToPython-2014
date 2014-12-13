#!/usr/bin/python

class Timer(object):

    def __enter__(self):
        print "In __enter__"
        self.start = time.time()
        return self
         
    def __exit__(self, err_type, err_val, err_trc):

        print "In __exit__" 
        self.elapsed = time.time() - self.start
        print "Run took {} seconds".format(self.elapsed)
        print err_type, err_val, err_trc
