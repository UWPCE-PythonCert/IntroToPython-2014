"""
For honesty purposes each answer should be recorded before testing
    the comprehension

    feast: return each delicacy capitalized
    result: correct prediction

    comprehension[0] = 'Lambs'
    comprehension[1] = 'Orangutan'

    spam feast: spam and sloths will be dropped len(x) <= 6
    result: correct prediction

    len(feast) will be 5 -- unchanged
    len(comprehension) will be  3 -- shortened

    lumberjack, inquisitioninquisition, spamspamspamspam
    len(comprehension[2]) = 16
    result: correct prediction

    should print out pairs of eggs and hams
    result: correct prediction

    len(comprehension) is 6
    comprehension[1] is poached egg and ham spam

    comprehension of the string is the same as the string
    WRONG!  Brackets made the comprehension a set!

    Rewrite the key for the dictionary with all keys in CAPS
"""

# expanded dict lab with comprehensions
food_prefs = {"name": u"Chris",
              u"city": u"Seattle",
              u"cake": u"chocolate",
              u"fruit": u"mango",
              u"salad": u"greek",
              u"pasta": u"lasagna"}

print "{name} is from {city}.  He likes {cake} cake, {fruit} fruit, {salad} salad, and {pasta}.\n".format(**food_prefs)

# write numbers 0 to 15 and the hex equivalent in 1 line
num_dict = {k: v for k, v in zip(range(16), [hex(h) for h in range(16)])}

print num_dict

# new dictionary with the same keys but the number of a's in each entry
a_dict = {k: v.count('a') for k, v in food_prefs.items()}

print a_dict

# create s2, s3, and s4 for range(21) using comprehensions DRY
s2 = set(n for n in range(21) for s in [2] if n % s is 0)
s3 = set(n for n in range(21) if n % 3 is 0)
s4 = set(n for n in range(21) if n % 4 is 0)

# using a single expression:
setlist = [set(n for n in range(21) if n % v is 0) for v in [2, 3, 4]]
print setlist
