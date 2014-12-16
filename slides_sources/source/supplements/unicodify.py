#!/usr/bin/env python

'''
Decorators to convert all arguments passed to a function or method to
unicode or str, including default arguments

From: http://axialcorps.com/2014/03/20/unicode-str/

'''


import sys
import functools
import inspect
 
def _convert_arg(arg, from_, conv, enc):
    '''Safely convert unicode to string or string to unicode'''
    return getattr(arg, conv)(encoding=enc) if isinstance(arg, from_) else arg
 
def _wrap_convert(from_type, fn, encoding=None):
    '''Decorate a function converting all str arguments to unicode or
       vice-versa'''
    conv = 'decode' if from_type is str else 'encode'
    encoding = encoding or sys.getdefaultencoding()
 
    # override string defaults using partial
    aspec, dflts = inspect.getargspec(fn), {}
    if aspec.defaults:
        for k,v in zip(aspec.args[-len(aspec.defaults):],aspec.defaults):
            dflts[k] = _convert_arg(v, from_type, conv, encoding)
        fn = functools.partial(fn, **dflts)
 
    @functools.wraps(fn.func if isinstance(fn, functools.partial) else fn)
    def converted(*args, **kwargs):
        args = [_convert_arg(a, from_type, conv, encoding) for a in args]
        for k,v in kwargs.iteritems():
            kwargs[k] = _convert_arg(v, from_type, conv, encoding)
        return fn(*args, **kwargs)
 
    return converted
 
def unicodify(fn=None, encoding=None):
    '''Convert all str arguments to unicode'''
    if fn is None:
        return functools.partial(unicodify, encoding=encoding)
    return _wrap_convert(str, fn, encoding=encoding)
 
def stringify(fn=None, encoding=None):
    '''Convert all unicode arguments to str'''
    if fn is None:
        return functools.partial(stringify, encoding=encoding)
    return _wrap_convert(unicode, fn, encoding=encoding)
    
__all__ = ['unicodify', 'stringify']