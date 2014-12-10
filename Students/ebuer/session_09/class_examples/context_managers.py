# -*- coding:  utf-8 -*-
import sys
from StringIO import StringIO
from contextlib import contextmanager


class Context(object):
    """from Doug Hellmann, PyMOTW
    http://pymotw.com/2/contextlib/#module-contextlib
    """
    def __init__(self, handle_error):
        print '__init__(%s)' % handle_error
        self.handle_error = handle_error

    def __enter__(self):
        print '__enter__()'
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print '__exit__(%s, %s, %s)' % (exc_type, exc_val, exc_tb)
        return self.handle_error


@contextmanager
def context(boolean):
    print "__init__ code here"
    try:
        print "__enter__ code goes here"
        yield object()
    except Exception as e:
        print "errors handled here"
        if not boolean:
            raise
    finally:
        print "__exit__ cleanup goes here"


@contextmanager
def print_encoded(encoding):
    old_stdout = sys.stdout
    sys.stdout = buff = StringIO()
    try:
        yield None
    finally:
        sys.stdout = old_stdout
        buff.seek(0)
        raw = buff.read()
        encoded = raw.encode(encoding)
        print encoded
