

class SparseArray:

    def __init__(self, *args):
        self.length = len(args)
        self.array = args
        self.arrr = {}
        for i in args:
            if i != 0:
                self.arrr[args.index(i)] = i
                #print(dict{args.index(i): i})
        self.arrr["len"] = self.length
        print(self.arrr[len(self.arrr)])

    def __len__(self):
        return self.arrr[-1][1]



SparseArray(1,2,3,4,5,0,0,8,0,0,0,0)

#sa = SparseArray(1,2,3,4,5,0,0,8,0,0,0,0)

#print(len(sa))