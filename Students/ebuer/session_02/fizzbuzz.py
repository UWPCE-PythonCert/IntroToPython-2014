
def fizzbuzz(rng):
    for r in rng:
        if not r % 3 and not r % 5:
            print "fizzbuzz"
        elif not r % 3:
            print "fizz"
        elif not r % 5:
            print "buzz"
        else:
            print r

GLOBAL_RANGE = range(100)

fizzbuzz(GLOBAL_RANGE)

print locals()
