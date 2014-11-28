def ack(m, n):
    if m == 0:
        return(n + 1)
    elif m > 0 and n == 0:
        return ack(m - 1, 1)
    elif m > 0 and n > 0:
        return ack(m -1, ack(m, n - 1))

if __name__ == "__main__":
    # execute only if run as a script
    main()
    #for m in range(0, 5):
    #    for n in range(0, 5):
    #        ack(m, n)
    #        print  n + 1
    #print "All Tests Pass"


