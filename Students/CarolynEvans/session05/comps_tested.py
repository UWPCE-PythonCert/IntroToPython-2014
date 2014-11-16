
# The following functions are tested in test.py

def count_evens(nums):
    return len([x for x in nums if x%2==0])

def print_food_prefs(d):
        return "{name} is from {city}, and he likes {cake} cake, {fruit} fruit, {salad} salad, and {pasta} pasta.".format(**d)

def hex_dict():
    return { i: hex(i) for i in range(0,16) }

def count_a(d):
      return { k:v.count('a') for k, v in d.iteritems()}

def mod_0_list(*args, **kwargs):
    """
    This functions returns sets of numbers that are evenly divisible by the given divisors.
    :param args: Contains the list of divisors.
    :param kwargs: Contains the beginning and ending numbers of the range to be tested.
    :return: Returns a list of numbers for each given divisor.
    """
    return [[i for i in range(kwargs['start'], kwargs['end'] + 1) if i%divisor == 0] for divisor in args]


