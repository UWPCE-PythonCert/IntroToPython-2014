#!/usr/bin/env python2.7

# # 1:
d = {"name": "Chris", "city": "Seattle", "cake": "Chocolate"}
print d

# delete the cake entry
d.pop("cake")
print d

d2 = {"fruit": "mango"}
d.update(d2)
print d
print d.keys()
print d.values()
print "Is 'cake' in 'd'?:", ("cake" in d)

# #2: Dictionary of integers and hex equivalents
l1=[]
l2=[]
for i in range(16):
    l1.append(i)
    l2.append(hex(i))

newdict = dict( zip(l1, l2) )
print newdict
# 3: Dictionary of same keys as #1 above, but with values which are the 
# number of t's in the previous values.
d = {"name": "Chris", "city": "Seattle", "cake": "Chocolate"}
print d
dts = {}
for k, v in d.items():
    dts.update({k: v.count("t")})

print dts

# #4: sets s2, s3, and s4 containing those numbers from 0-20 which are 
# evenly divisible by 2, 3, and 4, respectively
s2 = set()
s3 = set()
s4 = set()

for i in range(21):
    if(i%2 == 0):
        s2.update([i])
    if(i%3 == 0):
        s3.update([i])
    if(i%4 == 0):
        s4.update([i])

print "s2 = ", s2
print "s3 = ", s3
print "s4 = ", s4

print "Is s3 a subset of s2?", s3.issubset(s2)
print "Is s4 a subset of s2?", s4.issubset(s2)

# #5: 'Python' set and 'marathon' set
pyset = set()
for c in "Python":
    pyset.update([c])
pyset.update(["i"])

print pyset

marathon_set = set()
for c in "marathon":
    marathon_set.update([c])
marathon_set = frozenset(marathon_set)

print "Union of 'Python' and 'marathon':", pyset.union(marathon_set)
print "Intersection of 'Python' and 'marathon':", pyset.intersection(marathon_set)
