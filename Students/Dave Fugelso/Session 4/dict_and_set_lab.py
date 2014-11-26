'''
Create a dictionary containing "name", "city", and "cake" for "Chris" from "Seattle" who likes "Chocolate".
Display the dictionary.

Delete the entry for "cake"
Display the dictionary.

Add an entry for "fruit" with "Mango" and display the dictionary.
Display the dictionary keys.

Display the dictionary values.

Display whether or not "cake" is a key in the dictionary (i.e. False) (now).

Display whether or not "Mango" is a value in the dictionary (i.e. True).

Using the dict constructor and zip, build a dictionary of numbers from zero to fifteen and the hexadecimal equivalent (string is fine).

Using the dictionary from item 1: Make a dictionary using the same keys but with the number of ts in each value.

Create sets s2, s3 and s4 that contain numbers from zero through twenty, divisible 2, 3 and 4.

Display the sets.

Display if s3 is a subset of s2 (False)

and if s4 is a subset of s2 (True).
Create a set with the letters in Python and add i to the set.
Create a frozenset with the letters in marathon
display the union and intersection of the two sets.

'''

if __name__ == "__main__":
    d = {"name":"Chris", "city":"Seattle", "cake":"Chocolate"}
    print d
    
    d.pop('cake')
    print d
    
    d['fruit'] = 'Mango'
    print d
     
    print d.values()
    
    print d.has_key('cake')
    print 'Mango' in d.values()
    
    nums = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,14, 15)
    hexes = ('0x0', '0x1', '0x2', '0x3', '0x4','0x5', '0x6', '0x7', '0x8', '0x9', '0xa', '0xb', '0xc', '0xd', '0xe', '0xf')
    hexdict = dict (zip(nums, hexes))
    print hexdict
    
    for key in d:
        d[key] = d[key].count('t')
    print d
    
    #Create sets s2, s3 and s4 that contain numbers from zero through twenty, divisible 2, 3 and 4.
    s2 = set()
    s3 = set()
    s4 = set()
    for i in range (0,21):
        if i % 2 == 0:
            s2.add(i)
        if i % 3 == 0:
            s3.add(i) 
        if i % 4 == 0:
            s4.add(i)  
    print s2
    print s3
    print s4
    
    #Display if s3 is a subset of s2 (False)
    print s3.issubset(s2)
    
    #and if s4 is a subset of s2 (True).
    print s4.issubset(s2)
    
    #Create a set with the letters in Python and add i to the set.
    py = set(list('python'))
    py.add('i')
    print py
    
    #Create a frozenset with the letters in marathon
    fs = frozenset (list('marathon'))
    print fs
    
    #display the union and intersection of the two sets.   
    print py.union(fs)
    print py.intersection(fs)
    
    