food_prefs = {"name": "Chris", "city": "Seattle", "cake": "chocolate",
              "fruit": "mango", "salad": "caesar", "pasta": "lasagna"}

print("{name} is from {city} he likes {cake} cake,\n{fruit} smoothies, extra dressing \
on his {salad}\nsalads and always asks for seconds of {pasta}.".format(**food_prefs))

