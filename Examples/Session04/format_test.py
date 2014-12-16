def print_msg(t):
    print ("the first %i numbers are: " + ", ".join(["%i"] * len(t)) ) % ((len(t),) + t)

