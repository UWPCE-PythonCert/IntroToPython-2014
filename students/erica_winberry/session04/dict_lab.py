# -- PART 1 --
print("Part 1:")
# Create a dictionary containing “name”, “city”, and “cake” for “Chris” from “Seattle” who likes “Chocolate”.
d = {"name": "Chris", "city": "Seattle", "cake": "Chocolate"}
# Display the dictionary.
print(d)
# Delete the entry for “cake”.
d.pop("cake")
# Display the dictionary.
print(d)
# Add an entry for “fruit” with “Mango” and display the dictionary.
d.update({"fruit": "Mango"})
# Display the dictionary keys.
print(d.keys())
# Display the dictionary values.
print(d.values())
# Display whether or not “cake” is a key in the dictionary (i.e. False) (now).
print(d.get("cake", "Not there!"))
# Display whether or not “Mango” is a value in the dictionary (i.e. True).
print("Mango" in d.values())


# -- PART 2 --
# Using the dictionary from item 1: 
# Make a dictionary using the same keys but with the number of ‘t’s in each value.
print("\nPart 2:")
d2 = d.copy()
for k, v in d2.items():
   d2[k] = (v.count("t"))

print(d2)

# -- PART 3 --
print("\nSets, Part 1:")
# Create sets s2, s3 and s4 that contain numbers from zero through twenty, divisible 2, 3 and 4.
s2 = {2,4,6,8,10,12,14,16,18,20}
s3 = {3,6,9,12,15,18}
s4 = {4,8,12,16,20}
# Display the sets.
print(s2)
print(s3)
print(s4)
# Display if s3 is a subset of s2 (False)
print(s3 <= s2)
# and if s4 is a subset of s2 (True).
print(s4 <= s2)

# -- PART 4 --
print("\nSets, Part 2:")

pyset = {"P", "y", "t", "h", "o", "n"}
pyset.update(["i"])
m_fset = frozenset(("m", "a", "r", "a", "t", "h", "o", "n"))
print(pyset.union(m_fset))
print(pyset.intersection(m_fset))