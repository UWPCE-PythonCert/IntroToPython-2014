diction = {"name":"Chris", "city":"Seattle", "cake":"Chocolate"}

print (diction)

del diction["cake"]

diction["fruit"] = 'mango'

print (diction.keys())
print (diction.values())

print ("cake" in diction)
print ("mango" in diction.values())


new_diction = {}
for keys in diction:
	new_diction[keys] = diction[keys].count("t")

print (new_diction)


s2 = {x for x in range(0,21) if x%2 == 0}
s3 = {x for x in range(0,21) if x%3 == 0}
s4 = {x for x in range(0,21) if x%4 == 0}

print (s2, "\n", s3, "\n", s4)


print (s3.issubset(s2))
print (s4.issubset(s2))

pySet = {x for x in "python"}
pySet.update("i")

fzSet = frozenset({x for x in "marathon"})


print (pySet.union(fzSet))
print (pySet.intersection(fzSet))





