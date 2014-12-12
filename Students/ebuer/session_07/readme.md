##Session 7: Advanced OO, Properties, Class Methods

###More Subclassing

+ Subclassing is not for specialization
+ Nor is it for reusing code
+ The subclass is in charge (?) 


###Multiple Inheritance  
Inheriting from more than one class: just provide more than one parent

```python
class Combined(Super1, Super2, Super3):
    def __init__(self, something, somethingelse)
    Super1.__init__(self...)
    Super1.__init__(self...)
```

Remember: a method is an attribute of a class

Learn the method resolution order

Mixins:  
A subset of expected functionality in a re-usalbe package.  Why?  Because hierarchies are not always simple and clean.

Always subclass from 'object'

**super()**  
super() is a way to call a superclass method rather than explicity calling the unbound method on the superclass

see syntax examples in class notes

super() allows for more explicit calling of superclasses to ensure you are getting what you ask for.

####Properties -- Getters, Setters, Deleters  
Python provides a lack of clutter -- this is good

PJE on programming: python is not java

Uses a @ decorator, which adds functions for future special operations

    @property  
        def x(self):

means make a property called x with this as the getter

You do not need to define a setter, if you don't the attribute is read only.  Simiarly if yo don't define a deleter the attribute/property can't be deleted (this is generally prefered)

Remember to always inherit from object or all the @properties will not work

@property -- this is a getter, it gets a new property
@x.setter -- self explanitory, this allows new attribute to be set
@x.deleter -- same as above but for deleting

See example code

###Static and Class Methods

A __static method__ doesn't get self, self isn't passed in as part of the def()

```python
class staticadder(object):
    @staticmethod 
    def add(a, b):
         return a + b
```

Acts like a regular method sitting in the class object namespace without passing anything to it

Not actually very useful, but they are used in other languages, some of which require everything be in a class

Usually better to just write a module-level function

**Class Methods**  
Class method receives the class object rather than an instance as the first argument

Class methods are used fairly frequently, and they are friendly to subclassing

####Special Methods  
The core of _duck typing_

Special methods are tagged with dunders.
```python
object.__str___(self)
object.__unicode__(self)
object.__repr__(self)
```
    eval(repr(something)) == something

add a special method to a custom object to allow any user to call and apply the method using the same call as is normally associated with the __special__

for example def __add__(self): allows the '+' to be redefined to perform a custom function that then will be called when the '+' is applied to the class object

This is tricky.

**Protocols**  
Special methods needed to emulate a particular type of python object

```python
def __add__(self, v):
    """return element-wise vector sum of self and v"""
    assert len(self == len(v))
    return vector ([x1 + x2 for x1, x2 in zip(self, v)])
```


Use special methods when you want your class to act in a certain way

Homework:  
Circle class  
Project  
Render  