#!/usr/bin/env python
from datetime import datetime
import sys


class Timer(object):

    def __init__(self, file_object=sys.stdout):
        self.file_object = file_object

    def __enter__(self):
        self.start = datetime.now()
        return self

    def __exit__(self, e_type, e_value, e_tb):
        elasped = datetime.now() - self.start
        output = "This took {:f} seconds.".format(elasped.total_seconds())
        try:
            self.file_object.write(output)
        except AttributeError as e:
            raise e

        return False
