

class SparseArray:

    def __init__(self, *args):
        self.sparse = args
        self.array = {}
        self.length = len(args)
        for i in self.sparse:
            if i != 0:
                self.array[self.sparse.index(i)] = i

    def __repr__(self):
        return "SparseArray{}".format(self.sparse)

    def __str__(self):
        return "{}".format(self.array)

    def __len__(self):
        return self.length


