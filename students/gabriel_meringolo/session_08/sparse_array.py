

class SparseArray:

    def __init__(self, *args):
        self.array = {}
        self.length = 0
        self.sparse = []
        for i in args:
            self.length += 1
            if i != 0:
                self.array[args.index(i)] = i

    def __str__(self):
        for i in range(self.length):
            if i in self.array.keys():
                self.sparse.append(self.array[i])
            else:
                self.sparse.append(0)
        return str(self.sparse)

    def __repr__(self):
        return str(self.array)

    def __len__(self):
        return self.length

    def __getitem__(self, item):
        try:
            return self.array[item]
        except:
            return 0

    def __setitem__(self, key, value):
        self.array[key] = value

    def __delitem__(self, key):
        del[self.array[key]]


sa = SparseArray(1, 2, 3, 4, 0, 6, 0, 0, 9)


print(repr(sa))
print(sa)
