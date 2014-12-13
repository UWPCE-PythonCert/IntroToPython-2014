#!usr/local/bin/python


class SparseArray(object):
    """
    Use a dictionary to store the location of the values.  Then, if the user
    asks for a key that isn't in the dictionary, but it should exist, then
    return zero.
    """
    def __init__(self, sequence):
        self.data = {k: v for k, v in enumerate(sequence) if v != 0}
        self.mylen = len(sequence)
        self.current = -1

    def get_value(self, idx):
        try:
            return self.data[idx]
        except KeyError:
            if idx < self.mylen:
                return 0
            else:
                raise IndexError

    def __len__(self):
        return self.mylen

    def __getitem__(self, idx):
        if isinstance(idx, slice):
            l = []
            start, stop, stride = idx.indices(len(self))
            for i in xrange(start, stop):
                l.append(self.get_value(i))
            return l
        else:
            return self.get_value(idx)

    def __setitem__(self, idx, value):
        if idx < self.mylen:
            try:
                del self.data[idx]
            except KeyError:
                pass
            finally:
                if value != 0:
                    self.data[idx] = value
        else:
            raise IndexError

    def __delitem__(self, idx):
        if idx < self.mylen:
            self.mylen -= 1
            try:
                del self.data[idx]
            except KeyError:
                pass
            finally:
                d = {}
                for k, v in self.data.iteritems():
                    if k > idx:
                        d[k - 1] = v
                    else:
                        d[k] = v
                self.data = d
        else:
            raise IndexError

    def __iter__(self):
        self.current = -1
        return self

    def next(self):
        if self.current + 1 < self.mylen:
            self.current += 1
            return self.get_value(self.current)
        else:
            raise StopIteration
