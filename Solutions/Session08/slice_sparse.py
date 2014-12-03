
"""
example of emulating a sequence using slices
"""

class SparseArray(object):

    def __init__(self, my_array=()):
        self.length = len(my_array)
        self.sparse_array = self.convert_to_sparse(my_array)

    def convert_to_sparse(self, my_array):
        sparse_array = {}
        for index, number in enumerate(my_array):
            if number:
                sparse_array[index] = number
        return sparse_array

    def __len__(self):
        return self.length

    def __getitem__(self, index):
        #print('index', index)
        #print('length', self.length)
        # create a list of the slice they want returned
        mini_array = []
        if isinstance(index, int):
            return self.get_single_value(index)
        elif isinstance(index, slice):
            start, stop, step = index.indices(len(self))
            if step is None:
                step = 1
            key = start
            mini_array = []
            while key < stop + 1:
                #print('key', key)
                mini_array.append(self.get_single_value(key))
                key += step
        else:
            raise TypeError("index must be int or slice")
        return mini_array[:]

    def get_single_value(self, key):
        if key >= self.length:
            raise IndexError('array index out of range')
        else:
            return self.sparse_array.get(key, 0)

    def __setitem__(self, index, value):
        if isinstance(index, int):
            self.set_single_value(index, value)
        elif isinstance(index, slice):
            start, stop, step = index.indices(len(self))
            if step is None:
                step = 1
            key = start
            for each in value:
                #print('key', key)
                self.set_single_value(key, each)
                key += step
        else:
            raise TypeError("index must be int or slice")

    def set_single_value(self, key, value):
        if key > self.length:
            raise IndexError('array assignment index out of range')
        if value != 0:
            self.sparse_array[key] = value
        else:
            # if the value is being set to zero, we probably need to 
            # remove a key from our dictionary.
            self.sparse_array.pop(key, None)

    def __delitem__(self, key):
        # we probably need to move the keys if we are not deleting the last 
        # number, use pop in case it was a zero
        if key == self.length - 1:
            self.sparse_array.pop(key, None)
        else:
            # since we need to adjust all of the keys after the one we are 
            # deleting, probably most efficient to create a new dictionary
            new_dict = {}
            for k, v in self.sparse_array.iteritems():
                if k >= key:
                    new_dict[k - 1] = v
                else:
                    new_dict[k] = v
            # note we don't want to do update, since we need to make sure we are
            # getting rid of the old keys, when we moved the value to a new key
            self.sparse_array = new_dict
        # length is now one shorter
        self.length -= 1




