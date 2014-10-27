Session 04 ReadMe
===============================

Review of homework indicates there is a good opportunity here to update mailroom and the associated data storage types.  This should greatly simplify subsequent code.

MORE LOOPING RECOMMENDATIONS
-----------

remember: double looping can be accomplished by zipping two iterables together --
    for i, j in zip(list1, list2):
        do some stuff....

zipping can do any number of lists, creating a set of tuples with n values where n is the number of lists entered into zip

SLICING
-----------
list[i1:i2] = []  will replace list values with empty list, an effective erase tool

DICTIONARIES
-----------
dict.keys() -- key items
dict.values() -- value items
dict.items() -- returns tuples of key, value

support in, not in operators for keys BUT
     the same operators can be combined with dict.view items to check for 
     membership.  Very powerful.

dict.get('key_value') returns key's associated value within dictionary, will take second argument and return a default value if the key is absent

dict.pop('key_value') ==> returns value at key location and removes from dict
    (note similarity to list.pop(i)) no location pops last item

setdefault(key, [, default]) -- gets the value if present, sets default otherwise

sets are dictionaries with only keys, no associated values, construct w/{}

sets are mutable, there is an immutable variety called 'frozenset' syntax is same


EXCEPTIONS
-----------

ALWAYS ALWAYS specify the errors that will be excepted -- blank exceptions
are a very bad habit

Don't set up your code to catch exceptions unless there is something that can be done there to address the error

Check out PyCon when bored


    try:
        (tries to run)
    
    except (error):
        (runs on failure)
    
    finally:
        (always runs)
    
    else:
        (runs only when there is no exception)

    raise (error)('print some message') -- manually trip an error and send note


IO HANDLING

f = open( 'secrets.txt', [mode flags])

FLAGS

    * 'r', 'w', 'a'
    * 'rb', 'wb', 'ab'
    * r+, w+, a+
    * r+b, w+b, a+b
    * U
    * U+

be careful! 'w' flag will clear the file that is opened in prep for writing

file object is an iterator

stringIO module writes to memory

    * os module
    * os.getcwd()
    * os.chdir(path)
    * os.path.abspath()itp
    * os.path.relpath()
    * os.path.split()
    * os.listdir()
    * os.mkdir()

os.walk() -- very handy

shutil module

pathlib
pip install pathlib -- not included with Anaconda

!! really need to get to know unicode !! 


