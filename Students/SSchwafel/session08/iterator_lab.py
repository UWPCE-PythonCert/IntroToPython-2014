#!/usr/bin/python

class IterateMe(object):

    def __init__(self, stop, *args):
    

        if not args:

            self.start = -1
            self.stop = stop

        else:

            self.start = stop-1
            self.stop = args[0]
        
            if len(args) == 2:
                self.step = args[1]
		self.start = stop-self.step

    def __iter__(self):
        self.current = self.start

    def next(self):

        self.current += self.step

        if self.current < self.stop:
            return self.current

        else:
            raise StopIteration
            

    
    
