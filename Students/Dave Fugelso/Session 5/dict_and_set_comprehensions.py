'''
Lets revisiting the dict/set lab - see how much you can do with comprehensions instead.

Specifically, look at these:

First a slightly bigger, more interesting (or at least bigger..) dict:

food_prefs = {"name": u"Chris",
              u"city": u"Seattle",
              u"cake": u"chocolate",
              u"fruit": u"mango",
              u"salad": u"greek",
              u"pasta": u"lasagna"}
1. Print the dict by passing it to a string format method, so that you get something like:

"Chris is from Seattle, and he likes chocolate cake, mango fruit,
greek salad, and lasagna pasta"
2. Using a list comprehension, build a dictionary of numbers from zero to fifteen and the hexadecimal equivalent (string is fine).

Do the previous entirely with a dict comprehension - should be a one-liner
4. Using the dictionary from item 1: Make a dictionary using the same keys but with the number of "A"s in each value. You can do this either by editing 
the dict in place, or making a new one. If you edit in place, make a copy first!

5. Create sets s2, s3 and s4 that contain numbers from zero through twenty, divisible 2, 3 and 4.

Do this with one set comprehension for each set.
What if you had a lot more than 3? - Dont Repeat Yourself (DRY)
create a sequence that holds all three sets
loop through that sequence to build the sets up - so no repeated code.
Extra credit: do it all as a one-liner by nesting a set comprehension inside a list comprehension. (OK, that may be getting carried away!)
'''

food_prefs = {"name": u"Chris", u"city": u"Seattle", u"cake": u"chocolate", u"fruit": u"mango", u"salad": u"greek", u"pasta": u"lasagna"}
              
if __name__ == "__main__":

    #1. Print the dict by passing it to a string format method, so that you get something like:
    #"Chris is from Seattle, and he likes chocolate cake, mango fruit, greek salad, and lasagna pasta"
    print "{name} is from {city}, and he likes {cake} cake, {fruit} fruit, {salad} salad, and {pasta} pasta.".format(**food_prefs)   
  
    #2. Using a list comprehension, build a dictionary of numbers from zero to fifteen and the hexadecimal equivalent (string is fine).
    d =dict()
    print [d.setdefault(n,hex(n)) for n in range(0, 15)]
    print d
    
    
    #3.Do the previous entirely with a dict comprehension - should be a one-liner  
    print {n:hex(n) for n in range(0, 15)}
    
    
    #4. Using the dictionary from item 1: Make a dictionary using the same keys but with the number of "A"s in each value. You can do this either by editing 
    #the dict in place, or making a new one. If you edit in place, make a copy first!
    print {key:food_prefs[key].replace('a',str( food_prefs[key].count('a'))) for key in food_prefs}
    print food_prefs
   
   
    #5. Create sets s2, s3 and s4 that contain numbers from zero through twenty, divisible 2, 3 and 4.   

    #Do this with one set comprehension for each set.
    #What if you had a lot more than 3? - Dont Repeat Yourself (DRY)
    #create a sequence that holds all three sets
    #loop through that sequence to build the sets up - so no repeated code.
    #Extra credit: do it all as a one-liner by nesting a set comprehension inside a list comprehension. (OK, that may be getting carried away!)  
    s2 = {n for n in range(0, 21) if n % 2 == 0}
    s3 = {n for n in range(0, 21) if n % 3 == 0}
    s4 = {n for n in range(0, 21) if n % 2 == 0}
    print s2, s3, s4
    # or
    print [ {n for n in range(0, 21) if n%m == 0} for m in range(2, 5)]
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
    