import time

class Timer (object):
    '''
    Context manager that prints elapsed time on exit.
    '''
    def __init__(self):
        print 'init'
        pass


    def __enter__(self):
        print 'enter'
        self.start = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print 'Exit'
        self.end = time.time()
        
    def elapsed_time (self):
        return self.end - self.start
