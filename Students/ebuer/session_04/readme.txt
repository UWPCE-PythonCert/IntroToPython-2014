Starting Session 04 readme.

Review of homework indicates there is a good opportunity here to update mailroom and the associated data storage types.  This should greatly simplify subsequent code.

remember: double looping can be accomplished by zipping two iterables together --
    for i, j in zip(list1, list2):
        do some stuff....


DICTIONARIES

dict.keys() -- key items
dict.values() -- value items
dict.items() -- returns tuples of key, value

support in, not in operators for keys BUT
     the same operators can be combined with dict.view items to check for 
     membership.  Very powerful.

dict.get('key_value') returns location within dictionary
dict.pop('key_value') ==> returns value at key location and removes from dict
    (note similarity to list.pop(i))

setdefault(key, [value, default]) -- gets the value if present, sets default otherwise

sets are dictionaries with only keys, no associated values, construct w/{}

sets are mutable, there is an immutable variety called 'frozenset' syntax is same



