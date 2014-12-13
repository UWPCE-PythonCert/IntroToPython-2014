class SparseArray(object):
    def __init__(self, iterable):
        self.values = {}
        self.length = len(iterable)
        for i, val in enumerate(iterable):
            if val:
                self.values[i] = val
        
    def __getitem__(self, index):
        if index >= self.length:
            raise IndexError("Sparse array index out of range")
        else:
            return self.values.get(index, 0)
    
    def __setitem__(self, index, value):
        if index >= self.length:
            raise IndexError("Sparse array index out of range")
        else:
            if value == 0:
                self.values.pop(index, None)
            else:
                self.values[index] = value
    
    def __delitem__(self, index):
        if index >= self.length:
            raise IndexError("Sparse array index out of range")
        else:
            self.values.pop(index, None)
            self.length -= 1
            
    def __len__(self):
        return self.length
    
