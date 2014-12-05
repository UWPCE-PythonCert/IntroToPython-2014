#!/usr/local/bin/python


def print_dict(a_dict):
    """Returns the printed version of food_prefs dict."""
    s = ('{name} is from {city}, and he likes {cake} cake, {fruit} fruit, '
         '{salad} salad, and {pasta} pasta.')
    print s.format(**a_dict)


def build_dict_list_comp(n):
    """Return a dict with hexadecimal representation range of numbers."""
    a_list = [[k, '{:x}'.format(k)] for k in range(n)]
    return dict(a_list)


def build_dict_dict_comp(n):
    """Return a dict with hexadecimal representation range of numbers."""
    return {k: '{:x}'.format(k) for k in range(n)}


def dict_number_a(a_dict):
    """Return a dict with the number of 'a's."""
    return {k: v.count('a') for k, v in a_dict.iteritems()}


def create_sets():
    s2 = {i for i in range(21) if i % 2 == 0}
    s3 = {i for i in range(21) if i % 3 == 0}
    s4 = {i for i in range(21) if i % 4 == 0}
    print s2
    print s3
    print s4


def create_sets_better():
    l = []
    for x in range(2, 5):
        l.append({i for i in range(21) if i % x == 0})
    return l


def print_sets_better():
    l = []
    for x in range(2, 5):
        l.append({i for i in range(21) if i % x == 0})
    print str('{}\n' * 3).format(*l)


def create_sets_better_comprehension():
    return [{i for i in range(21) if i % x == 0} for x in range(2, 5)]


food_prefs = {"name": u"Chris",
              u"city": u"Seattle",
              u"cake": u"chocolate",
              u"fruit": u"mango",
              u"salad": u"greek",
              u"pasta": u"lasagna"}
