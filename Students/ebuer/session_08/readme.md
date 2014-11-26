##Session 8: Callable Classes, Iterators, Generators  

###Callable Classes  

What do you do when you want to evaluate the same function several times with the same set of arguments?  

This is a good place to apply a callable -- something you can call like a function.  

A class object is itself a callable.

```python
__call__(*args, **kwargs)

class Callable(object):
    def __init__(self, ...._)
        some init stuff
    def __call__(self, some parameters)
````

*Key Sequence Protocols*  
    __len__
    __getitem__
    __setitem__
    __delitem__
    __contains__

