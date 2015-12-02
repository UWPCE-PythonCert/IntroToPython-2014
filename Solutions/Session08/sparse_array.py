
"""
Example of emulating a sequence using slices

This class impliments a "sparse" array i.e. on with a lot of zero values.
Only the non-zero vlaues are stored.
"""

class SparseArray(object):

    def __init__(self, my_array=()):
        self._length = len(my_array)
        self.nonzero = self._convert_to_sparse(my_array)

    def _convert_to_sparse(self, my_array):
        nonzero = {}
        for index, value in enumerate(my_array):
            if value: # remember that zero is Falsey
                nonzero[index] = value
        return nonzero

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            # if it's the same class, can do direct check
            return (self._length == other._length) and (self.nonzero == other.nonzero)
        else:
            # arbitrary sequence -- need to loop
            try:
                if self._length != len(other):
                    #if it's the wrong length, no need to do more
                    return False
            except TypeError: # not a sequence
                return False
            # this could still fail if an object has a length, but can't be looped through 
            for val1, val2 in zip(self, other):
                if val1 != val2:
                    return False
            return True

    def __len__(self):
        return self._length

    def __str__(self):
        if self._length < 6:
            # just use the __repr__
            return self.__repr__()
        else:  # don't want to display the whole thing
            return "SparseArray of length: {} with {} non-zero elements".format(self._length, len(self.nonzero))

    def __repr__(self):
        msg = []
        msg = ["{:s}".format(repr(self[i])) for i in range(self._length)]
        msg = "SparseArray([" + ", ".join(msg) + "])"
        return msg

    def _get_single_value(self, index):
        """ returns a single value -- used by __getitem__"""
        # handle negative indexes
        index = self._length + index  if index < 0 else index
        if (index >= self._length) or (index < 0):
            raise IndexError('array index out of range')
        else:
            return self.nonzero.get(index, 0)

    def _get_slice(self, slice_): # naem with underscore to not mirror built-in
        """ returns a slice -- used by __getitem__"""
        # create an empty sparse array
        slice_array = self.__class__([])
        # populate it one by one
        for i in range(*slice_.indices(self._length)):
            slice_array.append(self[i])
        return slice_array
        
    def __getitem__(self, index):
        if isinstance(index, slice):
            return self._get_slice(index)
        else:
            # get an integer from an object that can be used as an index.
            index = index.__index__()
            return self._get_single_value(index)

    def _set_single_value(self, index, value):
        if index >= self._length:
            # expand to fit
            self._length = index+1
        if value != 0:
            self.nonzero[index] = value
        else:
            # if the value is being set to zero, we may need to
            # remove a key from the dictionary.
            self.nonzero.pop(index, None)

    def _set_slice(self, slice_, seq):
        """ set values to a slice - used by __setitem__"""
            
        start, stop, step = slice_.indices(self._length)
        slice_len = (stop - start) // step 
        try:
            if len(seq) != slice_len:
                raise ValueError("attempt to assign sequence of size {} to "
                                 "extended slice of size {}"
                                 .format(len(seq), slice_len)
                                 )
        except TypeError:
            raise TypeError("must assign iterable to slice")
        # now do it one by one:
        for i, value in zip(range(start, stop, step), seq):
            self._set_single_value(i, value)

    def __setitem__(self, index, value):
        # handle slices separately
        if isinstance(index, slice):
            self._set_slice(index, value)
        else:
            # get an integer from an object that can be used as an index.
            index = index.__index__() 
            self._set_single_value(index, value)


    # def __setitem__(self, index, value):
    #     # handle slices separately
    #     if isinstance(index, slice):
    #         start, stop, step = index.indices(len(self))
    #         if step is None:
    #             step = 1
    #         key = start
    #         new_values = []
    #         new_keys = []
    #         for each in value:
    #             if key < stop:
    #                 self[key] = each
    #             else:
    #                 # now instead of replacing values, we need to add (a) value(s) in the center,
    #                 # and move stuff over, probably want to collect all of the changes,
    #                 # and then make a new dictionary
    #                 new_values.append(each)
    #                 new_keys.append(key)
    #             key += step
    #         if new_keys:
    #             self.add_in_slice(new_keys, new_values)
    #     else:
    #         index = index.__index__()
    #         self._set_single_value(index, value)

    def append(self, value):
        self[self._length] = value

    def add_in_slice(self, new_keys, new_values):
        # sometimes we need to add in extra values
        # any existing values
        # greater than the last key of the new data
        # will be increased by how many
        new_dict = {}
        slice_length = len(new_keys)
        for k, v in self.nonzero.items():
            if k >= new_keys[-1]:
                # if greater than slice, change key
                new_dict[k + slice_length] = v
            elif k in new_keys:
                # if this is a key we are changing, change it,
                # unless we are changing to a zero...
                new_value = values[new_keys.index(k)]
                if new_value != 0:
                    new_dict[k] = new_value
            else:
                new_dict[k] = v
        # what if our new key was not previously in the dictionary?
        # stick it in now
        for k in new_keys:
            if k not in new_dict.keys():
                new_dict[k] = new_values[new_keys.index(k)]
        # note we don't want to do update, since we need to make sure we are
        # getting rid of the old keys, when we moved the value to a new key
        self.nonzero = new_dict
        # now we need to increase the length by the amount we increased our array by
        self._length += slice_length

    def __delitem__(self, key):
        # we probably need to move the keys if we are not deleting the last
        # number, use pop in case it was a zero
        if key == self._length - 1:
            self.nonzero.pop(key, None)
        else:
            # since we need to adjust all of the keys after the one we are
            # deleting, probably most efficient to create a new dictionary
            new_dict = {}
            for k, v in self.nonzero.items():
                if k >= key:
                    new_dict[k - 1] = v
                else:
                    new_dict[k] = v
            # note we don't want to do update, since we need to make sure we are
            # getting rid of the old keys, when we moved the value to a new key
            self.nonzero = new_dict
        # length is now one shorter
        self._length -= 1

