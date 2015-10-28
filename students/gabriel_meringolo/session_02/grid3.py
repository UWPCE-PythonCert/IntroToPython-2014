def makegrid(n,i):
    if n % 2 != 0:
        n += 1
    hN = int(n / 2)
    top = ("+ " + ("- " * hN )) * i + "+\n"
    side = (("|" + " " * (n + 1)) * i) + "|\n"
    row = (top + side * hN)
    print(row * i  + top)
    #print(row)


makegrid(10,7)