
"""
An example of emulating a sequence

A SparseArray is like a list, but only stores the non-zero values

It can be indexed, appended-to, and iterated through.
"""


class SparseArray(object):

    def __init__(self, my_array=()):
        """
        initilize a sparse array

        :param my_array: an initial sequence to start with
                         if there are zeros in it, they wil not be stored
        """
        self.length = len(my_array)
        # self.sparse_array is a dict that stores only the non-zero items
        self.sparse_array = self.convert_to_sparse(my_array)

    def convert_to_sparse(self, my_array):
        sparse_array = {}
        for index, number in enumerate(my_array):
            if number:  # remember that zeros are falsey.
                sparse_array[index] = number
        # or the dict comprehension method:
        # sparse_array = {index:number for index, number in enumerate(my_array) if number}
        return sparse_array

    def __len__(self):
        return self.length

    def __getitem__(self, key):
        # fixme: doesn't handle negative indexes properly
        try:
            return self.sparse_array[key]
        except KeyError:
            if key >= self.length:
                raise IndexError('array index out of range')
            return 0

    def __setitem__(self, key, value):
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
        if key == self.length - 1:  # it's the last item -- easy.
            self.sparse_array.pop(key, None)
        else:
            # since we need to adjust all of the keys after the one we are
            # deleting, probably most efficient to create a new dictionary
            new_dict = {}
            for k, v in self.sparse_array.items():
                if k >= key:
                    new_dict[k - 1] = v
                else:
                    new_dict[k] = v
            # note we don't want to do update, since we need to make sure we are
            # getting rid of the old keys, when we moved the value to a new key
            self.sparse_array = new_dict
        # length is now one shorter
        self.length -= 1
