def incremental(n):
    l = []
    for i in range(n):
        l.append(lambda x, e=i: x + e)
    return l
