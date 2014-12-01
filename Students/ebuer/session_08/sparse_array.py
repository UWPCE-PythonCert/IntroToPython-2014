"""
sparse_array.py

self.values = {}
for i, val in enumerate(iterable):
        if val:
            self.values[i] = val
"""

class SparseArray(object):

    def __init__(self, iterable):
        self.length = len(iterable)
        self.values = {i: j for i, j in enumerate(iterable) if i}
        print self.values

    def __call__(self):
        pass

    def __len__(self):
        return self.length

    def __getitem__(self, index):
        if index >= self.length:
            raise IndexError ("sparse array index out of range")
        else:
            return self.values.get(index, 0)

    def __setitem__(self, index, value):
        if index >= self.length:
            raise IndexError ("sparse array index out of range")
        else:
            if value == 0:
                self.values.pop(index, None)
            else:
                self.values[index] = value

    def __delitem__(self, index):
        if index >= self.length:
            raise IndexError ("sparse array index out of range")
        else:
            self.values.pop(index, None)

        self.length -= 1

    def __contains__(self):
        pass