data = ( ('George', 'a goldfish'),
         ('Joe', 'several small pieces of lint'),
         ('Jennifer','a red wagon')
         )

template = """
Dear %s,

Thank you so much for your gift of %s. I will treasure it
forever. I've always wanted an excuse to get %s, and now I
don't have to pay for it!

Please enjoy this form letter as a token of my sincere appreciation.
"""

for name, gift in data:
    print 'Filling template for %s' % name
    message = template%(name, gift, gift)
    file_name = 'thank_you_%s.txt' % name.lower()
    f = open(file_name, 'w')
    f.write(message)
    f.close()
