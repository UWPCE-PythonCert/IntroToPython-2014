
def function_builder(n):
    # l = []
    # for i in range(n):
    #     def f(x, inc=i):
    #         return x + inc
    #     l.append(f)
        # l.append(lambda x, inc=i: x + inc)
    # return l
    return [lambda x, inc=i: x + inc for i in range(n)]