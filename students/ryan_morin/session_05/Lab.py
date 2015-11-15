__author__ = 'Ryan'

food_prefs = {"name": u"Chris",
              u"city": u"Seattle",
              u"cake": u"chocolate",
              u"fruit": u"mango",
              u"salad": u"greek",
              u"pasta": u"lasagna"}

# Quesstion 1
print ("{name} is from {city}, and he likes {cake} cake, {fruit}, {salad} salad and {pasta} pasta"
       .format(**food_prefs))

#Question #2 /#3
c = {i:hex(i) for i in range (16)}
print (c)

fp_copy = food_prefs.copy()

#Question #4
d = {i:v.count("a") for i,v in food_prefs.items()}
print (d)

#Qestion#5
e = {i for i in range(21)}
s2 = e.copy()
s3 = e.copy()
s4 = e.copy()

s2 = {(i/2) for i in e}
s3 = {round((i/3),1) for i in e}
s4 = {round((i/4),1) for i in e}

print(s2,s3,s4)

list_a = list(e)
list_b = [2,3,4]

oput = [[(x*y) for x in list_a] for y in list_b ]
print (oput)
