def makegrid(n):
    if n % 2 != 0:
        n += 1
    hN = int(n / 2)
    top = ("+ " + ("- " * hN )) * 2 + "+\n"
    side = (("|" + " " * (n + 1)) * 2) + "|\n"
    print(top + side * hN + top + side * hN + top)
   # print(n)
   # print(hN)
   # print(top)

makegrid(11)