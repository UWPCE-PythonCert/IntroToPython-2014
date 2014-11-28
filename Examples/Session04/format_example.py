def print_me( nums ):
    formatter = "the first %d numbers are: " + ", ".join( ["%i"] * len(nums) )
    print "formatter: ", formatter
    print formatter%(( len(nums), ) + nums)

print_me( (2,3,4,5) )

