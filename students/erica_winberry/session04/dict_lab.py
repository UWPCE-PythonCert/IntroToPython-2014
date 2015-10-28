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
if "Mango" in d.values():
    print("True")